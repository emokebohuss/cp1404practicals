"""
Prac 10
Wikipedia
"""

import wikipedia
from wikipedia import PageError

search_string = input("Page title: ")
while search_string != "":
    try:
        page_title = wikipedia.page(search_string)
        print(page_title.title)
        print(page_title.url)
        print(page_title.images[0])
        print(search_string)
    except PageError:
        print(f"No results for {search_string}")
    search_string = input("Page title: ")
