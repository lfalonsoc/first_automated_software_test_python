from unittest import TestCase
from unittest.mock import patch

import app
from blog.blog import Blog
from blog.post import Post


class TestsApp(TestCase):
    def test_menu_calls_create_blog(self) -> None:
        with patch("builtins.input") as mocked_inp:
            mocked_inp.side_effect("c", "Test Create Blog", "Test Author", "q")

            app.menu()

            self.assertIsNotNone(app.blogs["Test Create Blog"])

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

    def test_ask_create_blog(self) -> None:
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test Author")
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get("Test"))

    def test_ask_read_blog(self) -> None:
        blog: Blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        with patch("builtins.input", return_value="Test"):
            with patch("app.print_posts") as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self) -> None:
        blog: Blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        with patch("builtins.print") as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self) -> None:
        post: Post = Post("Pist title", "Post content")
        expect_print: str = """
--- Post title ---

Post content

"""
        with patch("builtins.print") as mocket_print:
            app.print_posts(post)

            mocket_print.assert_called_with(expect_print)

    def test_ask_create_post(self) -> None:
        blog: Blog = Blog("Test", "Test Author")
        app.blogs = {"Test": blog}
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ("Test", "Test Title", "Test Content")
            app.ask_create_post()

            self.assertEqual(blog.posts[0].title, "Test Title")
            self.assertEqual(blog.posts[0].content, "Test Content")
