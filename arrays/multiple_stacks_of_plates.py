class MultipleStacksOfPlates:
    def __init__(self,capacity):
        self.capacity=capacity
        self.stacks=[]
    
    def __str__(self):
        return ' '.join(map(str,self.stacks))
    
    def push(self,value):
        if not self.stacks or len(self.stacks[-1])>=self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)
    
    def pop(self):
        if not self.stacks:
            print('Stack empty')
            return
        item= self.stacks[-1].pop()
        #delete the stack if it becomes empty
        if not self.stacks[-1]:
            self.stacks.pop()
        return item

    def pop_at(self,stack_index):
        if stack_index<0 or stack_index>=len(self.stacks) or not self.stacks[stack_index]:
            print('Non existent stack')
            return
        item= self.stacks[stack_index].pop()
        if not self.stacks[stack_index]:
            self.stacks.pop(stack_index)
        return item

m = MultipleStacksOfPlates(3)

m.push(1)
m.push(2)
m.push(3)
m.push(4)
m.push(5)
m.push(6)
m.push(7)
m.push(8)
print(m)

m.pop()
print(m)
m.pop()
print(m)
m.pop()
print(m)
