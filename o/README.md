# Postes Mensuels - Web UI

This folder contains a small Flask app that generates a PNG screenshot of a public Google Sheets table and serves it for download.

Prerequisites
- Python 3.8+
- Install dependencies and Playwright browsers

Quick start

```bash
cd o
python -m pip install -r requirements.txt
# Install Playwright browsers (one-time)
python -m playwright install
# Run the web app
python app.py
```

Open http://127.0.0.1:5000 in your browser and click "Generate & Download PNG".

Notes
- This app is intentionally self-contained in `o/` so it doesn't change existing working files.
- The generated PNG files are written to `o/generated/`.
- If you want the same behavior as the original `postemensuels.py`, leave the default URL in the form.

Docker / Anywhere deployment

 - Build a Docker image (one-time):

```bash
cd o
docker build -t postes-mensuels:latest .
```

 - Run locally with Docker:

```bash
docker run --rm -p 5000:5000 postes-mensuels:latest
```

 - Or with docker-compose:

```bash
cd o
docker-compose up --build
```

 - Push to a container registry (Docker Hub / GitHub Container Registry) and deploy on any cloud (Render, Fly, Railway, etc.). Use the same image and run command.

Notes on Playwright:
 - The image uses the Playwright base image which already includes browsers. You don't need to run `playwright install` inside the container.
 - If you run locally without Docker, you'll still need to run `python -m playwright install` once.
