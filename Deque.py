class deque(list):
    def Deque(self):
        self = []
    def addFront(self, item):
        self.insert(0, item)
    def addRear(self, item):
        self.append(item)
    def removeFront(self):
        self.pop(0)
    def removeRear(self):
        self.pop()
    def isEmpty(self):
        if len(self)==0:
            return True
        return False
    def size(self):
        return len(self)
    
            
