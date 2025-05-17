class Stack:
    def __init__(self):
        self.stack=[]
    
    def __str__(self):
        value = [i for i in reversed(self.stack)]
        return '\n'.join(map(str, value))
    
    def is_empty(self):
        return not bool(self.stack)

    def push(self,value):
        self.stack.append(value)
    
    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return
        self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return
        return self.stack[len(self.stack)-1]

s=Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.peek())