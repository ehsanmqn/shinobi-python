import requests
import json
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

    def url(self):
        return f"http://{self.host}:{self.port}?json=true"


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

    def __init__(self, host, port, apikey=None, email=None, password=None):
        self.host = host
        self.port = port

        if apikey:
            self.token = apikey
        else:
            self.email = email
            self.password = password

    @property()
    def url(self):
        return f"http://{self.host}:{self.port}?json=true"

    def authenticate(self):
        url = self.url()

        payload = json.dumps({
            "mail": self.email,
            "pass": self.password
        })
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code != 200:
            raise ValueError("A problem happened in deleting user in chat service")

        jsonify = response.json()
        self.token = jsonify["auth_token"]

        return jsonify["auth_token"]

    

