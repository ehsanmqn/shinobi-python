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
    group_key: str = None
    uid: str = None

    def __init__(self, host, port, apikey=None, email=None, password=None):
        self.host = host
        self.port = port

        if apikey:
            self.token = apikey
        else:
            self.email = email
            self.password = password

    def url(self):
        return f"http://{self.host}:{self.port}?json=true"

    """
    Login to Shinobi using user credentials
    When you authenticate with Shinobi it will offer you an Authorization Token. This token is your Session Key as well and can be used as an API Key. This key will remain active for 15 minutes after the last acivity or while your WebSocket is connected.
    """
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
            raise ValueError("Problem in login")

        jsonify = response.json()
        self.token = jsonify["auth_token"]
        self.group_key = jsonify["ke"]
        self.uid = jsonify["uid"]

        return jsonify["auth_token"]

    """
    API Key management class
    """
    class APIKey:
        """
        Get API Keys
        """
        def list():
            url = "{}/{}/api/{}/list".format(self.url(), self.token, self.group_key)

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in getting API Key")

            return response.json()["keys"]
        
        """
        Add an API Key
        The created key is binded to the user who created it.
        """
        def add(ip, auth_socket=1, get_monitors=1, control_monitors=1, get_logs=1, watch_stream=1, watch_snapshot=1, watch_videos=1, delete_videos=1):
            url = "{}/{}/api/{}/add".format(self.url(), self.token, self.group_key)

            payload = json.dumps({
                "data": {
                    "ip": "0.0.0.0",
                    "details": {
                        "auth_socket": "1",
                        "get_monitors": "1",
                        "control_monitors": "1",
                        "get_logs": "1",
                        "watch_stream": "1",
                        "watch_snapshot": "1",
                        "watch_videos": "1",
                        "delete_videos": "1"
                    }
                }
            })
            
            headers = {
                'Content-Type': 'application/json'
            }

            if response.status_code != 200:
                raise ValueError("Problem in adding API Key")

            response = requests.request("POST", url, headers=headers, data=payload)

            return response.json()["api"]

        """
        Delete an API Key
        """
        def delete(code):
            url = "{}/{}/api/{}/delete".format(self.url(), self.token, self.group_key)

            payload = json.dumps({
                "data": {
                    "code": code
                }
            })

            headers = {
                'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
    
            if response.status_code != 200:
                raise ValueError("Problem in adding API Key")

            return True

    """
    Monitor management class
    """
    class Monitor:
        """
        Get all saved monitors
        """
        def list():
            url = "{}/{}/monitor/{}".format(self.url(), self.token, self.group_key)

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in getting monitors")

            return response.json()
        
        """
         Add a monitor
        """
        def add():
            pass
        
        """
        Update a single monitor by ID
        """
        def update():
            pass
        
        """
        Delete a monitor by ID
        """
        def delete():
            pass
        
        """
        Get a single monitor by ID
        and it will have a set of stream links already pre-built in the streams variable.
        """
        def get(monitor_id):
            url = "{}/{}/monitor/{}/{}".format(self.url(), self.token, self.group_key, monitor_id)

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in getting monitor with id {}".format(monitor_id))

            return response.json()
        
        """
        Get all available h.264 streams in an .m3u8 playlist
        Enable the TV Channel option in your monitor's settings to see their streams in this list.
        """
        def get_all_streams():
            pass

        """
        Get a single monitor's available h.264 streams in an .m3u8 playlist
        Enable the TV Channel option in your monitor's settings to see their streams in this list.
        """
        def get_all_streams():
            pass

        """
        JPEG Snapshot
        Snapshot must be enabled in Monitor Settings.
        """
        def jpeg_snapshot():
            pass
        
        """
        MJPEG Stream
        Stream type must be MJPEG.
        """
        def mjpeg_stream():
            pass

        """
        MJPEG Stream for iframe
        """
        def mjpeg_stream_iframe():
            pass

        """
        m3u8 for HLS Stream
        Stream type must be HLS.
        """
        def m3u8_stream():
            pass
        
        """
        FLV Stream
        Stream type must be FLV.
        """
        def flv():
            pass
        
        """
        Poseidon (MP4) Stream
        Stream type must be Poesidon.
        """
        def mp4():
            pass

        """
        Poseidon (MP4) Stream
        This function provides the link for a Poseidon stream but on a channel aside from the Main one. You can create Stream Channels by opening your Monitor Settings, clicking Options, and then selecting Add Channel.
        """
        def stream_channels():
            pass