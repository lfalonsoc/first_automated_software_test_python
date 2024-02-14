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
    """
    1. Show the user the available blogs
    2. Let the user make a choise
    3. Do something wit that choise
    4. Eventually exit
    """
    print_blogs()  # 1.
    selection: str = input(MENU_PROMPT)  # 2.
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
    for key, blog in blogs.items():
        print("- {}".format(blog))


def ask_create_blog() -> None:
    title: str = input("Enter your blog title: ")
    author: str = input("Enter your name: ")

    blogs[title] = Blog(title, author)


def ask_read_blog() -> None:
    title: str = input("Enter the blog title you want to red: ")

    print_posts(blogs[title])


def print_posts(post: Any) -> None:
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post() -> None:
    pass
