from resources.base_resource import BaseResource
from flask_restful import fields, marshal_with
from dao.logistic_dao import LogisticDao
from model.logistics import Logistic


class LogisticResource(BaseResource):
    fields = {
        'id_': fields.Integer,
        'name': fields.String,
        'description': fields.String
    }

    def __init__(self) -> None:
        self.__dao = LogisticDao()
        self.__model_type = Logistic 
        super().__init__(self.__dao,self.__model_type)

    @marshal_with(fields)
    def get(self, id = None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self):
        return super().put()

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)
