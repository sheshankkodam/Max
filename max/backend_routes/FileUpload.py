from flask_restful import Resource, reqparse
from flask import request
from werkzeug.utils import secure_filename
from os.path import join


class FileUpload(Resource):
    def __init__(self):
        self.__HEADERS = {'Cache-Control': 'private, max-age=0, no-cache', 'Content-type': 'application/json'}

    def post(self):
        parser = reqparse.RequestParser()
        args = parser.parse_args()
        f = request.files['file']
        f.save(join('/Users/sheshank.kodam/Desktop', secure_filename(f.filename)))
        return 'file uploaded successfully'

