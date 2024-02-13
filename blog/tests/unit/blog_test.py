from unittest import TestCase
from blog.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self) -> None:
        b: Blog = Blog('Test', 'Test Author')
        
        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.post)
        self.assertEqual(0, len(b.post))
        
    def test_repr(self):
        b: Blog = Blog('Test', 'Test Author')
        b2: Blog = Blog('My day', "Rolf")
        
        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'My day by Rolf (0 posts)')
    
    def test_repr_multiple_posts(self):
        b: Blog = Blog('Test', 'Test Author')
        b.post = ['test']
        b2: Blog = Blog('My day', "Rolf")
        b2.post = ['Test', "Another"]
        
        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My day by Rolf (2 posts)')