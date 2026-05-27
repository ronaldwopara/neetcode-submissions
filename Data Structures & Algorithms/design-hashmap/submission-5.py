class MyHashMap:
    def __init__(self):
        self.size = 1000  
        self.table = [None] * self.size
        self.DELETED = -2  

    def hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)

        while self.table[idx] is not None and self.table[idx] is not self.DELETED:
            if self.table[idx][0] == key:
                self.table[idx] = (key, value)  
                return
            idx = (idx + 1) % self.size  

        self.table[idx] = (key, value)

    def get(self, key: int) -> int:
        idx = self.hash(key)

        while self.table[idx] is not None:
            if self.table[idx] is not self.DELETED and self.table[idx][0] == key:
                return self.table[idx][1]
            idx = (idx + 1) % self.size

        return -1

    def remove(self, key: int) -> None:
        idx = self.hash(key)

        while self.table[idx] is not None:
            if self.table[idx] is not self.DELETED and self.table[idx][0] == key:
                self.table[idx] = self.DELETED  
                return
            idx = (idx + 1) % self.size