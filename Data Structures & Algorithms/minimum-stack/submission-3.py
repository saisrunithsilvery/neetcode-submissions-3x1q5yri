class MinStack:

    def __init__(self):
        self.stack =[]
        self.min1=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min1:
            self.min1.append(min(self.min1[-1], val))
        else:
            self.min1.append(val)    

        

    def pop(self) -> None:
        self.stack.pop()
        self.min1.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min1[-1]
        
