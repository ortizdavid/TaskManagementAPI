import os
import uuid
from flask import request

class FileUploader:

    IMGS_EXTENSIONS = {'.png', '.jpg', '.jpeg'}
    PDF_EXTENSIONS = {'.pdf'}
    errors = []

    def __init__(self):
        pass


    def get_file_extension(self, filename: str):
        return os.path.splitext(filename)[1]


    def upload_image(self, file_field_name: str, upload_dir: str):

        file = request.files[file_field_name]
        original_name = file.filename
        extension = self.get_file_extension(original_name)
        
        if file_field_name not in request.files:
            self.errors.append('No file part in the request')
            return None
        if original_name == '':
            self.errors.append('No file selected for uploading')
            return None
        if extension not in self.IMGS_EXTENSIONS:
            self.errors.append(f'Invalid extension.. Allowed images {self.IMGS_EXTENSIONS}')
            return None
        if len(self.errors) == 0:
            final_name = str(uuid.uuid4()) + extension
            file.save(os.path.join(upload_dir, final_name))
            return final_name