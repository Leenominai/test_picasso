import os
from dotenv import load_dotenv

load_dotenv()


DATABASES = {
    "test": {
        "ENGINE": os.getenv("TEST_DB_ENGINE", default="django.db.backends.postgresql"),
        "NAME": os.getenv("TEST_POSTGRES_DB", default="test_postgres"),
        "USER": os.getenv("TEST_POSTGRES_USER", default="test_postgres"),
        "PASSWORD": os.getenv("TEST_POSTGRES_PASSWORD", default="test_postgres"),
        "HOST": os.getenv("DB_HOST", default="db"),
        "PORT": os.getenv("DB_PORT", default="5432"),
    }
}