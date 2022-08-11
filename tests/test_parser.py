from bluetooth_sensor_state_data import BluetoothServiceInfo, SensorUpdate
from sensor_state_data import (
    BinarySensorDescription,
    BinarySensorDeviceClass,
    BinarySensorValue,
    DeviceKey,
    SensorDescription,
    SensorDeviceClass,
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
                name="Qingping Motion & Light " "EEFF",
                model="CGPR1",
                manufacturer="Qingping",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="illuminance", device_id=None): SensorDescription(
                device_key=DeviceKey(key="illuminance", device_id=None),
                device_class=SensorDeviceClass.ILLUMINANCE,
                native_unit_of_measurement=Units.LIGHT_LUX,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="illuminance", device_id=None): SensorValue(
                device_key=DeviceKey(key="illuminance", device_id=None),
                name="Illuminance",
                native_value=13,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
        },
        binary_entity_descriptions={
            DeviceKey(key="motion", device_id=None): BinarySensorDescription(
                device_key=DeviceKey(key="motion", device_id=None),
                device_class=BinarySensorDeviceClass.MOTION,
            )
        },
        binary_entity_values={
            DeviceKey(key="motion", device_id=None): BinarySensorValue(
                device_key=DeviceKey(key="motion", device_id=None),
                name="Motion",
                native_value=False,
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
                name="Qingping Motion & Light " "EEFF",
                model="CGPR1",
                manufacturer="Qingping",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="illuminance", device_id=None): SensorDescription(
                device_key=DeviceKey(key="illuminance", device_id=None),
                device_class=SensorDeviceClass.ILLUMINANCE,
                native_unit_of_measurement=Units.LIGHT_LUX,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
            DeviceKey(key="illuminance", device_id=None): SensorValue(
                device_key=DeviceKey(key="illuminance", device_id=None),
                name="Illuminance",
                native_value=316,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_has_motion():
    parser = QingpingBluetoothDeviceData()
    service_info = BluetoothServiceInfo(
        name="Qingping Motion & Light",
        manufacturer_data={},
        service_uuids=[],
        address="aa:bb:cc:dd:ee:ff",
        rssi=-60,
        service_data={
            "0000fdcd-0000-1000-8000-00805f9b34fb": b"H\x12"
            b"\xcd\xd5`4-X\x08\x04\x01-\x01\x00\x0f\x01\xb7"
        },
        source="local",
    )
    result = parser.update(service_info)
    assert result == SensorUpdate(
        title=None,
        devices={
            None: SensorDeviceInfo(
                name="Qingping Motion & Light " "EEFF",
                model="CGPR1",
                manufacturer="Qingping",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="illuminance", device_id=None): SensorDescription(
                device_key=DeviceKey(key="illuminance", device_id=None),
                device_class=SensorDeviceClass.ILLUMINANCE,
                native_unit_of_measurement=Units.LIGHT_LUX,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="illuminance", device_id=None): SensorValue(
                device_key=DeviceKey(key="illuminance", device_id=None),
                name="Illuminance",
                native_value=301,
            ),
        },
        binary_entity_descriptions={
            DeviceKey(key="motion", device_id=None): BinarySensorDescription(
                device_key=DeviceKey(key="motion", device_id=None),
                device_class=BinarySensorDeviceClass.MOTION,
            )
        },
        binary_entity_values={
            DeviceKey(key="motion", device_id=None): BinarySensorValue(
                device_key=DeviceKey(key="motion", device_id=None),
                name="Motion",
                native_value=True,
            )
        },
    )
