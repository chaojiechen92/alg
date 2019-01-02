class Dog():
    def __init__(self):
        self.type = "dog"

    def __str__(self):
        return str(self.type)


class Cat():
    def __init__(self):
        self.type = "cat"

    def __str__(self):
        return self.type


class Pet():
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def __str__(self):
        return str(self.pet)


class DCqueue():

    def __init__(self):
        self.dogq = []
        self.catq = []
        self.count = 0

    def pushDog(self):
        d = Dog()
        self.dogq.append(Pet(d, self.count))
        self.count += 1
        return

    def pushCat(self):
        d = Cat()
        self.catq.append(Pet(d, self.count))
        self.count += 1
        return

    def pullCat(self):
        if self.isEmptyCat():
            return None

        return self.catq.pop(0)

    def pullDog(self):
        if self.isEmptyDog():
            return None

        return self.dogq.pop(0)

    def pullAll(self):
        if self.isEmpty():
            return None
        if self.isEmptyDog():
            return self.catq.pop(0)
        if self.isEmptyCat():
            return self.dogq.pop(0)

        if self.dogq[0].count < self.catq[0].count:
            return self.dogq.pop(0)
        else:
            return self.catq.pop(0)

    def isEmpty(self):
        if not self.dogq and not self.catq:
            return True
        return False

    def isEmptyDog(self):
        if not self.dogq:
            return True
        return False

    def isEmptyCat(self):
        if not self.catq:
            return True
        return False


if __name__ == "__main__":
    d = DCqueue()
    d.pushCat()
    d.pushDog()
    d.pushCat()
    print(d.pullDog())
    print(d.pullAll())
    print(d.pullAll())
    print(d.pullAll())
