# Notice

The component and platforms in this repository are not meant to be used by a
user, but as a "myfitnesspal" that custom component developers can build
upon, to make more awesome stuff.

This myfitnesspal uses ['sampleclient'](https://github.com/ludeeus/sampleclient) to simulate what you actually might use in your integration.

HAVE FUN! 😎

## Why?

This is simple, by having custom_components look (README + structure) the same
it is easier for developers to help each other and for users to start using them.

If you are a developer and you want to add things to this "myfitnesspal" that you think more
developers will have use for, please open a PR to add it :)

## What?

This repository contains multiple files, here is a overview:

File | Purpose
-- | --
`.devcontainer/*` | Used for development/testing with VSCODE, more info in the readme file in that dir.
`.github/ISSUE_TEMPLATE/feature_request.md` | Template for Feature Requests
`.github/ISSUE_TEMPLATE/issue.md` | Template for issues
`.github/settings.yml` | Probot settings to control the repository settings.
`.vscode/taks.json` | Tasks for the devcontainer.
`custom_components/myfitnesspal/.translations/*` | [Translation files.](https://developers.home-assistant.io/docs/en/next/internationalization_custom_component_localization.html#translation-strings)
`custom_components/myfitnesspal/__init__.py` | The component file for the integration.
`custom_components/myfitnesspal/config_flow.py` | Config flow file, this adds the UI configuration possibilities.
`custom_components/myfitnesspal/const.py` | A file to hold shared variables/constants for the entire integration.
`custom_components/myfitnesspal/manifest.json` | A [manifest file](https://developers.home-assistant.io/docs/en/creating_integration_manifest.html) for Home Assistant.
`custom_components/myfitnesspal/sensor.py` | Sensor platform for the integration.
`CONTRIBUTING.md` | Guidelines on how to contribute.
`example.png` | Screenshot that demonstrate how it might look in the UI.
`info.md` | An example on a info file (used by [hacs][hacs]).
`LICENSE` | The license file for the project.
`README.md` | The file you are reading now, should contain info about the integration, installation and configuration instructions.
`requirements.txt` | Python packages used by this integration.

***
README content if this was a published component:
***

# myfitnesspal

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE.md)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

_Component to integrate with [myfitnesspal][myfitnesspal]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show info from myfitnesspal API.

![example][exampleimg]

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `myfitnesspal`.
4. Download _all_ the files from the `custom_components/myfitnesspal/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. Choose:
   - Add `myfitnesspal:` to your HA configuration.
   - In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Myfitnesspal"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/myfitnesspal/.translations/en.json
custom_components/myfitnesspal/.translations/nb.json
custom_components/myfitnesspal/.translations/sensor.nb.json
custom_components/myfitnesspal/__init__.py
custom_components/myfitnesspal/config_flow.py
custom_components/myfitnesspal/const.py
custom_components/myfitnesspal/manifest.json
custom_components/myfitnesspal/sensor.py
```

## Example configuration.yaml

```yaml
myfitnesspal:
  username: my_username
  password: my_password
  sensor:
    - enabled: true
      name: My custom name
```

## Configuration options

Key | Type | Required | Description
-- | -- | -- | --
`username` | `string` | `False` | Username for the client.
`password` | `string` | `False` | Password for the client.
`sensor` | `list` | `False` | Configuration for the `sensor` platform.

### Configuration options for `sensor` list

Key | Type | Required | Default | Description
-- | -- | -- | -- | --
`enabled` | `boolean` | `False` | `True` | Boolean to enable/disable the platform.
`name` | `string` | `False` | `myfitnesspal` | Custom name for the entity.

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[myfitnesspal]: https://github.com/custom-components/myfitnesspal
[buymecoffee]: https://www.buymeacoffee.com/ludeeus
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/custom-components/myfitnesspal.svg?style=for-the-badge
[commits]: https://github.com/custom-components/myfitnesspal/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/custom-components/myfitnesspal.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Joakim%20Sørensen%20%40ludeeus-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/custom-components/myfitnesspal.svg?style=for-the-badge
[releases]: https://github.com/custom-components/myfitnesspal/releases
