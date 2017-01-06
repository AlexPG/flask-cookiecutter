import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my super secret key!!!'
    PER_PAGE = 5

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    {% if cookiecutter.postgresql=='y' %}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'postgresql:///data_dev'
    {% else %}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 
                                            'data-dev.sqlite')
    {% endif %}

    {% if cookiecutter.rest_framework == 'y' %}
    # Flask-Restplus settings
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False
    {% endif %}

class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SERVER_NAME = 'localhost:5000'
    {% if cookiecutter.postgresql=='y' %}
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'postgresql:///data_test'
    {% else %}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 
                                            'data-test.sqlite')
    {% endif %}

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}
