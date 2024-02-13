from unittest import TestCase
from blog.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self) -> None:
        b: Blog = Blog('Test', 'Test Author')
        
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.post)
        self.assertEqual(0, len(b.post))