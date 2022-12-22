from flask_restful import Resource
from flask import jsonify
from api.config.configuration import *
from api.common.util import OracleData


class APM3(Resource):
    def __init__(self):
        self.cred = read_cred(area="apm3")
        # print(self.cred)

    def get(self):
        # cred = read_cred(area="apm3")
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

    def put(self):
        raise NotImplementedError()

    def patch(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()

    def __del__(self):
        print("apm3 resource de-allocated")
