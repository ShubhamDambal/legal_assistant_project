# backend/config.py

import os

# Get the absolute path to the directory containing this file
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'legal_assistant.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
