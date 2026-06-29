# Social Reel Template — Café Athena

## Adobe Express Base Template

All recipe reels start from this template. Do not build from scratch.

**Template URL:** https://express.adobe.com/design/userTemplate/urn:aaid:sc:US:7fa31834-9bb7-583f-83e5-49ee4deb977e

Derived from the 06-07 Chicken and Dumplings production run (2026-06-22). First confirmed working reel.

---

## Specs

| Setting | Value |
|---------|-------|
| Format | Vertical (9:16) |
| Resolution | 720p |
| Duration | ~15 seconds |
| Platform | Facebook Reel, Instagram Reel |

---

## Production Workflow

1. **Voiceover** — ZONOS2 (primary) / Qwen3-TTS (backup). Seed 1847.
2. **Video clip** — Adobe Firefly, Kling 3.0 Omni, 720p, 9:16, 15s, seed 1847, 300 credits. Upload approved still as reference image.
3. **Assembly** — Open Adobe Express template (URL above). Import Firefly MP4 + final audio WAV. Sync, trim, export.
4. **UTM link** — Generate tracked URL before writing caption. Convention: `utm_source=[platform]&utm_medium=reel&utm_campaign=[recipe-slug]&utm_content=[folio-id]`
5. **Save** — Final MP4 to `Marketing/Marketing Content/Social/Recipes/[recipe-id]/` as `[recipe-id]-reel-v001.mp4`.

---

## Per-Recipe Notes

| Folio | Title | Template Used | Notes |
|-------|-------|--------------|-------|
| 06-07 | Chicken and Dumplings | Source (this template derived from it) | Facebook only, no UTM |
