from ...core import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, connector):
        super().__init__(connector)
        self.table = "bot_users"
