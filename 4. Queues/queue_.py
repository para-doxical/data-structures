"""Author: Bamidele Oluwatosin Daniel (Paradoxical)."""

# An implementation of a queue data structure, using python.

class Queue:
    """A queue is a LIFO (Last in First out) linear data structure."""

    def __init__(self, max_length=None):
        """
       Initiallizes queue with a maximum length.
       The default is that there is no maximum length. i.e
       max_length = None.
        """
        self.queue_list = []
        self.max_len = max_length

    def __str__(self) -> str:
        return self.queue_list.__str__()
    
    def enqueue(self, item):
        """
        Adds item as the new last item of queue.
        Returns true if the operation is successful or false if otherwise.
        """
        if (self.max_len == None or len(self.queue_list) < self.max_len):
            self.queue_list.append(item)
            return True
        return False
    
    def dequeue(self):
        """
        Deletes the first item from queue.
        Returns true if the operation is successful or false if otherwise.
        """
        if (len(self.queue_list) > 0):
            self.queue_list.pop(0)
            return True
        return False
    
    def Front(self):
        """
        Returns the first item of queue or -1 If the queue is empty.
        """
        if (len(self.queue_list) > 0):
            return self.queue_list[0]
        return -1

    def Rear(self):
        """
         Returns the last item of queue or -1 If the queue is empty.
        """
        if (len(self.queue_list) > 0):
            return self.queue_list[-1]
        return -1
    
    def isEmpty(self):
        """
        Returns true if queue is empty or false if otherwise.
        """
        return len(self.queue_list) == 0

    def isFull(self):
        """
        Returns true if queue is full or false if otherwise.
        """
        return False if (self.max_len == None) else len(self.queue_list) == self.max_len
    def clear(self):
        """
        Clears all the items in queue.
        """
        self.queue_list = []
    

if __name__ == "__main__":
    my_queue = Queue()
    print(f"Queue is empty: {my_queue.isEmpty()}")
    print("# I'll enqueue 4, 10, 7 and 9 respectively.")
    my_queue.enqueue(4)
    my_queue.enqueue(10)
    my_queue.enqueue(7)
    my_queue.enqueue(9)
    print(f"After adding 4, 10, 7 and 9, my queue is now: {my_queue}")
    print(f"# Clearing my queue :(")
    my_queue.clear()
    print(f"After clearing my queue, my queue is now: {my_queue}")
    print(f"Queue is empty: {my_queue.isEmpty()}")
    print("# I'll add 3, 5 and -1 to my queue.")
    my_queue.enqueue(3)
    my_queue.enqueue(5)
    my_queue.enqueue(-1)
    print(f"After adding 3, 5 and -1, my queue is now: {my_queue}")
    print(f"Queue is empty: {my_queue.isEmpty()}")
    my_queue.dequeue()
    print(f"After dequeuing once, my queue is now: {my_queue}")
    my_queue.dequeue()
    print(f"After dequeuing twice, my queue is now: {my_queue}")
    my_queue.dequeue()
    print(f"After dequeuing thrice, my queue is now: {my_queue}")