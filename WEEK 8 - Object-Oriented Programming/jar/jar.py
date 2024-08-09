class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError()
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return self.cookies * '🍪'

    def deposit(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError()
        if self.cookies + n > self._capacity:
            raise ValueError()
        self.cookies += n

    def withdraw(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError()
        if self.cookies < n:
            raise ValueError()
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if not isinstance(new_capacity, int) or new_capacity < 0:
            raise ValueError()
        self._capacity = new_capacity

    @property
    def size(self):
        return self.cookies
