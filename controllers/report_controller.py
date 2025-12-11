from flask import Blueprint, render_template

report = Blueprint("report", __name__)

@report.route("/report")
def tampil_report():
    logs = []
    try:
        with open("logs/aktivitas.log", "r") as f:
            for baris in f:
                waktu, aksi = baris.strip().split(" - ")
                logs.append({
                    "waktu": waktu,
                    "aksi": aksi
                })
    except:
        pass

    return render_template("report/hasil.html", logs=logs)
