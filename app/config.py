import os

class Config:
    SECRET_KEY = "dev-secret-7f3a9c"          # hardcoded signing key
    DEBUG = True
    DATABASE = os.environ.get("DATABASE", "shoplite.db")
    JWT_SECRET = "secret"
    AWS_ACCESS_KEY_ID = "AKIADEMOEXAMPLE00001"
    AWS_SECRET_ACCESS_KEY = "DEMO/wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    STRIPE_SECRET_KEY = "sk_test_DEMO_NOT_A_REAL_KEY"
    SESSION_COOKIE_SECURE = False
    CORS_ORIGINS = "*"
