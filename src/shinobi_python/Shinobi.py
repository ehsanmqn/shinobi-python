from dataclasses import dataclass


class Super:
    """
    Shinobi Super user APIs
    """
    host: str
    port: str
    token: str = None
    email: str = None
    password: str = None
    apikey: str = None

    def __init__(self, host, port, apikey=None, email=None, password=None):
        self.host = host
        self.port = port

        if apikey:
            self.apikey = apikey
        else:
            self.email = email
            self.password = password

    def authenticate(self):
        pass

    def url(self):
        return f"http://{self.host}:{self.port}/super"


@dataclass
class Admin:
    """
    Shinobi Admin user APIs
    """
    host: str
    port: str
    token: str = None
    email: str = None
    password: str = None
    apikey: str = None

    def __init__(self, host, port, apikey=None, email=None, password=None):
        self.host = host
        self.port = port

        if apikey:
            self.apikey = apikey
        else:
            self.email = email
            self.password = password

    def authenticate(self):
        pass

    @property
    def url(self) -> str:
        return f"http://{self.host}:{self.port}"

