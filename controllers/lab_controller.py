from flask import Blueprint, redirect
from services.guacamole_service import get_guacamole_token
from datetime import datetime
import os

lab = Blueprint("lab", __name__)

# Pastikan folder logs ada
if not os.path.exists("logs"):
    os.makedirs("logs")

def simpan_log(aksi):
    with open("logs/aktivitas.log", "a") as f:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{waktu} - {aksi}\n")

from flask import Blueprint, render_template

lab = Blueprint("lab", __name__)

@lab.route("/lab/ddos")
def ddos_design():
    return render_template("lab/ddos.html")
