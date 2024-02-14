from typing import Any
from unittest import TestCase
from unittest.mock import patch

import app
from blog.blog import Blog


class TestsApp(TestCase):
    def test_menu_prints_prompt(self) -> None:
        with patch("builtins.input") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_prints_blogs(self) -> None:
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input", return_value="q"):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_print_blogs(self) -> None:
        blog: Blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- Test by Test Author (0 posts)")
