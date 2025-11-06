"""The Smart Switches integration."""

from __future__ import annotations

import logging

from homeassistant.const import Platform
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.components import bluetooth
from homeassistant.exceptions import ConfigEntryNotReady

from .coordinator import (SmartSwitchConfigEntry, SmartSwitchDataUpdateCoordinator)
from .const import DOMAIN

_PLATFORMS: list[Platform] = [Platform.SENSOR]

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: SmartSwitchConfigEntry) -> bool:
    """Set up Smart Switches from a config entry."""

    assert entry.unique_id is not None
    
    entry.async_on_unload(entry.add_update_listener(_async_update_listener))
    await hass.config_entries.async_forward_entry_setups(
        entry, Platform.SENSOR,
    )

async def _async_update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Handle options update."""
    await hass.config_entries.async_reload(entry.entry_id)
