class MarkupContent:
    """The contents of a markup file (e.g. markdown, HTML).

    In a future release this object could also have a property
    for tokenized markup while preserving the raw_content property.
    """

    def __init__(self, raw_content: str):
        self._raw_content = raw_content

    @property
    def raw_content(self) -> str:
        return self._raw_content
