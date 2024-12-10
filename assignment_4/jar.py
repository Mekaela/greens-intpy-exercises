class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    # returns n cookies: "🍪🍪🍪" in jar
    def __str__(self):
        return self.size*'🍪'

    # add cookies in the kar, until capacity
    def deposit(self, n):
        # if adding n cookies exceeds capacity, return ValueError
        if self.size + n > self.capacity:
            raise ValueError("deposited cookies exceed capacity")
        self.size += n

    # remove n cookies from jar
    def withdraw(self, n):
        # if n exceeds cookies in jar, return ValueError
        if n > self.size:
            raise ValueError("insufficient cookies to withdraw")
        self.size -= n

    # return cookie jar's capacity: i.e. how many cookies can fit in the jar
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        # if capacity < 0 or not int, return ValueError
        if(capacity < 0):
            raise ValueError("capacity not large enough for cookies")
        self._capacity = capacity

    # return amount of cookies in jar
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar()
    print(jar)

if __name__ == "__main__":
    main()


# check50 cs50/problems/2022/python/jar
