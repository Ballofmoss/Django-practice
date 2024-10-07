
class Node:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return self.val
        



class LinkedList:
    start = None
    end = None
    
    
    def __end(self):
        last = self.start
        while last.next:
            # print(last.val)
            last = last.next
        
    
    def append(self, val):
        node = Node(val=val)
        
        if not self.start:
            self.start = node
            return
        last = self.start
        while last.next:
            last = last.next
            print(last.val)
        # print(last.val)
        last.next, self.end = node,node 
    def count(self):
        self.start = self.start.next
        last = self.start
        count = 0
        while last:
            count += 1
            last = last.next
        print('Длина массива:', count)
        return count
    def foundByArg(self, arg):
        count = 0
        last = self.start
        while last:
            count += 1
            if last.val == arg:
                print(last.val)
                return last, count
            last = last.next
    def takeOrder(self):
        order = self.start
        self.start = self.start.next
        return order
        
        
        


node = LinkedList()

node.append('шаурма')
node.append('пиво')
node.append('пицца')
node.append('картофель')
node.append('котлета')
node.count()
# print(node.takeOrder())

