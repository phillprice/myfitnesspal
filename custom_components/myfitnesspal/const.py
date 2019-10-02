"""Constants for myfitnesspal."""
# Base component constants
DOMAIN = "myfitnesspal"
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
ISSUE_URL = "https://github.com/phillprice/myfitnesspal/issues"
ATTRIBUTION = "Data from this is provided by myfitnesspal."

# Icons
ICON = "mdi:barley"

# Configuration
CONF_SENSOR = "sensor"
CONF_ENABLED = "enabled"
CONF_NAME = "name"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN
