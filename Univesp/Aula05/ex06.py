''' class Fila():
    def __init__(self):
        self.data = []

    def insert(self, x):
        self.data.append(x)

    def remove(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        
    def top(self):
        if len(self.data) > 0:
            return self.data[0]
        
    def empty(self):
        return not len(self.data) > 0
    
f = Fila()
'''
class S: 
    def __init__(self): 
        self.v = [ ] 
        self.i = -1 
 
    def push(self, x): 
        self.i += 1 
        self.v.insert(0, x) 
 
    def pop(self): 
        if(not self.empty()): 
            self.i -= 1 
            return self.v.pop() 
 
    def empty(self): 
        return self.i < 0 
 
 
s = S() 
for i in range(10): 
    s.push(i) 
 
while not s.empty(): 
    print(s.pop()) 
