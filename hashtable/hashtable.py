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

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
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

            current.next = HashTableEntry(key, value)
        else:
            self.storage[hi] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        self.storage[self.hash_index(key)] = None

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
            # print(v)
            while v:
                hi = self.hash_index(v.key)
                # print(v.next)
                # print(hi)
                if newarr[hi]:
                    current = newarr[hi]
                    # while current.next:
                    #     print(current.key)
                    #     current = current.next
                    # current.next = HashTableEntry(v.key, v.value)
                    # return

                else:
                    newarr[hi] = v
                # print(v.next)
                v = v.next

        # for ar in newarr:
        #     print(ar)

        self.storage = newarr


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")
    ht.put("line_4", "sss")
    ht.put("line_5", "ddd")
    ht.put("line_6", "ggg")
    ht.put("line_7", "hhh")

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

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))
    print(ht.get("line_4"))
    print(ht.get("line_5"))
    print(ht.get("line_6"))
    print(ht.get("line_7"))

    print("")

    # ht = HashTable(0x10000)

    # ht.put("key-0", "val-0")
    # ht.put("key-1", "val-1")
    # ht.put("key-2", "val-2")

    # ht.put("key-0", "new-val-0")
    # ht.put("key-1", "new-val-1")
    # ht.put("key-2", "new-val-2")

    # return_value = ht.get("key-0")
    # print(return_value, "new-val-0")
    # return_value = ht.get("key-1")
    # print(return_value, "new-val-1")
    # return_value = ht.get("key-2")
    # print(return_value, "new-val-2")

    # print("gg")
