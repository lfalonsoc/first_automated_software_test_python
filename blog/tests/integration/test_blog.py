from unittest import TestCase
from typing import Any

from blog.blog import Blog

class BlogTest(TestCase):    
    def test_create_post_in_blog(self) -> None:
        b: Blog = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')
        
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')
        
    def test_jason_no_post(self) -> None:
        b: Blog = Blog('Test', 'Test Author')
        expected: dict[str, str | Any] = {'title': 'Test',
                                    'author': 'Test Author',
                                    'posts': [],}
        
        self.assertDictEqual(expected, b.json())
    
    def test_json(self) -> None:
        b: Blog = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')
        
        expected: dict[str, str | Any] = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Test Post',
                    'content': 'Test Content',
                }
            ]
        }
        
        self.assertDictEqual(expected, b.json())