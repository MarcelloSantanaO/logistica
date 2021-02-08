from flask import Flask
from flask_restful import Api
from resources.logistic_resource import LogisticResource

app = Flask(__name__)
api = Api(app)

api.add_resource(LogisticResource,"/logistic", endpoint = "logistics")
api.add_resource(LogisticResource,"/logistic/<int:id>", endpoint = "logistic")

app.run(debug = True)