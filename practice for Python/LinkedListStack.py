'''
無需設計 isFull 這個函數，因為鏈結串列中並不會有滿堆疊的情況發生
isEmpty、push、pop
'''
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

top_linked_list = None

def LinkedisEmpty():
    if top_linked_list is None:
        return True

def LinkedPush(data):
    global top_linked_list
    new_data = Node(data)
    new_data.next = top_linked_list 
    top_linked_list = new_data

def LinedPop():
    global top_linked_list
    if not LinkedisEmpty():
        print(f"The top data is = {top_linked_list.data}")
        top_linked_list = top_linked_list.next
    else:
        print("Stack is empty")

# Push data to the stack
for i in [100, 15, 10]:
    LinkedPush(i)

# Pop data from the stack
for _ in range(3):
    LinedPop()


'''
1. 初始狀態：
top_linked_list = None

2. 第一次 LinkedPush(100)：
top_linked_list = Node(100)
此時，top_linked_list 指向一個節點，該節點的 data 為 100，next 為 None。

3. 第二次 LinkedPush(15)：
top_linked_list = Node(15) -> Node(100)
新的節點 (15) 被創建，其 next 指向之前的節點 (100)。



$ python LinkedListStack.py
The top data is = 10
The top data is = 15
The top data is = 100
'''