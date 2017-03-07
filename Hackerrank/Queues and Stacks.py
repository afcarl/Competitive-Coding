class Solution:
    def __init__(self):
        self.items=[]
        self.items2=[]
    def enqueueCharacter(self,item):
        self.items.insert(0,item)
#       print(self.items)
    def dequeueCharacter(self):
#        print(self.items[len(self.items)-1])
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items==[]
    def pushCharacter(self,item):
        self.items2.append(item)
#        print(self.items2)
    def popCharacter(self):
#        print(self.items2[len(self.items)-1])
        return self.items2.pop()
