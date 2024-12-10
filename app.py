import io
import os

from flask import Flask, send_file
from openpyxl import load_workbook  # type: ignore

app = Flask(__name__)


@app.route("/download_xlsx")
def download_xlsx():
    excel_path = os.path.join(app.root_path, "excel_files", "target.xlsx")
    workbook = load_workbook(excel_path)

    worksheet = workbook["Sheet1"]
    worksheet["A1"] = "a"
    worksheet["B1"] = "b"
    worksheet["C1"] = "c"

    output = io.BytesIO()
    workbook.save(output)
    output.seek(0)

    return send_file()


if __name__ == "__main__":
    app.run(debug=True)
