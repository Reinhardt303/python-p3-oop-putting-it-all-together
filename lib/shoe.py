#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand = 'generic', size = 0):
        self.brand = brand
        self.size = size
        self.condition = 'not new'

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if type(size) == int:
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")


        