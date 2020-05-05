class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        # self.storage = HashTableEntry()
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        # hash = 0xff
        hash = 0xcbf29ce484222325
        for n in key.encode():
            # print(n)
            hash = hash ^ n
            hash = hash * 0x100000001b3

        # print(hash)
        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """

        hash = 5381
        for n in key.encode():
            # hash = ((hash << 5) + hash) + n
            hash = hash * 33 + n

        return hash
        # return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hi = self.hash_index(key)
        if self.storage[hi]:
            current = self.storage[hi]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if(current.next is None):
                    current.next = HashTableEntry(key, value)
                    return
                current = current.next

            # current.next = HashTableEntry(key, value)
        else:
            self.storage[hi] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        hi = self.hash_index(key)
        print(hi)

        # if its a single node just delete it
        if self.storage[hi].next == None:
            if self.storage[hi].key == key:
                self.storage[hi] = None
            else:
                print("WARNING: no key")
        else:
            current = self.storage[hi]
            prev = current
            while current.next and current.key != key:
                prev = current
                current = current.next

            # if its the first link in the list
            if (current.key == self.storage[hi].key):
                print("1")
                self.storage[hi] = current.next
            elif (current.key == key):
                print("2")
                prev.next = current.next
            else:
                print("WARNING: no key")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hi = self.hash_index(key)
        if (self.storage[hi]):
            if(self.storage[hi].next):
                current = self.storage[hi]
                while current.key != key:
                    current = current.next
                return current.value
            else:
                return self.storage[hi].value

        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        self.capacity *= 2
        newarr = [None] * self.capacity

        for i, v in enumerate(self.storage):
            while v:
                hi = self.hash_index(v.key)
                if newarr[hi]:
                    current = newarr[hi]
                    while current.next:
                        current = current.next

                    current.next = HashTableEntry(v.key, v.value)
                else:
                    newarr[hi] = HashTableEntry(v.key, v.value)

                v = v.next

        self.storage = newarr

        # Solution 2 - Much cleaner
        # newHashTable = HashTable(self.capacity*2)
        # for i, v in enumerate(self.storage):
        #     while v:
        #         newHashTable.put(v.key, v.value)
        #         v = v.next

        # self.capacity = newHashTable.capacity
        # self.storage = newHashTable.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "111")
    ht.put("line_2", "222")
    ht.put("line_3", "333")
    ht.put("line_4", "sss")
    ht.put("line_5", "ddd")
    ht.put("line_6", "ggg")
    ht.put("line_7", "hhh")
    ht.put("line_12", "jjj")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))
    print(ht.get("line_4"))
    print(ht.get("line_5"))
    print(ht.get("line_6"))
    print(ht.get("line_7"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()

    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    print("1: ", ht.storage[1].value)
    print("1: ", ht.storage[1].next.value)

    print("3: ", ht.storage[3].value)
    print("3: ", ht.storage[3].next.value)
    print("3: ", ht.storage[3].next.next.value)

    print("")
    for i, v in enumerate(ht.storage):
        while v:
            print(i, v.value)
            v = v.next
    print("")
    ht.delete("line_8")
    print("")
    for i, v in enumerate(ht.storage):
        while v:
            print(i, v.value)
            v = v.next
    print("")

    # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))
    # print(ht.get("line_4"))
    # print(ht.get("line_5"))
    # print(ht.get("line_6"))
    # print(ht.get("line_7"))

    # print("")
