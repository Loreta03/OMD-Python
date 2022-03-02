class Stack(list):
    def Stack(self):
        self=[]
    def isEmpty(self):
        if len(self)==0:
            return True
        return False
    def push(self, item):
        self.append(item)
    def peek(self):
        return self[len(self)-1]
    def size(self):
        return len(self)

def IsOpenBracket(item):
    if item == '(' or item == '{' or item == '[':
        return True
    return False
def AreOppositeChar(item1, item2):
    if item1 == '(' and item2==')':
        return True
    elif item1 == '{' and item2 == '}':
        return True
    elif item1 == '[' and item2 == ']':
        return True
    else: return False
    
exp = input("Exp = ")
s = Stack()
balanced = True
for i in exp:
    try:
        if IsOpenBracket(i)==True:
            s.push(i)
        else:
            if AreOppositeChar(s.peek(), i) == True:
                s.pop()
            else:
                balanced = False
                break
    except:
        balanced = False
        
if balanced == True:
    print("Balanced")
else:
    print("Not balanced")
        


    
    
            
