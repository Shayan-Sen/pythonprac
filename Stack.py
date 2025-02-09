class Stack:
    def __init__(self):
        self.stack = []
    
    def pushItem(self, item):
        self.stack.append(item)
    
    def popItem(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None
    
    def toList(self):
        return self.stack.copy()
    
    def printStack(self):
        print("Stack contents:", self.stack)
    
    def clearStack(self):
        self.stack.clear()
    
    def searchItem(self, item):
        try:
            return self.stack.index(item)
        except ValueError:
            return -1
    
    def isFull(self, maxSize):
        return len(self.stack) == maxSize
    
    def __str__(self):
        return str(self.stack)
    
    def __repr__(self):
        return repr(self.stack)


if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.isEmpty())
    stack.pushItem(10)
    stack.pushItem(20)
    stack.pushItem(30)
    print("Stack size:", stack.size())
    print("Top item:", stack.peek())
    print("Stack contents:", stack.toList())
    stack.printStack()
    print("Is 20 in stack?", 20 in stack.toList())
    print("Index of 20:", stack.searchItem(20))
    print("Is stack full?", stack.isFull(5))
    stack.clearStack()
    print("Stack after clearing:", stack)