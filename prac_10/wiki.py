"""
Prac 10
Wikipedia
"""

import wikipedia
from wikipedia import PageError, DisambiguationError

search_string = input("Enter page title: ")
while search_string != "":
    try:
        page_title = wikipedia.page(search_string, auto_suggest=False)
        print(page_title.title)
        print(wikipedia.summary(search_string))
        print(page_title.url)
    except PageError:
        print(f'Page id "{search_string}" does not match any pages. Try another id!')
    except DisambiguationError as page_title_options:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(page_title_options.options)
    search_string = input("\nEnter page title: ")
print("Thank you.")