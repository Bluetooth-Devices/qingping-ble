from bluetooth_sensor_state_data import BluetoothServiceInfo, DeviceClass, SensorUpdate
from sensor_state_data import (
    DeviceKey,
    SensorDescription,
    SensorDeviceInfo,
    SensorValue,
    Units,
)

from qingping_ble.parser import QingpingBluetoothDeviceData


def test_can_create():
    QingpingBluetoothDeviceData()


# No support for motion sensor yet
# data = b"0X\x83\n\x02\xcd\xd5`4-X\x08"
# data = b"0X\x83\n\x02\xcd\xd5`4-X\x08"
# data = b"H\x12\xcd\xd5`4-X\x08\x04\x00-\x01\x00\x0f\x01\x8e"
# data = b"H\x12\xcd\xd5`4-X\x08\x04\x00-\x01\x00\x0f\x01\x8e"
# data = b"H\x12\xcd\xd5`4-X\x08\x04\x01-\x01\x00\x0f\x01\xb7"


def test_motion_and_light_signal_only():
    parser = QingpingBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="Qingping Motion & Light",
        manufacturer_data={},
        service_uuids=[],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        service_data={
            "0000fdcd-0000-1000-8000-00805f9b34fb": b"H\x12"
            b"\xcd\xd5`4-X\x08\x04\x00\r\x00\x00\x0f\x01\xee"
        },
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="Qingping Motion & Light EEFF",
                model="CGPR1",
                manufacturer="Qingping",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            )
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
                native_value=-60,
            )
        },
    )


def test_motion_and_light_battery_update():
    parser = QingpingBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="Qingping Motion & Light",
        manufacturer_data={},
        service_uuids=[],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        service_data={
            "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x08\x12"
            b"\xcd\xd5`4-X\x02\x01d\x0f\x01\x98\t\x04<\x01\x00\x00"
        },
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="Qingping Motion & Light EEFF",
                model="CGPR1",
                manufacturer="Qingping",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=DeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=DeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
                native_value=-60,
            ),
        },
    )
