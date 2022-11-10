from dataclasses import dataclass

@dataclass
class ApiKey:
    """
    API key data model.
    """
    ip_addr: str
    auth_socket: bool
    get_monitors: bool
    control_monitors: bool
    get_logs: bool
    watch_stream: bool
    watch_snapshot: bool
    watch_videos: bool
    delete_video: bool
