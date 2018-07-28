class Node(object):
    def __init__(self,data=None):
        self.data = data
        self.next = None
class List:
    def __init__(self):
        """Constructor for List"""
        self.head = Node()
        self.length = 0
    def insert(self,pos,data):
        assert pos>=0 and pos <= self.length
        tmpPtr = self.head
        while pos>0:
            tmpPtr = tmpPtr.next
            pos -= 1
        new_node = Node()
        new_node.data = data
        # 将当前节点与后一个节点拆开，this_node指向后一个节点，前一个节点指向this_node
        new_node.next = tmpPtr.next
        tmpPtr.next = new_node
        self.length += 1
    def append(self,data):
        self.insert(self.length,data)
    def delete(self,pos):
        assert pos<self.length
        temPtr = self.head
        while pos>0:
            # 改变指针的指向
            temPtr = temPtr.next
            pos -= 1
        if temPtr is not None:
            del_next = temPtr.next
            temPtr.next = del_next.next
            self.length -= 1
    def update(self,pos,data):
        # self.delete(pos)
        # self.insert(pos,data)
        assert pos < self.length
        temPtr = self.head
        while pos > 0:
            # 改变指针的指向
            temPtr = temPtr.next
            pos -= 1
        if temPtr is not None:
            temPtr.data = data
    def foreach(self):
        tmpPtr = self.head.next
        while tmpPtr is not None:
            yield tmpPtr.data
            tmpPtr = tmpPtr.next
if __name__ == '__main__':
    l = List()
    l.append(1)
    l.append(2)
    l.append(3)
    i1 = iter(l)
    for i in i1:
        print(i)
    # for i in l.foreach():
    #     print(i)
    # l.delete(2)
    # for i in l.foreach():
    #     print(i)
    # print(l)
    # l.update(2,5)
    # for i in l.foreach():
    #     print(i)