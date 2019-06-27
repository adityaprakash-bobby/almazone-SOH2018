import os


class Config:
    GOOGLEMAPS_KEY = 'AIzaSyCHpqu7GB3ZxaVbjFd1W-jSzH75XJQuyP8'
    SECRET_KEY = 'secretkey'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:root@localhost/new_db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
