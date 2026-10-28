# OCI Cloud Commander Web

Browser preview of [OCI Cloud Commander Android](https://github.com/seki999/OCI_Cloud_Commander_Android). The current Android source has **30 playable levels across five chapters**. This preview loads the original JSON and localization files without inventing additional levels.

**Not yet fully ported:** Kotlin transaction engine, IAM/network/runtime predicates and full scoring. Unsupported objectives are marked unverified and cannot be claimed, rather than falsely granting completion. No real OCI connection, credentials or charges.

## Local start

```bash
python scripts/sync_content.py
npm install
npm run dev
```

GitHub Pages builds and deploys on push to main. Enable Settings → Pages → Source → GitHub Actions if needed.
