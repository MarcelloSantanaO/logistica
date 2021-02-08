from flask_restful import Resource, fields, marshal_with
from flask import request
from dao.estimate_freight import Pricing


class EstimateResource(Resource):
    fields = {
        'Code': fields.String,
        'Value': fields.String,
        'Time': fields.String
    }
    @marshal_with(fields)
    def post(self):
        data = request.json
        list_dict = Pricing().estimate_correios(**data)
        return list_dict,200
