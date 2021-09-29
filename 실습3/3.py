class Set:
    def __init__(self):
        self.items = []

    def __eq__(self, setB):
        if len(self.items) == len(setB.items) and self.items.sort() == setB.items.sort():
            return True
        else:
            return False

    def insert(self, elem):
        if elem not in self.items:
            self.items.append(elem)

    def delete(self, elem):
        if elem in self.items:
            self.items.remove(elem)

    def union(self, setB):
        setC = Set()
        setC.items = list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC

    def intersect(self, setB):
        setC = Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC

    def difference(self, setB):
        setC = Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC
    
    def isSubset(self, setB):
        return all(elem in setB.items for elem in self.items)
        
    def isProperSubset(self, setB):
        return self.isSubset(setB) and self != setB

    def size(self):
        return len(self.items)

    def print(self):
        return self.items

def test(setA, setB):
    print(f"setA: {setA.print()}")
    print(f"setB: {setB.print()}")
    if setA == setB:
        print("A equal B: True")
    else:
        print("A euqal B: False")

    print(f"A subset B: {setA.isSubset(setB)}")
    print(f"A proper subset B: {setA.isProperSubset(setB)}")
    print(f"A union B: {setA.union(setB).print()}")
    print(f"A intersect B: {setA.intersect(setB).print()}")
    print(f"A difference B: {setA.difference(setB).print()}")
    print()


def main():
    setA = Set()
    setA.insert(2)
    setA.insert(3)
    setA.insert(4)
    
    setB = Set()
    setB.insert(2)
    setB.insert(3)
    setB.insert(4)
    
    setC = Set()
    setC.insert(2)
    setC.insert(3)
    
    test(setA, setB)
    test(setA, setC)
    test(setC, setA)
    
    
main()