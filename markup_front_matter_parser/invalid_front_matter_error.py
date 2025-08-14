class InvalidFrontMatterError(Exception):

    def __init__(self, message: str = "Invalid front matter encountered"):
        self.message = message
        super().__init__(f"{message}")
