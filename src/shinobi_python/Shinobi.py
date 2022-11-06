from dataclasses import dataclass


class Super:
    """
    Shinobi authenticated user
    """
    host: str
    port: str
    super_user_token: str = None
    super_user_email: str = None
    super_user_password: str = None

    def __init__(self, host, port, token=None, email=None, password=None):
        self.host = host
        self.port = port

        if token:
            self.super_user_token = token
        else:
            self.super_user_email = email
            self.super_user_password = password

    def authenticate(self):
        pass

    def get_url(self):
        return f"http://{self.host}:{self.port}/super"


@dataclass
class Admin:
    """
    Shinobi authenticated user
    """
    host: str
    port: str
    username: str
    password: str

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"

