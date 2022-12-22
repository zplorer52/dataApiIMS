from flask_restful import Resource, reqparse
from flask import jsonify, abort
from api.config.configuration import *
from api.common.util import OracleData
from api.common.util import MysqlData


class AREA(Resource):
    def __init__(self):
        # Parsing arguments from '/area?name=pulp2'
        parser = reqparse.RequestParser()
        # https://flask-restful.readthedocs.io/en/latest/reqparse.html#required-arguments
        # Argument Locations [ args,form,headers, cookies]
        parser.add_argument('name', type=str, location='args')

        area_name = parser.parse_args()
        # print(area_name['name'])        

        self.query = area_name['name']
        self.cred = read_cred(area=area_name['name'])        

    def get(self):
        data = None
        if self.cred:
            # ORACLE
            if self.cred['dbtype'] == "oracle":
                db = OracleData(self.cred)
            # MYSQL
            if self.cred['dbtype'] == "mysql":
                db = MysqlData(self.cred)
            
            result = db.getdata()
            if result:
                data = jsonify(result)
        if not data:
            abort(400, f"No data, for the query '{self.query}'")
            
        return data

    def post(self):
        raise NotImplementedError()
