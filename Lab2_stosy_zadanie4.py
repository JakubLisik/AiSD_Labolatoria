class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

def onp():
    i = input("Podaj kolejny znak/wartość w notacji postfiksowej: ")
    s = Stack()
    actions = ['+', '-', '*', '/', '^', '%']
    while i != '=':
        if actions.count(i) == 0:
            s.push(int(i))
        elif actions.count(i) == 1 and s.size()>=2:
            b = s.pop()
            a = s.pop()
            if i=='+': s.push(a+b)
            elif i=='-': s.push(a-b)
            elif i=='*': s.push(a*b)
            elif i=='/': s.push(a/b)
            elif i=='^': s.push(a**b)
            elif i=='%': s.push(a%b)
        # print(s.peek(), s.size())
        i = input("Podaj kolejny znak/wartość w notacji postfiksowej: ")
    return s.pop()
    

print(onp())