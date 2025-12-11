from flask import Flask,render_template
from config import Config

# Import semua controller (blueprint)
from controllers.dashboard_controller import dashboard
from controllers.lab_controller import lab
from controllers.report_controller import report

# Inisialisasi Flask
app = Flask(__name__)
app.config.from_object(Config)

# Registrasi semua route
app.register_blueprint(dashboard)
app.register_blueprint(lab)
app.register_blueprint(report)




# Jalankan server
if __name__ == "__main__":
    app.run(debug=True)
