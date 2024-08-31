class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class SLL:
    def __init__(self,head=None):
        self.head = head
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0
            
    def insertAtIndex(self,ind, data):
        newNode = Node(data)

        if ind<0 and ind >= self.size:
            raise IndexError("Index out of bound")
        
        if ind == 0 :
            newNode.next = self.head
            self.head = newNode
            self.size += 1
            return
    
        temp = self.head
        for i in range (ind - 1):
            temp = temp.next
        
        curr = temp.next
        temp.next = newNode
        newNode.next = curr
        self.size += 1

    def deleteAtIndex (self,ind):
        if ind < 0 or ind >= self.size():
            raise IndexError("Index Out Of Bound")
       
        if ind == 0:  
            temp = self.head
            self.head = self.head.next
            del temp
            self.size -= 1
            return
        
        curr = self.head
        for i in range(ind - 1):
            curr = curr.next

        temp = curr.next
        curr.next = temp.next
        del temp
        self.size -= 1

    def append(self, data):
        newNode = Node(data)
        temp = self.head

        if self.head is None:
            self.head = newNode
        
        else:
            while temp.next:
                temp = temp.next
            temp.next = newNode
        self.size += 1  



    def prepend(self,data):
        newNode = Node(data)

        if self.is_empty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def merge(self,secondLL):
        if self.size == 0:
            self.head = secondLL.head

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = secondLL.head
        

    def interleaves(self,otherLL):
        if self.size == 0:
            self.head = otherLL.head
            return
        else:
            curr = self.head
            temp = otherLL.head
            list = []
            while curr or temp:
                if curr.data == temp.data:
                    curr= curr.next

                else:
                    temp = temp.next

            if temp is None:
                curr.next = curr
            else:
                curr = temp.next


    def middleElement(self):
        if self.head is None:
            raise Exception("Empty LL")
        else:
            slow = self.head
            fast = self.head
            while fast and fast.next :
                slow = slow.next
                fast = fast.next.next
                if self.size %2 == 0:
                    return (slow.val + slow.next.val)/2
                else :
                    return slow.val
                
    def occurenceIndex(self,data):
        if self.head is None:
            raise Exception("Empty LL")
        else:    
            trav = self.head
            count = 0
            while trav:
                if trav.val == data:
                    return count
                trav = trav.next
                count +=1
            return -1

    def split(self,ind):
        if self.head is None:
            raise Exception("Empty LL")
        if ind < 0 or ind >= self.size:
            raise IndexError("Index out of bound")
        else:
            second = []
            curr = self.head
            count = 0
            while count < ind:
                curr = curr.next
                count += 1
            second.head = curr.next
            curr.next = None

            
x = SLL()
print(x)
x.append(6)
x.prepend(3)
print(x.head.val)          
print(x.size)
print(x.is_empty())    
print(x.head.next.next)            
x.insertAtIndex(2,2) 
print(x.head.next.next.val)
x.middleElement
print(x)