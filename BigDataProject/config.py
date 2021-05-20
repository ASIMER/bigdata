import os


class Config:
    def __init__(self):
        self.DB_API_KEY = os.environ.get("DB_API_KEY")
        self.GET_PRICE_OF_SPECIFIC_GAME = os.environ.get("GET_PRICE_OF_SPECIFIC_GAME")
        self.LIST_GAMES_WITH_PRICES = os.environ.get("LIST_GAMES_WITH_PRICES")
        self.LIST_GAMES_WITH_NO_PRICES = os.environ.get("LIST_GAMES_WITH_NO_PRICES")
        self.DB_LOCAL_COPY = bool(os.environ.get("DB_LOCAL_COPY"))
