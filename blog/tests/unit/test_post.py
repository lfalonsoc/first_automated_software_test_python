from unittest import TestCase
from blog.post import Post


class PostTesgt(TestCase):
    def test_create(self) -> None:
        p: Post = Post("Test", "Test Content")

        self.assertEqual("Test", p.title)
        self.assertEqual("Test Content", p.content)

    def test_json(self) -> None:
        p: Post = Post("Test", "Test Content")
        expected: dict[str, str] = {"title": "Test", "content": "Test Content"}

        self.assertDictEqual(expected, p.json())
