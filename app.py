from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ergonomics.db'
db = SQLAlchemy(app)

# User Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

# Assessment Table
class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task_type = db.Column(db.String(100), nullable=False)
    force_required = db.Column(db.Float, nullable=False)
    posture_complexity = db.Column(db.Integer, nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    clearance_reach = db.Column(db.Float, nullable=False)
    computed_risk_score = db.Column(db.Float, nullable=False)
    recommended_action = db.Column(db.String(500))

@app.route('/')
def home():
    return jsonify({"message": "Ergonomic Assessment API Running!"})

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
