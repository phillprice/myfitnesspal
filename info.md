[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE.md)

[![hacs][hacsbadge]](hacs)
![Project Maintenance][maintenance-shield]
[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

[![Discord][discord-shield]][discord]
[![Community Forum][forum-shield]][forum]

_Component to integrate with [strava][strava]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`sensor` | Show info from strava API.

![example][exampleimg]

{% if not installed %}
## Installation

1. Click install.
1. Add `strava:` to your HA configuration.

{% endif %}
## Example configuration.yaml

```yaml
strava:
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
`name` | `string` | `False` | `strava` | Custom name for the entity.


***

[strava]: https://github.com/custom-components/strava
[buymecoffee]: https://www.buymeacoffee.com/ludeeus
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
[commits-shield]: https://img.shields.io/github/commit-activity/y/custom-components/strava.svg?style=for-the-badge
[commits]: https://github.com/custom-components/strava/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[discord]: https://discord.gg/Qa5fW2R
[discord-shield]: https://img.shields.io/discord/330944238910963714.svg?style=for-the-badge
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/custom-components/strava.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Joakim%20Sørensen%20%40ludeeus-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/custom-components/strava.svg?style=for-the-badge
[releases]: https://github.com/custom-components/strava/releases
