"""The Smart Switches integration."""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "smart_switch"


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Smart Switches from a config entry."""
    # Store entry data if needed (currently empty)
    hass.data.setdefault(DOMAIN, {})

    # Integration is set up and ready
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # Clean up if needed
    return True
