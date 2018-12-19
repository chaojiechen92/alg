class Minstack():
    def __init__(self):
        self.stack = []
        self.minstack = []

    def getMin(self):
        if self.minstack:
            return self.minstack[-1]

    def push(self, val):
        self.stack.append(val)
        if not self.minstack or val <= self.getMin():
            self.minstack.append(val)
        return

    def pop(self):
        if not self.stack:
            return
        val = self.stack.pop()
        if val == self.getMin():
            self.minstack.pop()

        return


if __name__ == "__main__":
    m = Minstack()
    m.push(3)
    m.push(2)
    m.push(1)
    print(m.pop())
    print(m.getMin())