from enum import Enum


class FlaskEnv(Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"
    TESTING = "testing"
