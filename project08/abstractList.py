"""
Project: 8
File: abstractlist.py
Author: Laurie Jones, Harry Pinkerton, James Lawson

Common data and method implementations for lists.
"""

from abstractCollection import AbstractCollection


class AbstractList(AbstractCollection):
    """Represents an abstract list."""

    def __init__(self, sourceCollection = None):
        """Sets up the collection."""
        self.modCount = 0
        super().__init__(sourceCollection)

    def getModCount(self):
        """Maintains a count of modifications to the list"""
        return self.modCount

    def incModCount(self):
        """Increments the count of modifications to the list"""
        self.modCount += 1

    def index(self, item):
        """Precondition: item is in the list.
        Returns the position of item.
        Raises: ValueError if the item is not in the list."""
        position = 0
        for data in self:
            if data == item:
                return position
            else:
                position =+ 1
        if position == len(self):
            raise ValueError(str(item) + "not in list")
    
    def remove(self, item):
        """Precondition: item is in the list.
        Raises: ValueError if item in not in self.
        Postcondition: item is removed from self."""
        position = self.index(item)
        self.pop(position)
        

    def add(self, item):
        """Adds the item to the end of the list."""
        self.insert(len(self), item)
        

    def append(self, item):
        """Adds the item to the end of the list."""
        self.add(item)

    def listIterator(self):
        """Returns a list iterator, should not be invoked at this level."""
        raise NotImplementedError("Abstract class method invoked.")
