import io
import os

from flask import Flask, send_file
from openpyxl import load_workbook  # type: ignore

app = Flask(__name__)


@app.route("/download_xlsx")
def download_xlsx():
    return


if __name__ == "__main__":
    app.run(debug=True)
