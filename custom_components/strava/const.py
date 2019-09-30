"""Constants for strava."""
# Base component constants
DOMAIN = "strava"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
PLATFORMS = ["sensor"]
REQUIRED_FILES = [
    ".translations/en.json",
    "const.py",
    "config_flow.py",
    "manifest.json",
    "sensor.py"
]
ISSUE_URL = "https://github.com/custom-components/strava/issues"
ATTRIBUTION = "Data from this is provided by strava."

# Icons
ICON = "mdi:format-quote-close"

# Configuration
CONF_SENSOR = "sensor"
CONF_ENABLED = "enabled"
CONF_NAME = "name"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN
