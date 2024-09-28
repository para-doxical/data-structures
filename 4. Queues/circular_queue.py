"""Author: Bamidele Oluwatosin Daniel. (Paradoxical)."""

# An implementation of a circular queue data structure, using python.

class circularQueue():
    """The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle, and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

    One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values."""

    def __init__(self, max_length=None):
        """
       Initiallizes circular queue with a maximum length.
       The default is that there is no maximum length. i.e
       max_length = None.
        """
        self.queue_list = []
        self.max_len = max_length
    
    def __str__(self):
        return self.queue_list.__str__()

    def enQueue(self, item):
        """
        Adds item as the new last item of circular queue.
        Returns true if the operation is successful or false if otherwise.
        """
        if (self.max_len == None or len(self.queue_list) < self.max_len):
            self.queue_list.append(item)
            return True
        return False

    def deQueue(self):
        """
        Deletes the first item from circular queue.
        Returns true if the operation is successful or false if otherwise.
        """
        if (len(self.queue_list) > 0):
            self.queue_list.pop(0)
            return True
        return False

    def Front(self):
        """
        Returns the first item of circular queue or -1 If the queue is empty.
        """
        if (len(self.queue_list) > 0):
            return self.queue_list[0]
        return -1

    def Rear(self):
        """
         Returns the last item of circular queue or -1 If the queue is empty.
        """
        if (len(self.queue_list) > 0):
            return self.queue_list[-1]
        return -1

    def isEmpty(self):
        """
        Returns true if circular queue is empty or false if otherwise.
        """
        return len(self.queue_list) == 0

    def isFull(self):
        """
        Returns true if circular queue is full or false if otherwise.
        """
        return False if (self.max_len == None) else len(self.queue_list) == self.max_len
    def clear(self):
        """
        Clears all the items in circular queue.
        """
        self.queue_list = []


if (__name__ == "__main__"):
    test_circular_queue = circularQueue(3)
    print(test_circular_queue.enQueue(1)) # return True
    print(test_circular_queue.enQueue(2)) # return True
    print(test_circular_queue.enQueue(3)) # return True
    print(test_circular_queue.enQueue(4)) # return False
    print(test_circular_queue.Rear())     # return 3
    print(test_circular_queue.isFull())   # return True
    print(test_circular_queue.deQueue())  # return True
    print(test_circular_queue.enQueue(4)) # return True
    print(test_circular_queue.Rear())     # return 4
    print(test_circular_queue)