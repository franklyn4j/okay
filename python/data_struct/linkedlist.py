#!/usr/bin/python

class node:
    def __init__(self,x=None):
        self.value,self.next = x,None
#            self.value = x
#            self.next = None

class list:
    def __init__(self):
        self.head = None

    def append(self,value):
        if (isinstance(value,node)):
            x=value
        else:
            x = node(value)

        if (self.head == None):
            self.head = x
        else:
            self.head,x.next = x,self.head
#            temp = self.head
#            self.head = x
#            x.next = temp
        return x

    def printf(self):
        pos = self.head
        while (pos != None):
            print pos.value,
            pos = pos.next
        print

    def remove(self,value):
        pos,pre = self.head,self.head
        #pos = self.head
        #pre = self.head
        while (pos != None):
            if (pos is value):
                break
            else:
                pre,pos = pos,pos.next
#                pre = pos
#                pos = pos.next
        if(pos == None):
            return False
        
        if(pre != pos):
            pre.next = pos.next
            del pos
        else:
            self.head = pos.next
            del pos
        return True



x = list()
y = node()
n = x.append(4096)
x.printf()
x.remove(n)
x.printf()
y.value = 1000
x.append(y)
x.append(1)
x.append(2)
a = x.append(10246)
x.append(3)
z = node(77)
t = x.append(1024)
m = x.append(100)
x.printf()
x.remove(y)
x.printf()
x.remove(t)
x.printf()
x.remove(m)
x.printf()
x.remove(a)
x.printf()
