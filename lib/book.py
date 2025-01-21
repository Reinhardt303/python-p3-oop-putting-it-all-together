#!/usr/bin/env python3

class Book:

    def __init__(self, title = 'who reads books', page_count = 0):
        self.page_count = page_count
        self.title = title

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if type(page_count) == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title

    def turn_page(self):
        self.page_count += 1
        print("Flipping the page...wow, you read fast!")
    
        