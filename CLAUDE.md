# Home Assistant Integration

Custom HA integration for smart switch devices using **Bluetooth (BLE)**.

## Architecture

- [custom_components/smart_switch/\_\_init\_\_.py](custom_components/smart_switch/__init__.py) - Entry point
- [custom_components/smart_switch/config_flow.py](custom_components/smart_switch/config_flow.py) - Configuration UI
- [custom_components/smart_switch/coordinator.py](custom_components/smart_switch/coordinator.py) - BLE polling coordinator
- [custom_components/smart_switch/manifest.json](custom_components/smart_switch/manifest.json) - Metadata & version

## Development

```bash
make docker-build    # Build dev container
```

CI/CD automated via GitHub Actions (HACS validation, PR checks, versioning).

## Integration Notes

This handles **device management via Bluetooth** - separate from button press events which go via WiFi to the add-on.
Both channels can coexist for complementary functionality.
