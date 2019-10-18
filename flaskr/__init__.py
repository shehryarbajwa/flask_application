from flask import Flask, jsonify, render_template, request, Response, redirect
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, template_folder='pages')
    CORS(app)


    @app.route('/shehryar')
    def index():
        return jsonify([{"city": "Lahore",
        "state": "Punjab",
        "venues": [{
            "id": 1,
            "name": "The Musical Hop",
            "num_upcoming_shows": 0},
            {
                "id": 2,
                "name": "Park Square Live Music",
                "num_upcoming_shows": 1
            }]
        }])

    @app.route('/api')
    def api_route():
        return render_template('index.html')

    return app