import httplib
from time import time
from flask_restful import Resource
from flask_restful_swagger import swagger

from max.logs import create_logger
log = create_logger(__name__)

SERVER_START_TIME = int(round(time() * 1000))


class AppStatus(Resource):
    def __init__(self):
        self.__HEADERS = {'Cache-Control': 'private, max-age=0, no-cache', 'Content-type': 'application/json'}

    @swagger.operation(
        notes="Get status",
        nickname="get_status",
        responseMessages=[
            {
                "code": 404,
                "message": {
                    "status": "Soup App is Down"
                }
            }
        ]
    )
    def get(self):
        uptime = int(round(time() * 1000)) - SERVER_START_TIME
        successful_json = {"app": "max", "status": "Up and Listening", "uptime": uptime}
        log.info("status=heartbeat, app=max, message=Up and Listening, uptime=%d", uptime)
        return successful_json, httplib.OK, self.__HEADERS
