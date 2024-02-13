import sys
path = '/media/lfalonsoc/datos/docs_personales/estudio/python/automated_software_testing_with_python/first_automated_software_test_python/blog'
sys.path.insert(0, path)

from typing import Any
from unittest import TestCase
from unittest.mock import patch

import app
from blog.blog import Blog


class TestsApp(TestCase):
    def test_print_blog(self) -> None:
        blog: Blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')