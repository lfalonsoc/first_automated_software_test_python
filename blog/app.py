from typing import Any

from blog.blog import Blog

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, \
"r" to read one, "p" to create post, or "q" to quit.'
POST_TEMPLATE = """
--- {} ---

{}

"""

blogs: dict[Any, Any] = dict()  # blog_name : Blog object


def menu() -> None:
    print_blogs()
    selection: str = input(MENU_PROMPT)
    while selection != "q":
        if selection == "c":
            ask_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        selection: str = input(MENU_PROMPT)


def print_blogs() -> None:
    for blog in blogs.values():
        print("- {}".format(blog))


def ask_create_blog() -> None:
    title: str = input("Enter your blog title: ")
    author: str = input("Enter your name: ")

    blogs[title] = Blog(title, author)


def ask_read_blog() -> None:
    title: str = input("Enter the blog title you want to read: ")

    print_posts(blogs[title])


def print_posts(blog: Any) -> None:
    for post in blog.posts:
        print_post(post)


def print_post(post: Any) -> None:
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post() -> None:
    blog: str = input(
        "Enter the blog title you\
want to write a post in: "
    )
    title: str = input("Enter your post title: ")
    content: str = input("Enter your post content: ")

    blogs[blog].create_post(title, content)
