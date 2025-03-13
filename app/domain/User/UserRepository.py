from ...core import Base_repository


class UserRepository(Base_repository):
    def __init__(self, connector):
        super().__init__(connector)
        self.table = "bot_users"
