class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://Nutzername:Password@localhost/Databasename"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'our-secret-key'
    JWT_ERROR_MESSAGE_KEY = 'message'