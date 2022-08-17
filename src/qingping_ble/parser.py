"""Parser for Qingping BLE advertisements.

This file is shamelessly copied from the following repository:
https://github.com/Ernst79/bleparser/blob/c42ae922e1abed2720c7fac993777e1bd59c0c93/package/bleparser/qingping.py

MIT License applies.
"""
from __future__ import annotations

import logging
from struct import unpack

from bluetooth_sensor_state_data import BluetoothData
from home_assistant_bluetooth import BluetoothServiceInfo
from sensor_state_data import BinarySensorDeviceClass, SensorLibrary

_LOGGER = logging.getLogger(__name__)

DEVICE_TYPES = {
    0x01: "CGG1",
    0x07: "CGG1",
    0x09: "CGP1W",
    0x12: "CGPR1",
    0x0C: "CGD1",
    0x0E: "CGDN1",
}

SERVICE_DATA_UUID = "0000fdcd-0000-1000-8000-00805f9b34fb"


def short_address(address: str) -> str:
    """Convert a Bluetooth address to a short address."""
    split_address = address.replace("-", ":").split(":")
    return f"{split_address[-2].upper()}{split_address[-1].upper()}"[-4:]


class QingpingBluetoothDeviceData(BluetoothData):
    """Date update for Qingping Bluetooth devices."""

    def _start_update(self, service_info: BluetoothServiceInfo) -> None:
        """Update from BLE advertisement data."""
        _LOGGER.debug("Parsing qingping BLE advertisement data: %s", service_info)
        lower_name = service_info.name.lower()
        if "qingping" not in lower_name:
            return
        if SERVICE_DATA_UUID not in service_info.service_data:
            return
        unpadded_data = service_info.service_data[SERVICE_DATA_UUID]
        data = b"\x00\x00\x00\x00" + unpadded_data
        device_id = data[5]
        if device_id := DEVICE_TYPES.get(device_id):
            self.set_device_type(device_id)
        else:
            return
        name = (
            service_info.name[9:]
            if lower_name.startswith("qingping ")
            else service_info.name
        )
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
        xdata_point = 14
        while xdata_point < msg_length:
            xdata_id = data[xdata_point - 2]
            xdata_size = data[xdata_point - 1]
            if xdata_point + xdata_size <= msg_length:
                self._process_xdata(
                    xdata_id,
                    xdata_size,
                    data[xdata_point : xdata_point + xdata_size],  # noqa: E203
                )
            xdata_point += xdata_size + 2

    def _process_xdata(self, xdata_id: int, xdata_size: int, xdata: bytes) -> None:
        if xdata_id == 0x01 and xdata_size == 4:
            (temp, humi) = unpack("<hH", xdata)
            self.update_predefined_sensor(SensorLibrary.TEMPERATURE__CELSIUS, temp / 10)
            self.update_predefined_sensor(SensorLibrary.HUMIDITY__PERCENTAGE, humi / 10)
        elif xdata_id == 0x02 and xdata_size == 1:
            batt = unpack("B", xdata)[0]
            self.update_predefined_sensor(SensorLibrary.BATTERY__PERCENTAGE, batt)
        elif xdata_id == 0x07 and xdata_size == 2:
            pressure = unpack("<H", xdata)[0]
            self.update_predefined_sensor(SensorLibrary.PRESSURE__MBAR, pressure / 10)
        elif xdata_id == 0x08 and xdata_size == 4:
            (motion, illuminance_1, illuminance_2) = unpack("<BHB", xdata)
            self.update_predefined_binary_sensor(
                BinarySensorDeviceClass.MOTION, bool(motion)
            )
            self.update_predefined_sensor(
                SensorLibrary.LIGHT__LIGHT_LUX, illuminance_1 + illuminance_2
            )
        elif xdata_id == 0x09 and xdata_size == 4:
            illuminance = unpack("<I", xdata)[0]
            self.update_predefined_sensor(SensorLibrary.LIGHT__LIGHT_LUX, illuminance)
        elif xdata_id == 0x11 and xdata_size == 1:
            light = unpack("B", xdata)[0]
            self.update_predefined_binary_sensor(
                BinarySensorDeviceClass.LIGHT, bool(light)
            )
        elif xdata_id == 0x12 and xdata_size == 4:
            (pm2_5, pm10) = unpack("<HH", xdata)
            self.update_predefined_sensor(
                SensorLibrary.PM25__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, pm2_5
            )
            self.update_predefined_sensor(
                SensorLibrary.PM10__CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, pm10
            )
        elif xdata_id == 0x13 and xdata_size == 2:
            co2 = unpack("<H", xdata)[0]  # noqa: F841
            self.update_predefined_sensor(
                SensorLibrary.CO2__CONCENTRATION_PARTS_PER_MILLION, co2
            )
        elif xdata_id == 0x0F and xdata_size == 1:
            pass
            # packet_id = unpack("B", xdata)[0]  # noqa: F841
            # result.update({"packet": packet_id})
        else:
            _LOGGER.debug(
                "Unknown data received from Qingping device: %s",
                xdata.hex(),
            )
