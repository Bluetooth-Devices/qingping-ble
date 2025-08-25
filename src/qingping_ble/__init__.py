"""Parser for Qingping BLE advertisements."""

from __future__ import annotations

from sensor_state_data import (
    BinarySensorDeviceClass,
    BinarySensorValue,
    DeviceKey,
    SensorDescription,
    SensorDeviceClass,
    SensorDeviceInfo,
    SensorUpdate,
    SensorValue,
    Units,
)

from .parser import QingpingBluetoothDeviceData

__version__ = "1.0.0"

__all__ = [
    "BinarySensorDeviceClass",
    "BinarySensorValue",
    "DeviceKey",
    "QingpingBluetoothDeviceData",
    "SensorDescription",
    "SensorDeviceClass",
    "SensorDeviceInfo",
    "SensorDeviceInfo",
    "SensorUpdate",
    "SensorValue",
    "Units",
]
