from flask_restful import Resource
from flask import jsonify

DataLinks = [
    {
        "link":"/pulp2",
        "description": "DCS Pulp2 data from IMS"
    },
    {
        "link":"/apm3",
        "description": "DCS APM3 data from IMS"
    },
    {
        "link":"/nps",
        "description": "DCS NPS data from IMS"
    },
    {
        "link":"/pb5a",
        "description": "DCS PB5A data from IMS"
    },
    {
        "link":"/pm12",
        "description": "PM12 data"
    },
    {
        "link":"/area?name=nps",
        "description": "common link, arguments like apm3, pulp2, nps, pm12"
    }
]

class HelloWorld(Resource):
    def get(self):
        return jsonify(DataLinks)

    def post(self):
        raise NotImplementedError()
