from flask_restful import Resource, reqparse
from flask import request
from werkzeug.utils import secure_filename
from os.path import join
from os.path import join


class FileUpload(Resource):
    def __init__(self):
        self.__HEADERS = {'Cache-Control': 'private, max-age=0, no-cache', 'Content-type': 'application/json'}

    def get(self):
        return 'file uploaded successfully'

    def post(self):
        image_file = request.files['imageInput']
        image_file_name = secure_filename(image_file.filename)
        image_file.save(join('/Users/sheshank.kodam/Desktop/dev/personal_projects/Max', image_file_name))
        return 'file uploaded successfully1'

