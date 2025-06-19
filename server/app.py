from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Movie

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact= False

CORS(app)
migrate = Migrate(app, db)

# Initialize the database
db.init_app(app)


@app.route('/movies', methods=['GET'])
def movies():
    if request.method == 'GET':
        movies = [m.to_dict() for m in Movie.query.all()]
        
        return make_response(jsonify(movies), 200)
    
    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    )





if __name__ == '__main__':
    app.run(port=5555)