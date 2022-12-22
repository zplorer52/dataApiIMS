from flask import Flask

from flask_restful import Api

from api.resources.pulp2 import PULP2
from api.resources.apm3 import APM3
from api.resources.pm12 import PM12
from api.resources.nps import NPS
from api.resources.pb5a import PB5A
from api.resources.hello import HelloWorld

from api.resources.area import AREA

HOST = '0.0.0.0'
PORT = 5000
DEBUG = True


app = Flask(__name__)
## Undefined routes will throw 404, Not found error by 'catch_all_404s'
api = Api(app, catch_all_404s=True)


# Api descriptions
api.add_resource(HelloWorld, '/', '/hello')

## Common Routes
api.add_resource(PULP2, '/pulp2', '/pulp2')
api.add_resource(APM3, '/apm3', '/apm3')
api.add_resource(PM12, '/pm12', '/pm12')
api.add_resource(NPS, '/nps', '/nps')
api.add_resource(PB5A, '/pb5a', '/pb5a')

## Based on section defined in .conf
api.add_resource(AREA, '/area', '/area')


if __name__ == '__main__':
    app.run(host=HOST,port=PORT, debug=DEBUG)
