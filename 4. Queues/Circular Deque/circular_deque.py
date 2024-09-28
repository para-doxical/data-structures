"""Author: Bamidele Oluwatosin Daniel (Paradoxical)."""

# An implementation of circular dequeue data structure.


class circularDeque():
    """A circular deque is a queue data structure that allows insertion and deletion
    from both ends of the queue."""

    def __init__(self, max_length=None):
        """
        Initiallizes circular deque with a maximum length.
       The default is that there is no maximum length. i.e
       max_length = None.
        """
        self.items = []
        self.max_len = max_length

    def __str__(self):
        return self.items.__str__()   

    def insertFront(self, item):
        """
        Adds item to the front of circular deque.
        Returns true if the operation is successful or false if otherwise.
        """
        if (self.max_len == None or len(self.items) < self.max_len):
            self.items.insert(0, item)
            return True
        return False
        

    def insertLast(self, item):
        """
        Adds item to the end of circular deque.
        Returns true if the operation is successful or false if otherwise.
        """
        if (self.max_len == None or len(self.items) < self.max_len):
            self.items.append(item)
            return True
        return False

    def deleteFront(self):
        """
        Deletes the item at the front of circular deque.
        Returns true if the operation is successful or false if otherwise.
        """
        if (len(self.items) > 0):
            self.items.pop(0)
            return True
        return False

    def deleteLast(self):
        """
        Deletes the item at the end of circular deque.
        Returns true if the operation is successful or false if otherwise.
        """
        if (len(self.items) > 0):
            self.items.pop()
            return True
        return False

    def getFront(self):
        """
        Returns the first item in circular deque or -1 If circular deque is empty.
        """
        return self.items[0] if (len(self.items) > 0) else -1

    def getRear(self):
        """
        Returns the last item in circular deque or -1 If circular deque is empty.
        """
        return self.items[-1] if (len(self.items) > 0) else -1

    def isEmpty(self):
        """
        Returns true if circular deque is empty or false if otherwise.
        """
        return len(self.items) == 0

    def isFull(self):
        """
        Returns true if circular deque is full or false if otherwise.
        """
        return False if (self.max_len == None) else len(self.items) == self.max_len


if (__name__ == "__main__"):
    test_circular_deque = circularDeque(3)
    print(test_circular_deque.insertLast(1))  # return True
    print(test_circular_deque.insertLast(2))  # return True
    print(test_circular_deque.insertFront(3)) # return True
    print(test_circular_deque.insertFront(4)) # return False, the queue is full.
    print(test_circular_deque.getRear())      # return 2
    print(test_circular_deque.isFull())       # return True
    print(test_circular_deque.deleteLast())   # return True
    print(test_circular_deque.insertFront(4)) # return True
    print(test_circular_deque.getFront())     # return 4