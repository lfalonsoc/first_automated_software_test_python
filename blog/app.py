from typing import Any

blogs: dict[Any, Any] = dict() # blog_name : Blog object


def menu():
    """
    Show the user the available blogs
    Let the user make a choise
    Do something wit that choise
    Eventually exit
    """
    print_blogs()
    

def print_blogs() -> None:
    for key, blog in blogs.items():
        print("- {}".format(blog))
    