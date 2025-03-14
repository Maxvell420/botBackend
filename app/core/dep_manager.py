from . import context


class DepManager:

    def __init__(self):
        self.context = self.get_context()
        pass

    def get_context(self):
        return context
