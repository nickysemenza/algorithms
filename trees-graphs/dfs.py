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




#Depth First Search
class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []
        self.visited= False
    def addChild(self, data):
    	self.children.append(data)

a = Node(1)
b = Node(6)
# c = Node(7)
a.addChild(b)
# a.addChild(c)



pprint(dump(a))


print "S-------------------"
def search(node,findme):
	if(node is None):
		return
	if(node.data == findme):
		return node
	node.visited = True
	for each in node.children:
		if each.visited is False:
			search(each,findme)

print "E------------"

pprint(search(a,6))

