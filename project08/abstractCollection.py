"""
Project: 8
File: abstractcollection.py
Author: Laurie Jones, Harry Pinkerton, James Lawson
"""

class AbstractCollection(object):
    """An abstract collection implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._size = self._modCount = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "[" + ", ".join(map(str, self)) + "]"

    def __add__(self, other):
        """Returns a new collection containing the contents
        of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True

    def count(self, item):
        """Returns the number of instance of item in self."""
        counter = 0
        for nextItem in self:
            if item == nextItem: counter += 1
        return counter

    def getModCount(self):
        """Returns the number of mutations to this collection."""
        return self._modCount

    def incModCount(self):
        """Increments the number of mutations by one."""
        self._modCount += 1

    def resetSizeAndModCount(self):
        """Resets the numbers of items and mutations to 0."""
        self._size = 0
        self._modCount = 0


