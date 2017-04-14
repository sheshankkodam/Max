from flask import Flask

from frontend_routes import FRONTEND

app = Flask(__name__)
app.register_blueprint(FRONTEND)

API_BASE = "/api/"
API_VERSION = "v1/"


def run():
    app.run(debug=True)

if __name__ == '__main__':
        app.run()
