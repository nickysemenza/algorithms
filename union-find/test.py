class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = self
        self.size = 1
from pprint import pprint
import copy
def dump(inp):
  obj = copy.copy(inp)	
  newobj=obj	
  if '__dict__' in dir(obj):
    newobj=obj.__dict__
    if ' object at ' in str(obj) and not newobj.has_key('__type__'):
      newobj['__type__']=str(obj)
    for attr in newobj:
      newobj[attr]=dump(newobj[attr])
  return newobj

def union(x,y):
  if(x.size < y.size):
    x.parent = y
    y.size = y.size + x.size
  else:
    y.parent = x
    x.size = x.size + y.size
def find(x):
  r = x
  while(r.parent is not r): # find the root
    r = r.parent
  z = x
  while(z.parent is not z): # path compression
    w = z
    z = z.parent
    w.parent = r

def show(node):
  print str(node.data) + " -> " + str(node.parent.data) + "(size: "+str(node.size)+")"
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
union(a,b)
union(a,c)
union(c,d)

show(a)
show(b)
show(c)
show(d)
print "-------------\n"
find(d)
show(a)
show(b)
show(c)
show(d)
# print(dump(b))