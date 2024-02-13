from typing import List, Any


class Blog:
    def __init__(self, title:str, author: str) -> None:
        self.title: str = title
        self.author: str = author
        self.post: List[Any] = []