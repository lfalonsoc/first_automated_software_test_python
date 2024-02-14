from typing import Any
from unittest import TestCase
from unittest.mock import patch

import app
from blog.blog import Blog
from blog.post import Post


class TestsApp(TestCase):
    def setUp(self) -> None:
        blog: Blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}

    def test_menu_prints_blogs(self) -> None:
        with patch("builtins.print") as mocked_print:
            with patch("builtins.input", return_value="q"):
                app.menu()
                text: str = "- Test by Test Author (0 posts)"

                mocked_print.assert_called_with(text)

    def test_menu_calls_create_blog(self) -> None:
        with patch("builtins.input") as mck_inp:
            mck_inp.side_effect = ("c", "Test Create Blog", "Test Author", "q")
            app.menu()

            self.assertIsNotNone(app.blogs["Test Create Blog"])

    def test_menu_prints_prompt(self) -> None:
        with patch("builtins.input", return_value="q") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self) -> None:
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input", return_value="q"):
                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_ask_read_blogs(self) -> None:
        with patch("builtins.input") as mocked_input:
            with patch("app.ask_read_blog") as mocked_ask_read_blog:
                mocked_input.side_effect = ("r", "Test", "q")
                app.menu()

                mocked_ask_read_blog.assert_called()

    def test_menu_calls_ask_create_post(self) -> None:
        with patch("builtins.input") as mocked_input:
            with patch("app.ask_create_post") as mocked_ask_create_post:
                input: Any = ("p", "Test", "New Post", "New Content", "q")
                mocked_input.side_effect = input
                app.menu()

                mocked_ask_create_post.assert_called()

    def test_print_blogs(self) -> None:
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- Test by Test Author (0 posts)")

    def test_ask_create_blog(self) -> None:
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test Author")
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get("Test"))

    def test_ask_read_blog(self) -> None:
        with patch("builtins.input", return_value="Test"):
            with patch("app.print_posts") as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(app.blogs["Test"])

    def test_print_posts(self) -> None:
        blog: Any = app.blogs["Test"]
        blog.create_post("Post title", "Post content")
        with patch("app.print_post") as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self) -> None:
        post: Post = Post("Post title", "Post content")
        expected_print: str = """
--- Post title ---

Post content

"""
        with patch("builtins.print") as mocked_print:
            app.print_post(post)

            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self) -> None:
        app_blog_test: Any = app.blogs["Test"]
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test Title", "Test Content")
            app.ask_create_post()

            self.assertEqual(app_blog_test.posts[0].title, "Test Title")
            self.assertEqual(app_blog_test.posts[0].content, "Test Content")
