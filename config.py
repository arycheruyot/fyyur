import os
from os import environ
from os import getenv

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL



DB_HOST = os.getenv('DB_HOST', '127.0.0.1:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '1994')
DB_NAME = os.getenv('DB_NAME', 'fyyur_db')

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)


SQLALCHEMY_TRACK_MODIFICATIONS = False