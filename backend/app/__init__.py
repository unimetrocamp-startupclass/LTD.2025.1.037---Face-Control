from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads'

    from .routes import image_bp
    app.register_blueprint(image_bp)

    return app
