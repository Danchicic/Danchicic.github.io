from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Services:
    convertio_api_key: str


@dataclass
class Config:
    tg_bot: TgBot
    services: Services


env = Env()
env.read_env()


