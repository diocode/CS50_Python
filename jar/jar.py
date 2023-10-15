class Jar:
    def __init__(self, capacity=12):
        if int(capacity) >= 0:
            self._capacity = capacity
            self.cookies = 0
        else:
            raise ValueError

    def __str__(self):
        if self.cookies:
            return "🍪" * self.cookies
        else:
            return ""

    def deposit(self, n):
        if not (self.cookies + n > self.capacity):
            self.cookies += n
        else:
            raise ValueError

    def withdraw(self, n):
        if (self.cookies - n >= 0):
            self.cookies -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies

    @size.setter
    def size(self, size):
        self._size = size
