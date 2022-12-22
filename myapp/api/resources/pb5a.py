from flask_restful import Resource
from flask import jsonify
from api.config.configuration import *
from api.common.util import OracleData


class PB5A(Resource):
    def __init__(self):
        self.cred = read_cred(area="pb5a")

    def get(self):
        # cred = read_cred(area="pb5a")
        # print(cred)
        data = None
        if self.cred:
            db = OracleData(self.cred)
            result = db.getdata()
            if result:
                data = jsonify(result)
                
        if not data:
            abort(400, "No data")

        return data

    def post(self):
        raise NotImplementedError()
