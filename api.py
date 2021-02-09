from flask import Flask
from flask_restful import Api
from resources.logistic_resource import LogisticResource
from resources.estimate_freight import EstimateResource


app = Flask(__name__)
api = Api(app)

api.add_resource(LogisticResource,"/logistic", endpoint = "logistics")
api.add_resource(LogisticResource,"/logistic/<int:id>", endpoint = "logistic")
api.add_resource(EstimateResource,"/pricing", endpoint= "Pricing")
app.run(debug = True)