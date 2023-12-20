from .config import *

config = Config(
    tg_bot=TgBot(
        token=env('BOT_TOKEN'),
    ),
    services=Services(
        convertio_api_key=env('CONVERTIO_API_KEY')
    )
)
