from flask import Flask, jsonify, render_template, request, Response, redirect, abort
from .models import setup_db, Plant
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__, template_folder='pages')
    setup_db(app)
    CORS(app)


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response


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
                "name": "Gaddafi Stadium",
                "num_upcoming_shows": 1
            }]
        }])

    @app.route('/api')
    def api_route():
        return render_template('index.html')

    
    @app.route('/plants', methods=['GET','POST'])
    def get_plants():
        page = request.args.get('page', 1, type=int)
        print(page)
        start = (page - 1) * 10
        print(start)
        end = start + 5
        print(end)
        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]


        return jsonify({
            'success': True,
            'plants': formatted_plants[start:end],
            'total_plants': len(formatted_plants) 
        })
    
    @app.route('/plants/<int:plant_id>')
    def get_specific_plant(plant_id):
        plant = Plant.query.filter(Plant.id == plant_id).one_or_none()

        if plant is None:
            abort(404)

        else:

            return jsonify({
                'success': True,
                'plant': plant.format()
            })


    return app