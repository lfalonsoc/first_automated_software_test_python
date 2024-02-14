class Post:
    def __init__(self, title: str, content: str) -> None:
        self.title: str = title
        self.content: str = content

    def json(self) -> dict[str, str]:
        return {
            "title": self.title,
            "content": self.content,
        }
