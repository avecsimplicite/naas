Client-only approach — use only your browser

This folder contains a single static HTML page (`index.html`) that:

- Fetches the published Google Sheets CSV (the sheet must be "Published to the web" or reachable with CORS).
- Renders the sheet as an HTML table in the browser.
- Uses `html2canvas` to convert the rendered table into a PNG and triggers a download.

Usage

1. Serve the folder with a local static server (recommended) to avoid file:// fetch restrictions:

```bash
cd o_static
python -m http.server 8000
# Then open http://localhost:8000 in your browser
```

2. Paste your sheet's "Publish to web" URL into the input, click "Load & Render Table", then click "Download PNG".

Notes and caveats

- Cross-origin limitations: If the sheet isn't published to the web or the server blocks CORS, `fetch` will fail in the browser. Options:
  - Publish the sheet to the web (File → Publish to web) and use the published URL.
  - Use a simple CORS proxy (not recommended for sensitive data) such as `https://api.allorigins.win/raw?url=` or set up your own proxy.
  - Run the static page via a local HTTP server rather than opening the file directly, which avoids some browser restrictions.

Proxy usage notes

- The page includes a "Use CORS proxy" toggle and a proxy base input. When enabled the CSV URL will be requested via `proxyBase + encodeURIComponent(csvUrl)`. Example proxy bases you can try:
  - `https://api.allorigins.win/raw?url=` (public, free)
  - `https://cors.bridged.cc/` (public proxy — may require registration)

- Security: do NOT use a public proxy for private or sensitive sheet data. A better option is to run your own small proxy (for example a single Heroku/Render/Cloud Run function) that fetches the sheet server-side and returns it with permissive CORS headers.

- This is fully client-side — no Python, no server required.

No-server (open file directly) mode

- If you want to open `index.html` directly from your file manager (file:///) without running any server, use the "Load via script (no server required)" checkbox in the UI. This uses the Google gviz JSON loader which runs as a script tag and avoids CORS restrictions that block `fetch` from file://.
- Limitations: the gviz loader requires that the sheet is at least viewable publicly (published or shared). If you paste a URL that doesn't include the spreadsheet id (for example certain publish-to-web formats), the script loader may not extract the id automatically — in that case copy the edit URL containing `/d/{spreadsheetId}/`.

Embedding (iframe)

- I added `embed.html` which is designed to be embedded via an `<iframe>` from any website. It accepts these query parameters:
  - `url` (required): the spreadsheet URL (preferably the edit or publish URL containing the spreadsheet id). Must be URL-encoded.
  - `padding` (optional): number of pixels of white padding to add around the table in the PNG (default 8).
  - `close=1` (optional): the embed page posts a message to the parent after download so the host page can react.

- Example iframe snippet:

```html
<iframe src="https://example.com/path/to/o_static/embed.html?url=https%3A%2F%2Fdocs.google.com%2Fspreadsheets%2Fd%2F<SPREADSHEET_ID>%2Fedit%23gid%3D665461249&padding=8&close=1"
        width="900" height="600" style="border:0"
        sandbox="allow-scripts allow-downloads allow-same-origin">
  Loading…
</iframe>
```

- Notes & caveats:
  - If your host page sets restrictive Content Security Policy (CSP) or you serve `embed.html` with headers that prevent framing (e.g., `X-Frame-Options: DENY`), the iframe will be blocked. Ensure the server serving `embed.html` allows framing.
  - The `sandbox` attribute above tightens security but allows scripts and downloads; adjust as needed. If you omit `sandbox`, downloads should still work if the browser allows it.
  - If the embed is cross-origin and you rely on the gviz/script loader, it still works because the script is loaded from Google; however, some corporate networks may block access.
  - The `close=1` param causes a postMessage to the parent telling it the download completed; host pages can listen for that message to hide the iframe or show a confirmation.


Security

- Don't paste private sheet URLs unless you trust the local machine/browser.
- If you deploy this page publicly, ensure you don't expose private data.
