from typing import List, Any


class Blog:
    def __init__(self, title:str, author: str) -> None:
        self.title: str = title
        self.author: str = author
        self.post: List[Any] = []
    
    def __repr__(self) -> str:
        return '{} by {} ({} post{})'.format(self.title, 
                                            self.author,
                                            len(self.post),
                                            's' if len(self.post) != 1 else '')
    
    def create_post(self, title: str, content: str):
        pass
    
    def json(self):
        pass