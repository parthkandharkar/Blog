import os


class Config:
    SECRET_KEY = '60d67a09bb1fd99350c6c0be3e1046f5'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'parthkandharkar@gmail.com'
    MAIL_PASSWORD = 'nwhb vkvb iumt zgzj'