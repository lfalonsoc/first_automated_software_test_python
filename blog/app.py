from typing import Any

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, \
"r" to read one, "p" to create post, or "q" to quit.'

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


def print_blogs() -> None:
    for key, blog in blogs.items():
        print("- {}".format(blog))
