from ...core import Base_repository


class UserRepository(Base_repository):

    def __init__(self, conn, table: str = "bot_users"):
        super().__init__(conn, table)
