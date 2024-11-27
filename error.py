class DataGouvException(Exception):
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description
        super().__init__(description)