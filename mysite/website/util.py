import os


def get_entry(title):
    """
    Retrieves an entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = open('website/static/website/posts/'+f"{title}.md")
        print(f)
        return f.read()
    except FileNotFoundError:
        return None
