from ...core import Base_repository


class UserRepository(Base_repository):
    pass

    def all(self):
        query = "SELECT * FROM TABLE users"
        self.query(query)
