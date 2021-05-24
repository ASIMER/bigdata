import os


class Config:
    def __init__(self):
        self.DB_API_KEY = os.environ.get("DB_API_KEY")
        self.DB_API_KEY_COMMENTS = os.environ.get("DB_API_KEY_COMMENTS")
        self.GET_PRICE_OF_SPECIFIC_GAME = os.environ.get("GET_PRICE_OF_SPECIFIC_GAME")
        self.LIST_GAMES_WITH_PRICES = os.environ.get("LIST_GAMES_WITH_PRICES")
        self.LIST_GAMES_WITH_NO_PRICES = os.environ.get("LIST_GAMES_WITH_NO_PRICES")
        self.GET_GAME_INFO = os.environ.get("GET_GAME_INFO")
        self.DB_LOCAL_COPY = os.environ.get("DB_LOCAL_COPY") == "True"
        self.RECORD_COMMENT = os.environ.get("RECORD_COMMENT")
        self.GET_GAME_COMMENTS = os.environ.get("GET_GAME_COMMENTS")
        self.GET_GAME_BY_NAME = os.environ.get("GET_GAME_BY_NAME")
