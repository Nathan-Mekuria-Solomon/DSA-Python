class Queue:
    def __init__(self):
        self.arr = []
        self.size = 0
        
    def enQueue(self, element):
        self.arr.append(element)
        self.size  += 1
        
    def deQueue(self):
        temp = self.arr[0]
        self.arr.remove(temp)
        self.size -= 1
        return temp

class Vertix:
    def __init__(self, node):
        self.id = node
        self.adjacency = {} # adjacent dictionary
        self.distance = -1
        self.visited = False
        self.previous = None
        
    def addNeighbor(self, neighbor, weight= 0):
        self.adjacency[neighbor] = weight
        
    def getConnections(self):
        return self.adjacency.keys()
    
    def setVertixId(self, id):
        self.id = id
        
    def getVertixId(self):
        return self.id
    
    def getWeight(self, neighbor):
        return self.adjacency[neighbor]
    
    def setDistance(self, distance):
        self.distance = distance
        
    def getDistance(self):
        return self.distance
    
    def setPrevious(self, prev):
        self.previous = prev
        
    def setVisited(self):
        self.visited = True
        
    def __str__(self):
        return str(self.id),                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     


class Graph:
    def __init__(self):
        self.vertixDict = {}
        self.num = 0
        
    def __iter__(self): # idk the purpose
        return iter(self.vertixDict.values())
    
    def addVertix(self, node):
        self.num += 1
        self.vertixDict[node] = Vertix(node)
        
    def getVertix(self, node):
        if node in self.vertixDict:
            return self.vertixDict[node]
        else:
            return None
        
    def addEdge(self, start, end, weight= 0):
        if start not in self.vertixDict:
            self.addVertix(start)
            
        if end not in self.vertixDict:
            self.addVertix(end)
            
        self.vertixDict[start].addNeighbor(self.vertixDict[end], weight)
        self.vertixDict[end].addNeighbor(self.vertixDict[start], weight) # only undirectional
        
    def getVertices(self):
        return self.vertixDict.keys()
    
    def getV(self):
        return self.vertixDict.values()
    
    def getEdges(self):
        edges = []
        
        for vtx in self.vertixDict:
            vtx = self.vertixDict[vtx]
            for nbr in vtx.getConnections():
                v = vtx.getVertixId()
                n = nbr.getVertixId()
                edges.append((v, n, vtx.getWeight(nbr)))
                
        return edges
 
def shortest_path(graph, s):
    start = graph.getVertix(s)
    start.distance = 0
    start.previous = None
    que = Queue()
    que.enQueue(start)
    
    while que.size > 0:
        curr = que.deQueue()
        
        for nbr in curr.getConnections():
            if nbr.distance == -1:
                nbr.distance = curr.distance + 1
                nbr.previous = curr
                que.enQueue(nbr)
                
    for vrt in graph.getV():
        print(f"the distance b/n {start} and {vrt.getVertixId()} is {vrt.distance}")
    
if __name__ == "__main__":
    graph = Graph()
    graph.addVertix('a')
    graph.addVertix('b')
    graph.addVertix('c')
    graph.addVertix('d')
    graph.addVertix('e')
    
    graph.addEdge('a', 'b', 4)
    graph.addEdge('a', 'c', 1)
    graph.addEdge('c', 'b', 2)
    graph.addEdge('b', 'e', 4)
    graph.addEdge('c', 'd', 4)
    graph.addEdge('d', 'e', 4)
    
    shortest_path(graph, 'b')
    
    