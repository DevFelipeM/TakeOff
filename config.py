import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'sua-chave-secreta-aqui'  
    JWT_SECRET_KEY = 'sua-chave-secreta-jwt'  
    JWT_ACCESS_TOKEN_EXPIRES = 3600