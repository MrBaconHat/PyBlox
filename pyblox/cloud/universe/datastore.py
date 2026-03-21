import aiohttp

class DataStore:
    def __init__(self, universe_id: int, api_key: str):
        self.universe_id = universe_id
        self.api_key = api_key