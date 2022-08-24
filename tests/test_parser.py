import pytest
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


LIGHT_AND_MOTION = BluetoothServiceInfo(
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

MOTION_AND_LIGHT_ENSURE_SUPPORTED = BluetoothServiceInfo(
    name="Qingping Motion & Light",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"H\x12\xcd\xd5`4-X\x08\x04\x01\xe8\x00\x00\x0f\x01{"
    },
    source="local",
)


ALARM_CLOCK = BluetoothServiceInfo(
    name="Qingping Alarm Clock",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x08\x0c"
        b"4MV4-X\x01\x04 \x01\xb2\x01\x02\x01d"
    },
    source="local",
)


AIR_MONITOR = BluetoothServiceInfo(
    name="Qingping Air Monitor Lite",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x88\x0e\xd6\x88\x8f\xe6"
        b"HT\x01\x04\x03\x01\x16"
        b"\x02\x12\x04\x02\x00\x02\x00\x13\x02%\x02"
    },
    source="local",
)


CLOCK_LITE = BluetoothServiceInfo(
    name="Qingping BT Clock Lite",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x08\x1e\xf3&T4-X\x01\x046\x01\xcc\x01\x02\x01d"
    },
    source="local",
)

NO_VALID_DATA = BluetoothServiceInfo(
    name="Qingping Motion & Light",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        # No valid data yet
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"0X\x83\n\x02\xcd\xd5`4-X\x08"
    },
    source="local",
)


LEES_GUITARS = BluetoothServiceInfo(
    name="Lee Guitars Thermo-Hygrometer",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x8a\x0f\xd1,c4-X\x01\x04\x00\x01\x12\x02\x02\x01("
    },
    source="local",
)


LEES_GUITARS_PASSIVE = BluetoothServiceInfo(
    name="",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x8a\x0f\xd1,c4-X\x01\x04\x00\x01\x12\x02\x02\x01("
    },
    source="local",
)

LEES_GUITARS_PASSIVE_ADDR = BluetoothServiceInfo(
    name="aa:bb:cc:dd:ee:ff",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x8a\x0f\xd1,c4-X\x01\x04\x00\x01\x12\x02\x02\x01("
    },
    source="local",
)


def test_supported_motion_and_light():
    parser = QingpingBluetoothDeviceData()
    parser.supported(MOTION_AND_LIGHT_ENSURE_SUPPORTED) is True
    assert parser.title == "Motion & Light " "EEFF"


def test_supported_set_the_title():
    parser = QingpingBluetoothDeviceData()
    parser.supported(NO_VALID_DATA) is False
    parser.supported(LIGHT_AND_MOTION) is True
    assert parser.title == "Motion & Light " "EEFF"


def test_motion_and_light_signal_only():
    parser = QingpingBluetoothDeviceData()
    assert parser.update(LIGHT_AND_MOTION) == SensorUpdate(
        title="Motion & Light EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Motion & Light " "EEFF",
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
        title="Motion & Light EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Motion & Light " "EEFF",
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
        title="Motion & Light EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Motion & Light " "EEFF",
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


def test_alarm_clock():
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(ALARM_CLOCK)
    assert parsed == SensorUpdate(
        title="Alarm Clock EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Alarm Clock EEFF",
                model="CGD1",
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
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=43.4,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=28.8,
            ),
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_air_monitor():
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(AIR_MONITOR)
    assert parsed == SensorUpdate(
        title="Air Monitor Lite EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Air Monitor Lite EEFF",
                model="CGDN1",
                manufacturer="Qingping",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="pm25", device_id=None): SensorDescription(
                device_key=DeviceKey(key="pm25", device_id=None),
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement=Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="carbon_dioxide", device_id=None): SensorDescription(
                device_key=DeviceKey(key="carbon_dioxide", device_id=None),
                device_class=SensorDeviceClass.CO2,
                native_unit_of_measurement=Units.CONCENTRATION_PARTS_PER_MILLION,
            ),
            DeviceKey(key="pm10", device_id=None): SensorDescription(
                device_key=DeviceKey(key="pm10", device_id=None),
                device_class=SensorDeviceClass.PM10,
                native_unit_of_measurement=Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="pm25", device_id=None): SensorValue(
                device_key=DeviceKey(key="pm25", device_id=None),
                name="Pm25",
                native_value=2,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=25.9,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=53.4,
            ),
            DeviceKey(key="carbon_dioxide", device_id=None): SensorValue(
                device_key=DeviceKey(key="carbon_dioxide", device_id=None),
                name="Carbon " "Dioxide",
                native_value=549,
            ),
            DeviceKey(key="pm10", device_id=None): SensorValue(
                device_key=DeviceKey(key="pm10", device_id=None),
                name="Pm10",
                native_value=2,
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


def test_clock_lite():
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(CLOCK_LITE)
    assert parsed == SensorUpdate(
        title="BT Clock Lite EEFF",
        devices={
            None: SensorDeviceInfo(
                name="BT Clock Lite EEFF",
                model="CGC1",
                manufacturer="Qingping",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=31.0,
            ),
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=46.0,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


@pytest.mark.parametrize(
    "adv", [LEES_GUITARS_PASSIVE, LEES_GUITARS, LEES_GUITARS_PASSIVE_ADDR]
)
def test_lees_gutairs(adv):
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(adv)
    assert parsed == SensorUpdate(
        title="Lee Guitars Thermo-Hygrometer EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Lee Guitars " "Thermo-Hygrometer EEFF",
                model="CGM1",
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
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=40,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=25.6,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=53.0,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )
