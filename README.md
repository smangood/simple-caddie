# Simple Caddie

Offline golf caddie web app. Open https://smangood.github.io/simple-caddie/ in Chrome on Android, then menu > Add to Home screen / Install app.
All data stays on the phone (localStorage); nothing is sent anywhere.

How the site is built: the GitHub Actions workflow in `.github/workflows/publish.yml` assembles `index.html`
(v2 parts in `src/` plus the v3 edit script in `src/v3/`, applied by `tools/apply_ed.py`), decodes the base64 icons
in `icons/`, checks everything against `checksums.sha256`, and publishes the result to the `gh-pages` branch.
When index.html changes, bump VERSION at the top of sw.js.
