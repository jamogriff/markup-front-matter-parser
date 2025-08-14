class MarkupContent:
    """The contents of a markup file (e.g. markdown, HTML).

    In a future release this object could also have a property
    for tokenized markup while preserving the raw property.
    """

    def __init__(self, raw: str):
        self._raw= raw

    @property
    def raw(self) -> str:
        return self._raw
