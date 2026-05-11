class LinkedList:
    linked = []
    
    def __init__(self):
        self.linked = []
    
    def get(self, index: int) -> int:
        if index >= len(self.linked):
            return -1
        for i in range(len(self.linked)):
            if self.linked[i][1] - 1 == index:
                return self.linked[i][0]

    def insertHead(self, val: int) -> None:
        self.linked.insert(0, [val, 0])
        for i in range(len(self.linked)):
            self.linked[i][1] += 1

    def insertTail(self, val: int) -> None:
        self.linked.append([val, len(self.linked) + 1])

    def remove(self, index: int) -> bool:
        if index >= len(self.linked):
            return False
        self.linked.pop(index)
        for i in range(index, len(self.linked)):
            self.linked[i][1] -= 1
        return True

    def getValues(self) -> List[int]:
        return [x[0] for x in self.linked[:]]
