# Home Assistant Integration

Barebones Home Assistant custom integration for Smart Switches.

## Current Status

This integration has been stripped down to the **absolute minimum** required files:

- [custom_components/smart_switch/\_\_init\_\_.py](custom_components/smart_switch/__init__.py) - Minimal entry point (13 lines)
- [custom_components/smart_switch/manifest.json](custom_components/smart_switch/manifest.json) - Integration metadata

The integration currently does nothing except successfully load in Home Assistant. It serves as a placeholder for future functionality.

## Structure

```
custom_components/
└── smart_switch/
    ├── __init__.py       # Minimal setup function
    └── manifest.json     # Integration metadata (v0.1.0)
```

## Development

```bash
make docker-build    # Build dev container
```

CI/CD automated via GitHub Actions (HACS validation, PR checks, semantic versioning).

## Usage

Add to Home Assistant's `configuration.yaml`:

```yaml
smart_switch:
```

Then restart Home Assistant.

## Future Considerations

Originally planned for **Bluetooth (BLE) device management**, but current architecture uses WiFi for button events via the homeassistant-addon. This integration could be expanded in the future for device configuration, monitoring, or other complementary functionality.
