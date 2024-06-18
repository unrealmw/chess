import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # BABEL_DEFAULT_LOCALE = 'ru'
    # BABEL_SUPPORTED_LOCALES = ['en', 'ru']
    # BABEL_TRANSLATION_DIRECTORIES = 'translations'

