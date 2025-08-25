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

AIR_MONITOR_DEV_TYPE_36 = BluetoothServiceInfo(
    name="Qingping Air Monitor Lite",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x88$kM\xc9\x94"
        b"\xc2|\x01\x04\xfd\x00I"
        b"\x02\x12\x04\t\x00\t\x00\x13\x02a\x02"
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


QINGPING_DOOR_WINDOW = BluetoothServiceInfo(
    name="Qingping Door/Window Sensor",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\xc8\x04M:@4-X\x04\x01\x01\x0f\x01\xef"
    },
    source="local",
)


QINGPING_TEMP_RH_M = BluetoothServiceInfo(
    name="Qingping Temp RH M",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x08\x16\xa7%\x144-X\x01\x04\xd8\x00\xbb\x01\x02\x01d"
    },
    source="local",
)

QINGPING_TEMP_RH_PRO_E = BluetoothServiceInfo(
    name="Qingping Temp RH Pro E",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x08\x15\x01'@4-X\x01\x04\xde\x00\xe9\x01\x02\x01d"
    },
    source="local",
)


QINGPING_TEMP_RH_MONITOR_PRO = BluetoothServiceInfo(
    name="Qingping Temp & RH Monitor Pro",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x88\x18\x07\x22\x40\x34\x2d\x58\x01\x04\x18\x01\xcd"
        b"\x00\x02\x01\x61\x07\x02\x73\x27"
    },
    source="local",
)

QINGPING_CO2_TEMP_RH = BluetoothServiceInfo(
    name="Qingping CO2 Temp RH",
    manufacturer_data={},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": b"\x883ol\x824-X\x01\x04\xee\x00=\x01\x02\x01]"
        b"\x13\x02\x8f\x02"
    },
    source="local",
)

# Real data from user's CGP22C with firmware 1.3.8
QINGPING_CGP22C_REAL = BluetoothServiceInfo(
    name="Qingping CO2 Temp RH",
    manufacturer_data={},
    service_uuids=[],
    address="58:2D:34:86:1D:93",
    rssi=-75,
    service_data={
        "0000fdcd-0000-1000-8000-00805f9b34fb": (
            b"\n]\x93\x1d\x864-X\x01\x04\x17\x01\xce\x01\x02\x01d\x13\x02\xb3\x02"
        )
    },
    source="10:B4:1D:16:30:A2",
)


def test_supported_motion_and_light():
    parser = QingpingBluetoothDeviceData()
    parser.supported(MOTION_AND_LIGHT_ENSURE_SUPPORTED) is True
    assert parser.title == "Motion & Light EEFF"


def test_supported_set_the_title():
    parser = QingpingBluetoothDeviceData()
    parser.supported(NO_VALID_DATA) is False
    parser.supported(LIGHT_AND_MOTION) is True
    assert parser.title == "Motion & Light EEFF"


def test_motion_and_light_signal_only():
    parser = QingpingBluetoothDeviceData()
    assert parser.update(LIGHT_AND_MOTION) == SensorUpdate(
        title="Motion & Light EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Motion & Light EEFF",
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
                name="Signal Strength",
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


def test_motion_and_light_battery_update() -> None:
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
                name="Motion & Light EEFF",
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
                name="Signal Strength",
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
                name="Motion & Light EEFF",
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
                name="Signal Strength",
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
                name="Signal Strength",
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
                name="Carbon Dioxide",
                native_value=549,
            ),
            DeviceKey(key="pm10", device_id=None): SensorValue(
                device_key=DeviceKey(key="pm10", device_id=None),
                name="Pm10",
                native_value=2,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
                native_value=-60,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_air_monitor_dev_type_36():
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(AIR_MONITOR_DEV_TYPE_36)
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
            DeviceKey(key="pm25", device_id=None): SensorDescription(
                device_key=DeviceKey(key="pm25", device_id=None),
                device_class=SensorDeviceClass.PM25,
                native_unit_of_measurement=Units.CONCENTRATION_MICROGRAMS_PER_CUBIC_METER,
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
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=25.3,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=58.5,
            ),
            DeviceKey(key="carbon_dioxide", device_id=None): SensorValue(
                device_key=DeviceKey(key="carbon_dioxide", device_id=None),
                name="Carbon Dioxide",
                native_value=609,
            ),
            DeviceKey(key="pm25", device_id=None): SensorValue(
                device_key=DeviceKey(key="pm25", device_id=None),
                name="Pm25",
                native_value=9,
            ),
            DeviceKey(key="pm10", device_id=None): SensorValue(
                device_key=DeviceKey(key="pm10", device_id=None),
                name="Pm10",
                native_value=9,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
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
                name="Signal Strength",
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
                name="Lee Guitars Thermo-Hygrometer EEFF",
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
                name="Signal Strength",
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


def test_door_window():
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(QINGPING_DOOR_WINDOW)
    assert parsed == SensorUpdate(
        title="Door/Window Sensor EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Door/Window Sensor EEFF",
                model="CGH1",
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
            )
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
                native_value=-60,
            )
        },
        binary_entity_descriptions={
            DeviceKey(key="door", device_id=None): BinarySensorDescription(
                device_key=DeviceKey(key="door", device_id=None),
                device_class=BinarySensorDeviceClass.DOOR,
            ),
            DeviceKey(
                key=(None, "door_left_open"), device_id=None
            ): BinarySensorDescription(
                device_key=DeviceKey(key=(None, "door_left_open"), device_id=None),
                device_class=BinarySensorDeviceClass.PROBLEM,
            ),
        },
        binary_entity_values={
            DeviceKey(key="door", device_id=None): BinarySensorValue(
                device_key=DeviceKey(key="door", device_id=None),
                name="Door",
                native_value=False,
            ),
            DeviceKey(key=(None, "door_left_open"), device_id=None): BinarySensorValue(
                device_key=DeviceKey(key=(None, "door_left_open"), device_id=None),
                name="Door left open",
                native_value=False,
            ),
        },
        events={},
    )


def test_temp_rh_m():
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(QINGPING_TEMP_RH_M)
    assert parsed == SensorUpdate(
        title="Temp RH M EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Temp RH M EEFF",
                model="CGG1",
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
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
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
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=21.6,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=44.3,
            ),
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
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_temp_rh_pro_e():
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(QINGPING_TEMP_RH_PRO_E)
    assert parsed == SensorUpdate(
        title="Temp RH Pro E EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Temp RH Pro E EEFF",
                model="CGF1W",
                manufacturer="Qingping",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
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
        },
        entity_values={
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=48.9,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=22.2,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
                native_value=-60,
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


def test_temp_rh_monitor_pro():
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(QINGPING_TEMP_RH_MONITOR_PRO)
    assert parsed == SensorUpdate(
        title="Temp & RH Monitor Pro EEFF",
        devices={
            None: SensorDeviceInfo(
                name="Temp & RH Monitor Pro EEFF",
                model="CGP23W",
                manufacturer="Qingping",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
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
            DeviceKey(key="pressure", device_id=None): SensorDescription(
                device_key=DeviceKey(key="pressure", device_id=None),
                device_class=SensorDeviceClass.PRESSURE,
                native_unit_of_measurement=Units.PRESSURE_MBAR,
            ),
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
        },
        entity_values={
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=20.5,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=28.0,
            ),
            DeviceKey(key="pressure", device_id=None): SensorValue(
                device_key=DeviceKey(key="pressure", device_id=None),
                name="Pressure",
                native_value=1009.9,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
                native_value=-60,
            ),
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=97,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_co2_temp_rh():
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(QINGPING_CO2_TEMP_RH)
    assert parsed == SensorUpdate(
        title="CO2 Temp RH EEFF",
        devices={
            None: SensorDeviceInfo(
                name="CO2 Temp RH EEFF",
                model="CGP22C",
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
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="carbon_dioxide", device_id=None): SensorDescription(
                device_key=DeviceKey(key="carbon_dioxide", device_id=None),
                device_class=SensorDeviceClass.CO2,
                native_unit_of_measurement=Units.CONCENTRATION_PARTS_PER_MILLION,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=23.8,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=31.7,
            ),
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=93,
            ),
            DeviceKey(key="carbon_dioxide", device_id=None): SensorValue(
                device_key=DeviceKey(key="carbon_dioxide", device_id=None),
                name="Carbon Dioxide",
                native_value=655,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
                native_value=-60,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_cgp22c_real_data() -> None:
    """Test with real CGP22C data from user with firmware 1.3.8."""
    parser = QingpingBluetoothDeviceData()
    parsed = parser.update(QINGPING_CGP22C_REAL)
    assert parsed == SensorUpdate(
        title="CO2 Temp RH 1D93",
        devices={
            None: SensorDeviceInfo(
                name="CO2 Temp RH 1D93",
                model="CGP22C",
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
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="battery", device_id=None): SensorDescription(
                device_key=DeviceKey(key="battery", device_id=None),
                device_class=SensorDeviceClass.BATTERY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="carbon_dioxide", device_id=None): SensorDescription(
                device_key=DeviceKey(key="carbon_dioxide", device_id=None),
                device_class=SensorDeviceClass.CO2,
                native_unit_of_measurement=Units.CONCENTRATION_PARTS_PER_MILLION,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=27.9,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=46.2,
            ),
            DeviceKey(key="battery", device_id=None): SensorValue(
                device_key=DeviceKey(key="battery", device_id=None),
                name="Battery",
                native_value=100,
            ),
            DeviceKey(key="carbon_dioxide", device_id=None): SensorValue(
                device_key=DeviceKey(key="carbon_dioxide", device_id=None),
                name="Carbon Dioxide",
                native_value=691,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal Strength",
                native_value=-75,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )
