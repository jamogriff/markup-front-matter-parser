class InvalidMarkdownError(Exception):

    def __init__(self, file_path: str, message: str = "Invalid markdown file encountered"):
        self.file_path = file_path
        self.message = message
        super().__init__(f"{message}: {file_path}")
