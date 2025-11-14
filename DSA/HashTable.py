class Hashtable:
    def __init__(self):
        self.max=1000000
        self.arr= [None for i in range(self.max)]

    def get_hash(self,key):
        h= 0
        for char in key:
            h += ord(char)
        return h / self.max 
    
    def __setitem__(self,key,value): # __setitem__ helps to set items like t["march"]=30
        h= self.get_hash(key)
        self.arr[h].append(value)
        return self.arr
    
    def __getitem__(self,key): #__getitem__ helps to get items for ex.  t["march"] will return 30
        return self.arr[self.get_hash(key)]

    def __delitem__(self,key):
        h= self.get_hash(key)
        self.arr[h]=None

t = Hashtable() 
t['march']= 30
t['March']= 30
print(t['march'])
del t['March']
print (t['March'])

