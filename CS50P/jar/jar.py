class Jar:
    def __init__(self, capacity=12, n = 0):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.n = n

    def __str__(self):
        return '🍪' * self.n

    def deposit(self, n):
        self.n += n
        if self.n > self._capacity:
            raise ValueError

    def withdraw(self, n):
        if self.n < n:
            raise ValueError
        self.n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.n