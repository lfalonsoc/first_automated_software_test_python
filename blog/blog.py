from typing import List, Any

from blog.post import Post


class Blog:
    def __init__(self, title: str, author: str) -> None:
        self.title: str = title
        self.author: str = author
        self.posts: List[Any] = []

    def __repr__(self) -> str:
        return "{} by {} ({} post{})".format(
            self.title,
            self.author,
            len(self.posts),
            "s" if len(self.posts) != 1 else "",
        )

    def create_post(self, title: str, content: str) -> None:
        self.posts.append(Post(title, content))

    def json(self) -> dict[str, str | list[Any]]:
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }
