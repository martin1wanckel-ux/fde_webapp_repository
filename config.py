import os
from dataclasses import dataclass

ALLOWED_ENVIRONMENTS = ["development", "staging", "production"]
ALLOWED_ENVIRONMENTS_SET = frozenset(ALLOWED_ENVIRONMENTS)
@dataclass

class Config:
    """ This class is used to store configuration values for the application. It includes validation for the app_env and port attributes. """
    port: int
    app_env: str
    log_level: str
    def __post_init__(self):
        if self.app_env not in ALLOWED_ENVIRONMENTS:
            raise ValueError(f"Invalid app_env: {self.app_env}. Must be one of {ALLOWED_ENVIRONMENTS}.")
        if not isinstance(self.port, int):
            raise TypeError("Port attribute of Class instance must be an integer")
        elif self.port < 0:
            raise ValueError("Port attribute of Class instance must be non-negative integers")
    @classmethod
    def from_env(cls)-> "Config":
        # this function reads the environment variables and returns a Config instance. If checks whether Port value is an integer and raises a ValueError if not. It also checks whether the app_env value is valid and raises a ValueError if not (From None such that only this error is directly displayed).
        raw_port = os.environ.get("PORT", "8000") # Get port or default value, int(str)
        try:
            port = int(raw_port)
        except ValueError:
            raise ValueError(f"Invalid PORT value: {raw_port}. Must be an integer.") from None
        return cls(
            port = port, 
            app_env = os.getenv("APP_ENV", "development"),
            log_level = os.getenv("LOG_LEVEL", "INFO"))

if __name__ == "__main__":
    config = Config.from_env()
    print(config.__doc__)
    print(config)