from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from config import ProductionConfig
import os

def create_app(config_class=ProductionConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Swagger UI configuration
    SWAGGER_URL = '/api/docs'
    API_URL = '/static/swagger.json'
    
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "API Documentation"
        }
    )
    
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    
    # Register your blueprints/routes here
    from routes import api
    app.register_blueprint(api)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
