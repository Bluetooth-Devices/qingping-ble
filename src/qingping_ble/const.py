"""Constants for Qingping BLE advertisements."""

from sensor_state_data import BaseDeviceClass


class ExtendedSensorDeviceClass(BaseDeviceClass):
    """Device class for additional sensors (compared to sensor-state-data)."""

    # Sensirion-style VOC index (unitless, 1-500, relative to the sensor's
    # own recent baseline; not a concentration)
    VOC_INDEX = "voc_index"

    # Sound pressure in dB (exists in HA but not yet in sensor-state-data)
    SOUND_PRESSURE = "sound_pressure"
