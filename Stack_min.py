class Stack:
    def __init__(self):
        self.elem=[]
        self.mins_stack=[]

    def push(self, value):
        self.elem.append(value)

        if self.mins_stack:
            if self.elem[-1]<self.mins_stack[-1]:
                self.mins_stack.append(value)
            else:
                self.mins_stack.append(self.mins_stack[-1])
        else:
            self.mins_stack.append(value)

    def pop(self):
        if self.elem:
            self.mins_stack.pop()
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

    def min_elem(self):
        return self.mins_stack[-1]

stack1=Stack()
stack1.push(3)
stack1.push(12)
stack1.push(7)
stack1.push(1)

print(stack1.min_elem())

stack1.pop()
print(stack1.min_elem())