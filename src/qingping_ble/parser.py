"""
Parser for Qingping BLE advertisements.

This file is shamelessly copied from the following repository:
https://github.com/Ernst79/bleparser/blob/c42ae922e1abed2720c7fac993777e1bd59c0c93/package/bleparser/qingping.py

MIT License applies.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from struct import Struct

from bluetooth_data_tools import short_address
from bluetooth_sensor_state_data import BluetoothData
from home_assistant_bluetooth import BluetoothServiceInfo
from sensor_state_data import BinarySensorDeviceClass, SensorLibrary

_LOGGER = logging.getLogger(__name__)

UNPACK_TEMP_HUMID = Struct("<hH").unpack
UNPACK_PRESSURE = Struct("<H").unpack
UNPACK_MOTION_ILLUM = Struct("<BHB").unpack
UNPACK_ILLUMINANCE = Struct("<I").unpack
UNPACK_PM = Struct("<HH").unpack
UNPACK_CO2 = Struct("<H").unpack


@dataclass
class QingpingDevice:
    model: str
    name: str


DEVICE_TYPES = {
    0x01: QingpingDevice("CGG1", ""),
    0x04: QingpingDevice("CGH1", "Door/Window Sensor"),  # Door/Window Sensor
    0x07: QingpingDevice("CGG1", ""),
    0x09: QingpingDevice("CGP1W", ""),
    0x0C: QingpingDevice("CGD1", "Alarm Clock"),
    0x0E: QingpingDevice("CGDN1", "Air Monitor Lite"),
    0x0F: QingpingDevice("CGM1", "Lee Guitars Thermo-Hygrometer"),
    0x12: QingpingDevice("CGPR1", "Motion & Light"),
    0x15: QingpingDevice("CGF1W", "Temp RH Pro E"),
    0x16: QingpingDevice("CGG1", "Temp RH M"),
    0x18: QingpingDevice("CGP23W", "Temp & RH Monitor Pro"),
    0x1E: QingpingDevice("CGC1", "BT Clock Lite"),
    0x24: QingpingDevice("CGDN1", "Air Monitor Lite"),
    0x26: QingpingDevice("CGP23W", "Temp RH Baro Pro S"),
    0x33: QingpingDevice("CGP22C", "CO2 Temp RH"),
    0x4F: QingpingDevice("CGG3", "Temp RH M"),
    0x5D: QingpingDevice("CGP22C", "CO2 Temp RH"),
}


SERVICE_DATA_UUID = "0000fdcd-0000-1000-8000-00805f9b34fb"


class QingpingBluetoothDeviceData(BluetoothData):
    """Date update for Qingping Bluetooth devices."""

    def _start_update(self, service_info: BluetoothServiceInfo) -> None:
        """Update from BLE advertisement data."""
        _LOGGER.debug("Parsing qingping BLE advertisement data: %s", service_info)
        lower_name = service_info.name.lower()
        if SERVICE_DATA_UUID not in service_info.service_data:
            return
        unpadded_data = service_info.service_data[SERVICE_DATA_UUID]
        if len(unpadded_data) < 2:
            return
        data = b"\x00\x00\x00\x00" + unpadded_data
        device_id = data[5]
        if not (device := DEVICE_TYPES.get(device_id)):
            _LOGGER.debug("Device type %s is not supported", device_id)
            return
        if device.name:
            name = device.name
        elif lower_name.startswith("qingping "):
            name = service_info.name[9:]
        else:
            name = service_info.name
        self.set_device_type(device.model)
        self.set_title(f"{name} {short_address(service_info.address)}")
        self.set_device_name(f"{name} {short_address(service_info.address)}")
        self.set_device_manufacturer("Qingping")
        self._process_update(data)

    def _process_update(self, data: bytes) -> None:
        """Update from BLE advertisement data."""
        _LOGGER.debug("Parsing Qingping BLE advertisement data: %s", data)
        msg_length = len(data)
        if msg_length < 12:
            return
        # hlen byte: bit 6 set means the advertisement carries an event
        # (e.g. motion-change). In event packets the trailing bytes of the
        # 0x08 (motion+illuminance) chunk do not contain a valid illuminance
        # reading. See https://github.com/pvvx/TLB2Z ble_scaning.c.
        is_event = bool(data[4] & 0x40)
        xdata_point = 14
        while xdata_point < msg_length:
            xdata_id = data[xdata_point - 2]
            xdata_size = data[xdata_point - 1]
            if xdata_point + xdata_size <= msg_length:
                self._process_xdata(
                    xdata_id,
                    xdata_size,
                    data[xdata_point : xdata_point + xdata_size],
                    is_event,
                )
            xdata_point += xdata_size + 2

    def _process_xdata(
        self, xdata_id: int, xdata_size: int, xdata: bytes, is_event: bool = False
    ) -> None:
        if xdata_id == 0x01 and xdata_size == 4:
            (temp, humi) = UNPACK_TEMP_HUMID(xdata)
            self.update_predefined_sensor(SensorLibrary.TEMPERATURE__CELSIUS, temp / 10)
            self.update_predefined_sensor(SensorLibrary.HUMIDITY__PERCENTAGE, humi / 10)
        elif xdata_id == 0x02 and xdata_size == 1:
            self.update_predefined_sensor(SensorLibrary.BATTERY__PERCENTAGE, xdata[0])
        elif xdata_id == 0x04 and xdata_size == 1:
            closed = xdata[0]
            self.update_predefined_binary_sensor(
                BinarySensorDeviceClass.DOOR, closed in (0, 2)
            )
            self.update_predefined_binary_sensor(
                BinarySensorDeviceClass.PROBLEM,
                closed == 2,  # left open
                key=(None, "door_left_open"),
                name="Door left open",
            )
        elif xdata_id == 0x07 and xdata_size == 2:
            (pressure,) = UNPACK_PRESSURE(xdata)
            self.update_predefined_sensor(SensorLibrary.PRESSURE__MBAR, pressure / 10)
        elif xdata_id == 0x08 and xdata_size == 4:
            (motion, illuminance_1, illuminance_2) = UNPACK_MOTION_ILLUM(xdata)
            self.update_predefined_binary_sensor(
                BinarySensorDeviceClass.MOTION, bool(motion)
            )
            # Only the motion byte is valid in event packets; the trailing
            # bytes are not illuminance and produce spurious spikes (#84).
            if not is_event:
                self.update_predefined_sensor(
                    SensorLibrary.LIGHT__LIGHT_LUX,
                    illuminance_1 + (illuminance_2 << 16),
                )
        elif xdata_id == 0x09 and xdata_size == 4:
            (illuminance,) = UNPACK_ILLUMINANCE(xdata)
            self.update_predefined_sensor(SensorLibrary.LIGHT__LIGHT_LUX, illuminance)
        elif xdata_id == 0x11 and xdata_size == 1:
            self.update_predefined_binary_sensor(
                BinarySensorDeviceClass.LIGHT, bool(xdata[0])
            )
        elif xdata_id == 0x12 and xdata_size == 4:
            (pm2_5, pm10) = UNPACK_PM(xdata)
            self.update_predefined_sensor(
                SensorLibrary.PM25__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, pm2_5
            )
            self.update_predefined_sensor(
                SensorLibrary.PM10__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, pm10
            )
        elif xdata_id == 0x13 and xdata_size == 2:
            (co2,) = UNPACK_CO2(xdata)
            self.update_predefined_sensor(
                SensorLibrary.CO2__CONCENTRATION_PARTS_PER_MILLION, co2
            )
        elif xdata_id == 0x18 and xdata_size == 2:
            # Static 2-byte hardware capability bitmap (screen type, power
            # source, Wi-Fi capabilities, ...), not a sensor reading. On the
            # CGP22C it is always 0x0122, which #96 misread as CO2 and used to
            # overwrite the real 0x13 value with a constant 290 ppm (#72, #115).
            # CO2 is always broadcast as TLV id 0x13; confirmed against
            # Qingping's internal BLE protocol spec in #115.
            pass
        elif xdata_id == 0x0F and xdata_size == 1:
            pass
            # packet_id = unpack("B", xdata)[0]
            # result.update({"packet": packet_id})
        else:
            _LOGGER.debug(
                "Unknown data received from Qingping device: %s",
                xdata.hex(),
            )
