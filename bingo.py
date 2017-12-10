#Write a user defined callable type
#Functions act like object; we can also create class to be callable if we
#define the __call__ functions

import random

class bingo:

    def __init__(self, items):
        #list() will ensure that the original list is not edited
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty Bingo Cage')

    def __call__(self):
        return self.pick()

if __name__ == '__main__':
    obj = bingo(range(25))
    print(obj.pick())
    #the function basically becomes callable
    print(obj())
