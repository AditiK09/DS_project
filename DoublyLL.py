class Node:
    def __init__(self, val = 0,prev = None, next = None):
        self.prev = prev
        self.next = next
        self.val = val

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def insertAtIndex(self,ind,data):
        if ind < 0 or ind > self.size:
            raise IndexError("Index out of bounds")
        newNode = Node(data)
        if ind == 0:
            if self.isEmpty():
                self.head = newNode
                self.tail = newNode
        
        else:
            curr = self.head
            count = 1         # bcz count & (index -1) will match this way
            
            while(count != (ind-1)):
                curr = curr.next
                count += 1
            temp = curr.next
            curr.next = newNode
            newNode.prev = curr
            newNode.next = temp
            temp.prev = newNode
        self.size += 1
        
    def deleteAtIndex(self,ind,data):
        if self.head is None:
            raise Exception("Empty LL")

        else:
            curr = self.head
            count = 0
            while count != ind:
                curr = curr.next
                count += 1
            temp = curr.prev
            temp.next = curr.next
            curr.next.prev = temp
            del curr
        self.size -= 1

    def append(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.head = newNode
            self.tail = newNode
        else:        
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1
        
    def prepend(self,data):
        newNode = Node(data)

        if self.is_empty():
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def merge(self,otherLL):
        if self.isEmpty():
            self.head = otherLL.head
            self.tail = otherLL.tail
        elif not otherLL.isEmpty():
            self.tail.next = otherLL.head
            otherLL.head.prev = self.tail
            self.tail = otherLL.tail
        self.size += otherLL.size

    def occurence(self,data):
        if self.isEmpty() is None:
            raise Exception("Empty LL")
        
        elif self.isEmpty() != None:
            curr = self.head
            count = 0
            while curr.data != data:
                curr = curr.next
                count += 1
            return count
        else:
            return -1
        
    def split(self, ind):
        if self.isEmpty() is None:
            raise Exception("Empty LL")
        else:
            secondLL = []
            curr = self.head
            count = 0
            while count < ind:
                curr = curr.next
                count += 1
            self.head = curr.next 
            self.tail = curr
    
    def interleaves(self,otherLL):
        if self.isEmpty() is None:
            return otherLL
        else:
            curr = self.head
            temp = self.head
            while curr is None and temp is None:
                if curr != temp:
                    curr = curr.next
                else:
                    curr.next = temp
                    temp.prev = curr
                    temp = temp.next
            
            if temp is None:
                curr.next = curr
            else:
                curr = temp.next

    def middleElement(self):
        if self.isEmpty() is None:
            raise Exception("Empty LL")
        
        while fast and fast.next:
            slow = self.head
            fast = self.head
            slow = slow.next
            fast = fast.next.next
        
        if self.size % 2 == 0:
            return (slow.val, slow.prev.val)
        else:
            return slow.val
