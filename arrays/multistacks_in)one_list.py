class MultiStack:
    def __init__(self,size,no_of_stacks=3):
        self.no_of_stacks =no_of_stacks
        self.stack_size=size
        self.custom_stacks=[0]*(size*self.no_of_stacks)
        self.track_stack_sizes=[0]* self.no_of_stacks
    
    def is_full(self, stack_number):
        return self.track_stack_sizes[stack_number]==self.stack_size
    
    def is_empty(self,stack_number):
        return self.track_stack_sizes[stack_number]==0
    
    def get_top_element_index(self,stack_number):
        offset = stack_number * self.stack_size
        return offset+ self.track_stack_sizes[stack_number]

    def push(self,value,stack_number):
        if self.is_full(stack_number):
            print(f'stack number {stack_number} is full.')
            return
        self.custom_stacks[self.get_top_element_index(stack_number)]=value
        self.track_stack_sizes[stack_number]+=1
    
    def pop(self,stack_number):
        if self.is_empty(stack_number):
            print(f'stack number {stack_number} is empty.')
            return
        index =self.get_top_element_index(stack_number)-1
        print(f'{index=}')
        item =self.custom_stacks[index]
        self.custom_stacks[index]=None
        self.track_stack_sizes[stack_number]-=1
        return item
    
    def __str__(self):
        return "-".join(map(str,self.custom_stacks))

m = MultiStack(3)
m.push(1,0)
m.push(4,1)
m.push(7,2)
m.push(8,2)
m.push(9,2)

print(m.pop(2))
print(m.pop(2))


