from flask_restful import Resource
from flask import jsonify
from api.config.configuration import *
from api.common.util import MysqlData

class PM12(Resource):
    def __init__(self):
        self.cred = read_cred(area="pm12")

    def get(self):
        # print(self.cred)
        data = None
        if self.cred:
            db = MysqlData(self.cred)
            result = db.getdata()
            if result:
                data = jsonify(result)
        if not data:
            abort(400, "No data")

        return data
    

    def post(self):
        raise NotImplementedError()

    def __del__(self):
        print("PM12 resource de-allocated")