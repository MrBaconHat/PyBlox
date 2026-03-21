from ..utils.requests import make_request

class UsernameHistory:
    def __init__(self, client, user_id, limit, sort_order, nextCursor, previousCursor, data):
        
        self.__client = client
        
        self.__user_id = user_id
        self.__limit = limit
        self.__sort_order = sort_order
        
        self.next_cursor = nextCursor
        self.previous_cursor = previousCursor
        self.usernames = data

    async def next_page(self) -> "UsernameHistory":
        if not self.next_cursor:
            return None
            
        return await self.__client.get_username_history(
            user_id=self.__user_id,
            cursor=self.next_cursor,
            limit=self.__limit,
            sort_order=self.__sort_order
        )

    async def previous_page(self) -> "UsernameHistory":
        if not self.previous_cursor:
            return None
            
        return await  self.__client.get_username_history(
            user_id=self.__user_id,
            cursor=self.previous_cursor,
            limit=self.__limit,
            sort_order=self.__sort_order
        )