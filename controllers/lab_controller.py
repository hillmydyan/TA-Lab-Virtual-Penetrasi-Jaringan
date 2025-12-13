from flask import Blueprint, render_template
from datetime import datetime
import os

lab = Blueprint("lab", __name__)

if not os.path.exists("logs"):
    os.makedirs("logs")

def simpan_log(aksi):
    with open("logs/aktivitas.log", "a") as f:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{waktu} - {aksi}\n")

# =========================
# LAB DDOS
# =========================
@lab.route("/lab/ddos")
def ddos_design():
    simpan_log("Akses LAB DDOS")
    return render_template("lab/ddos.html")

# =========================
# LAB SNIFFING
# =========================
@lab.route("/lab/sniffing")
def sniffing_design():
    simpan_log("Akses LAB Sniffing")
    return render_template("lab/sniffing.html")
