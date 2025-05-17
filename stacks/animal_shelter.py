class AnimalShelter:
    def __init__(self):
        self.animal = []
    
    def enque(self,type):
        self.animal.append(type)
    
    def deque(self):
        if not self.animal:
            return None
        return self.animal.pop(0)
    
    def dequeue_cat(self):
        if not self.animal:
            return None
        for i,animal in enumerate(self.animal):
            if animal=='cat':
                return self.animal.pop(i)
        return None
    
    def dequeue_dog(self):
        if not self.animal:
            return None
        for i,animal in enumerate(self.animal):
            if animal=='dog':
                return self.animal.pop(i)
        return None
    
    def __str__(self):
        return "-".join(map(str,self.animal))

a=AnimalShelter()
a.enque("dog")
a.enque("dog")
a.enque("cat")
a.enque("dog")
a.enque("cat")
a.enque("cat")
a.enque("cat")

print(a.deque())
print(a)
print(a.dequeue_cat())
print(a)
print(a.dequeue_dog())
print(a)