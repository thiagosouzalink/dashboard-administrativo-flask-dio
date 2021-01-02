import os

class Config():
    CSRF_ENABLE = True
    SECRET = "859112cddee2a5df6cafc733655fe516"
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None


class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = "localhost"
    PORT_HOST = 8080
    URL_MAIN = f'http://{IP_HOST}:{PORT_HOST}/' # http://localhost/8080
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/dashboard_aula"


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = "192.0.0.1"
    PORT_HOST = 8080
    URL_MAIN = f"http://{IP_HOST}/{PORT_HOST}" # http://localhost/8080
    SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost/dashboard_aula"


app_config = {
    'development': DevelopmentConfig()
}

app_active = os.getenv("FLASK_ENV") # Obtém variável de ambiente
if app_active is None:
    app_active = "development"
