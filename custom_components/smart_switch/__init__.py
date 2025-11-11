"""The Smart Switches integration."""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "smart_switch"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Smart Switches component."""
    # Integration is set up and ready
    return True
