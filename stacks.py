class Stack:
    def __init__(self):
        self.elem=[]

    def push(self, value):
        self.elem.append(value)

    def pop(self):
        if self.elem:
            return self.elem.pop()
        else:
            return None
    def size(self):
        return len(self.elem)

    def is_empty(self):
        return len(self.elem)==0 #method returns boolean

    def peek(self): #returns element from the top of the stack without deleting it
        if len(self.elem)==0:
            return None
        else:
            return self.elem[-1]

stack1=Stack()
stack1.push(3)
stack1.push("Name")
stack1.push(True)

print(stack1.size())
print(stack1.peek())