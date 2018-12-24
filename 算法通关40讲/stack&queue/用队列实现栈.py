class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x = []
        self.y = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.y.append(x)
        if len(self.y) > 1:
            self.x.append(self.y.pop(0))
        return

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return -1
        ret = self.y.pop(0)
        while self.x:
            self.y.append(self.x.pop(0))

        while len(self.y) > 1:
            self.x.append(self.y.pop(0))

        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.y[0]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.x and not self.y:
            return True
        return False


if __name__ == "__main__":
    pass
