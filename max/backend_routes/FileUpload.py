from flask_restful import Resource, reqparse
from flask import request
from werkzeug.utils import secure_filename
from os.path import join, exists
import os


class FileUpload(Resource):
    def __init__(self):
        self.__HEADERS = {'Cache-Control': 'private, max-age=0, no-cache', 'Content-type': 'application/json'}

    def get(self):
        return 'file uploaded successfully'

    def post(self):
        output_directory = '/Users/sheshank.kodam/Desktop/dev/personal_projects/avatars'

        if not exists(output_directory):
            os.makedirs(output_directory)

        image_file = request.files['avatar']
        # first_name = request.files['firstName']
        # last_name = request.files['lastName']
        # dob = request.files['dateOfBirth']

        image_file_name = secure_filename(image_file.filename)
        image_file.save(join(output_directory, image_file_name))
        return 'file uploaded successfully1'

