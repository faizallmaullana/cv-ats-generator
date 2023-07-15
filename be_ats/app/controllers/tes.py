from flask import request, jsonify
from flask_restful import Resource
from app import db

from app.models.tes import tes

class Isi(Resource):
    def get(self):
        value = tes.query.all()
        result = []
        for a in value:
            result.append(a.name)
        return jsonify(name=result)
    
    def post(self):
        name = request.json.get('name', None)
        value = tes(
            name=name
        )
        db.session.add(value)
        db.session.commit()