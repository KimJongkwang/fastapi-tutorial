from dataclasses import dataclass
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """기본 Configuration"""

    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = False


@dataclass
class LocalConfig(Config):
    DB_URL: str = "mysql+pymysql://'travis':0000@localhost/notification_api?charset=utf8"
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]
    # "mysql+pymysql://travis:0000@localhost/notification_api?charset=utf8mb4"


@dataclass
class ProdConfig(Config):
    # 운영서버(Production Server)
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]


def conf():
    """환경에 따라 fastapi reload 설정 및 환경 불러오기"""
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))