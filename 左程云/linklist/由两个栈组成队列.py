class Mystack():

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val):
        self.s1.append(val)

    def pop(self):
        if not self.s1 and not self.s2:
            return

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()


if __name__ == "__main__":
    m = Mystack()
    # m.push(1)
    # m.push(2)
    # m.push(3)
    print(m.pop())
    print(m.pop())
