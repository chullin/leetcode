Max = 10
Stack = [None] * Max
Top = 0

def isFull():
    global Top
    global Max
    if(Top > Max):
        return True
    else:
        return False
    
def push(new_data):
    global Top
    if(isFull() != True):
        Stack[Top] = new_data   # push data in stack
        Top = Top + 1           # The top has to be moved up  
    
def isEmpty():
    global Top
    if(Top == 0):
        return True
    else:
        return False

def pop():
    global Top
    global Max
    if(isEmpty() != True):
        print(f"頂部資料為:{Stack[Top-1]}")
        Stack.pop()
        Top = Top - 1

push(10)
push(15)
push(100)
pop()
pop()
pop()



'''
$ python stack.py 
頂部資料為:100
頂部資料為:15
頂部資料為:10

'''