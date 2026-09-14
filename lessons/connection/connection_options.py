from dataclasses import dataclass

@dataclass
class ConnectionOptions:
    HOST: str = "localhost"
    PORT: int = 6379
    DB: int = 0

