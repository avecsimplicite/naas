from flask import Flask, send_file, render_template, request, redirect, url_for
from capture import capture_sheet_table, URL_DEFAULT
import os

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html", default_url=URL_DEFAULT)


@app.route("/generate")
def generate():
    # Allow overriding URL via query param for flexibility
    url = request.args.get("url") or URL_DEFAULT
    output_dir = os.path.join(os.getcwd(), "generated")
    os.makedirs(output_dir, exist_ok=True)

    # Capture and return file as attachment
    output_file = capture_sheet_table(url=url, table_only=True, output_dir=output_dir)

    return send_file(output_file, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
