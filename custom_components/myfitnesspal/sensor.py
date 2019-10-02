"""Sensor platform for myfitnesspal."""
import logging

from homeassistant.helpers.entity import Entity

from .const import ATTRIBUTION, DEFAULT_NAME, DOMAIN, DOMAIN_DATA, ICON

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(
    hass, config, async_add_entities, discovery_info=None
):  # pylint: disable=unused-argument
    """Setup sensor platform."""
    async_add_entities([MyfitnesspalSensor(hass, discovery_info)], True)


async def async_setup_entry(hass, config_entry, async_add_devices):
    """Setup sensor platform."""
    async_add_devices([MyfitnesspalSensor(hass, {})], True)


class MyfitnesspalSensor(Entity):
    """myfitnesspal Sensor class."""

    def __init__(self, hass, config):
        self.hass = hass
        self.attr = {}
        self._state = None
        self._name = config.get("name", DEFAULT_NAME)

    async def async_update(self):
        """Update the sensor."""
        # Send update "signal" to the component
        await self.hass.data[DOMAIN_DATA]["client"].update_data()

        # Get new data (if any)
        updated = self.hass.data[DOMAIN_DATA]["data"].get("data", {})

        # Check the data and update the value.
        _LOGGER.error(updated)
        if 'calories' in updated:
            self._state = updated['calories']
            updated.pop('calories')
            self._attributes = updated
        elif updated == {}:
            self._state = 0

    @property
    def unique_id(self):
        """Return a unique ID to use for this sensor."""
        return (
            "0717a0cd-745c-48fd"
        )  # Don't had code this, use something from the device/service.

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": self.name,
            "manufacturer": "Myfitnesspal",
        }

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return self.attr
