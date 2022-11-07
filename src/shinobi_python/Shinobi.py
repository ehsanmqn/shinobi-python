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
        def add(uid, name, host, port, username=None, password=None):
            url = "{}/{}/configureMonitor/{}/{}".format(self.url(), self.token, self.group_key, uid)

            payload = json.dumps({
                "data": {
                    "ke": self.uid,
                    "name": name,
                    "shto": "[]",
                    "shfr": "[]",
                    "details": {
                    "max_keep_days": "",
                    "notes": "",
                    "dir": "",
                    "auto_compress_videos": None,
                    "rtmp_key": "",
                    "auto_host_enable": "1",
                    "auto_host": "",
                    "rtsp_transport": "tcp",
                    "muser": username,
                    "mpass": password,
                    "port_force": "0",
                    "fatal_max": "0",
                    "skip_ping": None,
                    "is_onvif": None,
                    "onvif_non_standard": None,
                    "onvif_port": "",
                    "primary_input": "0",
                    "aduration": "1000000",
                    "probesize": "1000000",
                    "stream_loop": "0",
                    "sfps": "",
                    "wall_clock_timestamp_ignore": None,
                    "accelerator": "0",
                    "hwaccel": "auto",
                    "hwaccel_vcodec": "",
                    "hwaccel_device": "",
                    "stream_type": "hls",
                    "stream_flv_type": "ws",
                    "stream_flv_maxLatency": "",
                    "stream_mjpeg_clients": "",
                    "stream_vcodec": "copy",
                    "stream_acodec": "no",
                    "hls_time": "2",
                    "hls_list_size": "3",
                    "preset_stream": "ultrafast",
                    "stream_quality": "15",
                    "stream_fps": "2",
                    "stream_scale_x": "",
                    "stream_scale_y": "",
                    "stream_rotate": None,
                    "signal_check": "10",
                    "signal_check_log": "0",
                    "stream_vf": "",
                    "tv_channel": "0",
                    "tv_channel_id": "",
                    "tv_channel_group_title": "",
                    "stream_timestamp": "0",
                    "stream_timestamp_font": "",
                    "stream_timestamp_font_size": "",
                    "stream_timestamp_color": "",
                    "stream_timestamp_box_color": "",
                    "stream_timestamp_x": "",
                    "stream_timestamp_y": "",
                    "stream_watermark": "0",
                    "stream_watermark_location": "",
                    "stream_watermark_position": "tr",
                    "snap": "0",
                    "snap_fps": "",
                    "snap_scale_x": "",
                    "snap_scale_y": "",
                    "snap_vf": "",
                    "vcodec": "copy",
                    "crf": "1",
                    "preset_record": "",
                    "acodec": "no",
                    "record_scale_y": "",
                    "record_scale_x": "",
                    "cutoff": "15",
                    "rotate": None,
                    "vf": "",
                    "timestamp": "0",
                    "timestamp_font": "",
                    "timestamp_font_size": "10",
                    "timestamp_color": "white",
                    "timestamp_box_color": "0x00000000@1",
                    "timestamp_x": "(w-tw)/2",
                    "timestamp_y": "0",
                    "watermark": "0",
                    "watermark_location": "",
                    "watermark_position": "tr",
                    "record_timelapse": None,
                    "record_timelapse_mp4": None,
                    "record_timelapse_fps": None,
                    "record_timelapse_scale_x": "",
                    "record_timelapse_scale_y": "",
                    "record_timelapse_vf": "",
                    "record_timelapse_watermark": None,
                    "record_timelapse_watermark_location": "",
                    "record_timelapse_watermark_position": None,
                    "detector": "0",
                    "onvif_events": None,
                    "detector_save": "1",
                    "use_detector_filters": "0",
                    "use_detector_filters_object": "1",
                    "detector_record_method": "sip",
                    "detector_trigger": "1",
                    "detector_buffer_seconds_before": "",
                    "detector_timeout": "0.5",
                    "watchdog_reset": "1",
                    "detector_delete_motionless_videos": "0",
                    "detector_http_api": None,
                    "detector_send_frames": "1",
                    "detector_fps": "",
                    "detector_scale_x": "640",
                    "detector_scale_y": "480",
                    "detector_lock_timeout": "",
                    "detector_send_video_length": "",
                    "snap_seconds_inward": "",
                    "cords": "[]",
                    "detector_filters": "{\"7cam3\":{\"id\":\"7cam3\",\"enabled\":\"1\",\"filter_name\":\"Standard Object Detection Filter\",\"where\":[{\"p1\":\"tag\",\"p2\":\"!indexOf\",\"p3\":\"person\",\"p4\":\"&&\"},{\"p1\":\"tag\",\"p2\":\"!indexOf\",\"p3\":\"car\",\"p4\":\"&&\"},{\"p1\":\"tag\",\"p2\":\"!indexOf\",\"p3\":\"truck\",\"p4\":\"&&\"}],\"actions\":{\"halt\":\"1\",\"save\":\"\",\"indifference\":\"\",\"webhook\":\"\",\"command\":\"\",\"record\":\"\",\"emailClient\":\"\",\"global_webhook\":\"\"}}}",
                    "det_multi_trig": None,
                    "group_detector_multi": [],
                    "detector_pam": "1",
                    "detector_sensitivity": "",
                    "detector_max_sensitivity": "",
                    "detector_threshold": "1",
                    "detector_color_threshold": "",
                    "inverse_trigger": None,
                    "detector_frame": "0",
                    "detector_motion_tile_mode": None,
                    "detector_tile_size": "",
                    "detector_noise_filter": None,
                    "detector_noise_filter_range": "",
                    "detector_use_detect_object": "0",
                    "detector_send_frames_object": None,
                    "detector_obj_count_in_region": None,
                    "detector_obj_region": None,
                    "detector_use_motion": "1",
                    "detector_fps_object": "",
                    "detector_scale_x_object": "",
                    "detector_scale_y_object": "",
                    "detector_buffer_vcodec": "auto",
                    "detector_buffer_acodec": None,
                    "detector_buffer_fps": "",
                    "event_record_scale_x": "",
                    "event_record_scale_y": "",
                    "event_record_aduration": "",
                    "event_record_probesize": "",
                    "detector_audio": None,
                    "detector_audio_min_db": "",
                    "detector_audio_max_db": "",
                    "detector_webhook": "0",
                    "detector_webhook_timeout": "",
                    "detector_webhook_url": "",
                    "detector_webhook_method": None,
                    "detector_command_enable": "0",
                    "detector_command": "",
                    "detector_command_timeout": "",
                    "detector_notrigger": "0",
                    "detector_notrigger_timeout": "",
                    "detector_notrigger_discord": None,
                    "detector_notrigger_webhook": None,
                    "detector_notrigger_webhook_url": "",
                    "detector_notrigger_webhook_method": None,
                    "detector_notrigger_command_enable": None,
                    "detector_notrigger_command": "",
                    "detector_notrigger_command_timeout": "",
                    "control": "0",
                    "control_base_url": "",
                    "control_url_method": None,
                    "control_digest_auth": None,
                    "control_stop": "0",
                    "control_url_stop_timeout": "",
                    "control_turn_speed": "",
                    "detector_ptz_follow": None,
                    "detector_ptz_follow_target": "",
                    "control_url_center": "",
                    "control_url_left": "",
                    "control_url_left_stop": "",
                    "control_url_right": "",
                    "control_url_right_stop": "",
                    "control_url_up": "",
                    "control_url_up_stop": "",
                    "control_url_down": "",
                    "control_url_down_stop": "",
                    "control_url_enable_nv": "",
                    "control_url_disable_nv": "",
                    "control_url_zoom_out": "",
                    "control_url_zoom_out_stop": "",
                    "control_url_zoom_in": "",
                    "control_url_zoom_in_stop": "",
                    "control_invert_y": None,
                    "groups": [],
                    "notify_emailClient": None,
                    "notify_global_webhook": None,
                    "notify_onUnexpectedExit": None,
                    "notify_useRawSnapshot": None,
                    "detector_emailClient_timeout": "",
                    "cust_input": "",
                    "cust_stream": "",
                    "cust_snap": "",
                    "cust_record": "",
                    "cust_detect": "",
                    "cust_detect_object": "",
                    "cust_sip_record": "",
                    "custom_output": "",
                    "loglevel": "warning",
                    "sqllog": "0",
                    "detector_cascades": "",
                    "stream_channels": "",
                    "input_maps": "",
                    "input_map_choices": {
                        "stream": [],
                        "snap": [],
                        "record": [],
                        "record_timelapse": [],
                        "detector": [],
                        "detector_object": [],
                        "detector_sip_buffer": []
                    },
                    "substream": {
                        "input": {
                        "type": "h264",
                        "stream_flv_type": None,
                        "fulladdress": "",
                        "sfps": "",
                        "aduration": "",
                        "probesize": "",
                        "stream_loop": None,
                        "rtsp_transport": "",
                        "accelerator": "0",
                        "hwaccel": None,
                        "hwaccel_vcodec": "",
                        "hwaccel_device": "",
                        "cust_input": ""
                        },
                        "output": {
                        "stream_type": "hls",
                        "stream_mjpeg_clients": "",
                        "stream_vcodec": "copy",
                        "stream_acodec": "no",
                        "hls_time": "",
                        "hls_list_size": "",
                        "preset_stream": "",
                        "stream_quality": "",
                        "stream_v_br": "",
                        "stream_a_br": "",
                        "stream_fps": "",
                        "stream_scale_x": "640",
                        "stream_scale_y": "480",
                        "stream_rotate": None,
                        "svf": "",
                        "cust_stream": ""
                        }
                    }
                    },
                    "type": "h264",
                    "ext": "mp4",
                    "protocol": "rtsp",
                    "host": host,
                    "path": "/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif",
                    "port": port,
                    "fps": 1,
                    "mode": "start",
                    "width": 640,
                    "height": 480,
                    "saveDir": "",
                    "currentlyWatching": 0,
                    "status": "Watching",
                    "code": "2",
                    "streams": [
                    "/49698d0ad9df3cf212eebc959225a8f9/hls/tenantuuid1//s.m3u8"
                    ],
                    "streamsSortedByType": {
                    "hls": [
                        "/49698d0ad9df3cf212eebc959225a8f9/hls/tenantuuid1//s.m3u8"
                    ]
                    }
                }
            })
            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in adding monitor with id {}".format(uid))

            return response.json()["ok"]
        
        """
        Update a single monitor by ID
        """
        def update(uid, data):
            url = "{}/{}/configureMonitor/{}/{}".format(self.url(), self.token, self.group_key, uid)

            payload = json.dumps(data)

            headers = {
            'Content-Type': 'application/json'
            }

            response = requests.request("PUT", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in updating monitor with id {}".format(uid))

            return response.json()["ok"]
        
        """
        Delete a monitor by ID
        """
        def delete(uid):
            url = "{}/{}/configureMonitor/{}/{}/delete".format(self.url(), self.token, self.group_key, uid)

            payload={}
            headers = {}

            response = requests.request("DELETE", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in deleting monitor with id {}".format(uid))

            return response.json()["ok"]
        
        """
        Get a single monitor by ID
        and it will have a set of stream links already pre-built in the streams variable.
        """
        def get(uid):
            url = "{}/{}/monitor/{}/{}".format(self.url(), self.token, self.group_key, uid)

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in getting monitor with id {}".format(uid))

            return response.json()
        
        def tv_channels(uid=None):

            if uid is None:
                url = "{}/{}/tvChannels/{}".format(self.url(), self.token, self.group_key)
            else:
                url = "{}/{}/tvChannels/{}/{}".format(self.url(), self.token, self.group_key, uid)

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in getting monitor with id {}".format(uid))

            return response.json()

    class Stream:
        """
        Get JPEG Snapshot
        Snapshot must be enabled in Monitor Settings.
        """
        def jpeg(monitor_id):
            url = "{}/{}/jpeg/{}/{}/s.jpg".format(self.url(), self.token, self.group_key, monitor_id)

            payload={}
            headers = {}

            if response.status_code != 200:
                raise ValueError("Problem in getting snapshot from monitor with id {}".format(monitor_id))

            response = requests.request("GET", url, headers=headers, data=payload)

            return response
        
        """
        Get MJPEG Stream
        Stream type must be MJPEG.
        """
        def mjpeg(monitor_id):
            url = "{}/{}/mjpeg/{}/{}?full=true".format(self.url(), self.token, self.group_key, monitor_id)

            payload={}
            headers = {}

            if response.status_code != 200:
                raise ValueError("Problem in getting stream from monitor with id {}".format(monitor_id))

            response = requests.request("GET", url, headers=headers, data=payload)

            return response

        """
        Get m3u8 for HLS Stream
        Stream type must be HLS.
        """
        def hls(monitor_id):
            url = "{}/{}/hls/{}/{}/s.m3u8".format(self.url(), self.token, self.group_key, monitor_id)

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in getting HLS stream from monitor with id {}".format(monitor_id))

            return response

        """
        Get FLV Stream
        Stream type must be FLV.
        """
        def flv():
            url = "{}/{}/flv/{}/{}/s.flv".format(self.url(), self.token, self.group_key, monitor_id)

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in getting FLV stream from monitor with id {}".format(monitor_id))

            return response

        """
        Poseidon (MP4) Stream
        Stream type must be Poesidon.
        """
        def mp4(monitor_id):
            url = "{}/{}/mp4/{}/{}/s.mp4".format(self.url(), self.token, self.group_key, monitor_id)

            payload={}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            if response.status_code != 200:
                raise ValueError("Problem in getting MP4 stream from monitor with id {}".format(monitor_id))

            return response

        """
        Get all available h.264 streams in an .m3u8 playlist
        Enable the TV Channel option in your monitor's settings to see their streams in this list.
        """
        def list():
            pass

        """
        Get a single monitor's available h.264 streams in an .m3u8 playlist
        Enable the TV Channel option in your monitor's settings to see their streams in this list.
        """
        def get_all_streams(monitor_id):
            pass

        """
        MJPEG Stream for iframe
        """
        def mjpeg_stream_iframe():
            pass

        """
        Poseidon (MP4) Stream
        This function provides the link for a Poseidon stream but on a channel aside from the Main one. You can create Stream Channels by opening your Monitor Settings, clicking Options, and then selecting Add Channel.
        """
        def stream_channels():
            pass