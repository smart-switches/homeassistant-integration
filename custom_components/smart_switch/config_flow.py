"""Config flow for Smart Switches integration."""

from __future__ import annotations

import logging
from typing import Any

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class SmartSwitchConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Smart Switches."""

    # Config entry schema version. Increment when changing the data structure.
    # Used by Home Assistant to migrate old config entries to new formats.
    VERSION = 1

    async def async_step_user(
        self,
        user_input: dict[str, Any] | None = None,
    ) -> FlowResult:
        """Handle the initial step."""
        # Only allow a single config entry
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            # Create the config entry
            return self.async_create_entry(
                title="Smart Switches",
                data={},
            )

        # Show a simple confirmation form
        return self.async_show_form(step_id="user")
