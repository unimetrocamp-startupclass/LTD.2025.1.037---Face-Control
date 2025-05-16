import os
from werkzeug.utils import secure_filename
from datetime import datetime

class ImageHandler:
    def __init__(self, upload_dir='uploads'):
        self.upload_dir = upload_dir
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

    def save_image(self, image_file):
        filename = secure_filename(image_file.filename)
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        full_path = os.path.join(self.upload_dir, f"{timestamp}_{filename}")
        image_file.save(full_path)
        return full_path
