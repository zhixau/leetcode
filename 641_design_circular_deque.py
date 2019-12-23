class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self._size = 0
        self._capacity = k
        self._queue = []

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self._queue.append(value)
        else:
            self._queue.insert(0, value)
        self._size = self._size + 1

        return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False

        self._queue.append(value)
        self._size = self._size + 1

        return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        try:
            self._queue.pop(0)
            self._size = self._size - 1
            return True
        except:
            return False

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False

        try:
            self._queue.pop()
            self._size = self._size - 1
            return True
        except:
            return False

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self._queue[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self._queue[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self._size == 0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self._size == self._capacity

if __name__ == "__main__":
    circularDeque = MyCircularDeque(3)
    a = circularDeque.insertLast(1) # return True
    print(a)
    b = circularDeque.insertLast(2) # return True
    print(b)
    c = circularDeque.insertFront(3) # return True
    print(c)
    d = circularDeque.insertFront(4) # return False
    print(d)
    e = circularDeque.getRear() # return 2
    print(e)
    f = circularDeque.isFull() # return true
    print(f)
    g = circularDeque.deleteLast()# return true
    print(g)
    h = circularDeque.insertFront(4) # return true
    print(h)
    i = circularDeque.getFront() # return 4
    print(i)
