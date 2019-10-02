"""
Component to integrate with myfitnesspal.

For more details about this component, please refer to
https://github.com/custom-components/myfitnesspal
"""
import logging
import os
from datetime import date, timedelta

import homeassistant.helpers.config_validation as cv
import myfitnesspal
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers import discovery
from homeassistant.util import Throttle
from integrationhelper.const import CC_STARTUP_VERSION

from .const import (CONF_ENABLED, CONF_NAME, CONF_PASSWORD, CONF_SENSOR,
                    CONF_USERNAME, DEFAULT_NAME, DOMAIN, DOMAIN_DATA,
                    ISSUE_URL, PLATFORMS, REQUIRED_FILES, VERSION)

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=30)

_LOGGER = logging.getLogger(__name__)

SENSOR_SCHEMA = vol.Schema(
    {
        vol.Optional(CONF_ENABLED, default=True): cv.boolean,
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
    }
)

CONFIG_SCHEMA = vol.Schema(
    {
        DOMAIN: vol.Schema(
            {
                vol.Optional(CONF_USERNAME): cv.string,
                vol.Optional(CONF_PASSWORD): cv.string,
                vol.Optional(CONF_SENSOR): vol.All(cv.ensure_list, [SENSOR_SCHEMA])
            }
        )
    },
    extra=vol.ALLOW_EXTRA,
)


async def async_setup(hass, config):
    """Set up this component using YAML."""
    if config.get(DOMAIN) is None:
        # We get her if the integration is set up using config flow
        return True

    # Print startup message
    _LOGGER.info(
        CC_STARTUP_VERSION.format(
            name=DOMAIN, version=VERSION, issue_link=ISSUE_URL)
    )

    # Check that all required files are present
    file_check = await check_files(hass)
    if not file_check:
        return False

    # Create DATA dict
    hass.data[DOMAIN_DATA] = {}

    # Get "global" configuration.
    username = config[DOMAIN].get(CONF_USERNAME)
    password = config[DOMAIN].get(CONF_PASSWORD)

    # Configure the client.
    client = myfitnesspal.Client(username, password)
    hass.data[DOMAIN_DATA]["client"] = MyfitnesspalData(hass, client)

    # Load platforms
    for platform in PLATFORMS:
        # Get platform specific configuration
        platform_config = config[DOMAIN].get(platform, {})

        # If platform is not enabled, skip.
        if not platform_config:
            continue

        for entry in platform_config:
            entry_config = entry

            # If entry is not enabled, skip.
            if not entry_config[CONF_ENABLED]:
                continue

            hass.async_create_task(
                discovery.async_load_platform(
                    hass, platform, DOMAIN, entry_config, config
                )
            )
    hass.async_create_task(
        hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_IMPORT}, data={}
        )
    )
    return True


async def async_setup_entry(hass, config_entry):
    """Set up this integration using UI."""
    conf = hass.data.get(DOMAIN_DATA)
    if config_entry.source == config_entries.SOURCE_IMPORT:
        if conf is None:
            hass.async_create_task(
                hass.config_entries.async_remove(config_entry.entry_id)
            )
        return False

    # Print startup message
    _LOGGER.info(
        CC_STARTUP_VERSION.format(
            name=DOMAIN, version=VERSION, issue_link=ISSUE_URL)
    )

    # Check that all required files are present
    file_check = await check_files(hass)
    if not file_check:
        return False

    # Create DATA dict
    hass.data[DOMAIN_DATA] = {}

    # Get "global" configuration.
    username = config_entry.data.get(CONF_USERNAME)
    password = config_entry.data.get(CONF_PASSWORD)

    # Configure the client.
    client = myfitnesspal.Client(username, password)
    hass.data[DOMAIN_DATA]["client"] = MyfitnesspalData(hass, client)

    # Add sensor
    hass.async_add_job(
        hass.config_entries.async_forward_entry_setup(config_entry, "sensor")
    )

    return True


class MyfitnesspalData:
    """This class handle communication and stores the data."""

    def __init__(self, hass, client):
        """Initialize the class."""
        self.hass = hass
        self.client = client

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def update_data(self):
        """Update data."""
        # This is where the main logic to update platform data goes.
        try:
            startdate = date.today()
            mfpday = await self.hass.async_add_executor_job(self.client.get_date(
                startdate.year,
                startdate.month,
                startdate.day
            ))
            _LOGGER.error(mfpday.totals)
            self.hass.data[DOMAIN_DATA]["data"] = mfpday.totals
        except Exception as error:  # pylint: disable=broad-except
            _LOGGER.error("Could not update data - %s", error)


async def check_files(hass):
    """Return bool that indicates if all files are present."""
    # Verify that the user downloaded all files.
    base = f"{hass.config.path()}/custom_components/{DOMAIN}/"
    missing = []
    for file in REQUIRED_FILES:
        fullpath = "{}{}".format(base, file)
        if not os.path.exists(fullpath):
            missing.append(file)

    if missing:
        _LOGGER.critical("The following files are missing: %s", str(missing))
        returnvalue = False
    else:
        returnvalue = True

    return returnvalue


async def async_remove_entry(hass, config_entry):
    """Handle removal of an entry."""

    try:
        await hass.config_entries.async_forward_entry_unload(config_entry, "sensor")
        _LOGGER.info(
            "Successfully removed sensor from the myfitnesspal integration")
    except ValueError:
        pass
