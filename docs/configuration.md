# Custom configuration

Pass a JSON configuration with `--config`:

```bash
cleanfolder ~/Downloads --config config.example.json --preview
```

Extensions may include a leading dot and are normalized to lowercase. Unknown
extensions are placed in `fallback_category`.
