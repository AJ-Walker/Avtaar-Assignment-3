from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:system@localhost:3306/avtaar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if not data:
        return jsonify({'message': 'No input data provided'}), 400
    if not data.get('name') or not data.get('gender') or not data.get('email'):
        return jsonify({'message': 'Some Data Not Provided.'}), 400

    name = data['name']
    gender = data['gender']
    email = data['email']
    # print(name, gender, email)

    try:
        user = models.User(name=name, gender=gender, email=email)
        db.session.add(user)
        db.session.commit()
        output = {"message": f"User {name} is successfully created"}
        return jsonify(output)
    except Exception as err:
        return jsonify({"Error": f"{err.orig.args[1]}"}), 400

@app.route('/api/event', methods=['POST'])
def create_event():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'No input data provided'}), 400
    if not data.get('uid') or not data.get('name') or not data.get('occurrence') or not data.get('startDate'):
        return jsonify({'message': 'Some Data Not Provided'}), 400

    uid = data['uid']
    name = data['name']
    occurrence = data['occurrence']
    start_date = data['startDate']
    start_date = datetime.strptime(start_date, '%d-%m-%Y').strftime('%Y-%m-%d')

    if data.get('endDate'):
        end_date = data['endDate']
        end_date = datetime.strptime(end_date, '%d-%m-%Y').strftime('%Y-%m-%d')
    else:
        end_date = None
    # print(uid, name, occurrence, start_date, end_date)

    try:
        event = models.Events(uid=uid, name=name, occurrence=occurrence, startDate=start_date, endDate=end_date)
        db.session.add(event)
        db.session.commit()
        output = {"message": f"Event {name} is successfully created"}
        return jsonify(output)
    except Exception as err:
        return jsonify({"Error": f"{err.orig.args[1]}"}), 400


if __name__ == '__main__':
    app.run(debug=True)