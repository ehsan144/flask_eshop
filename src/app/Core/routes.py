from flask_restful import Resource


class CoreResource(Resource):
    def get(self):
        return {"hello": "world"}
