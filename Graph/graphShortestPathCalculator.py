import sys
import collections

class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        self.adj = collections.defaultdict(list)
        self.length = n

        for node in edges:
            start, end, w = node
            self.adj[start].append([end, w])

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        # don't consider conflict between same edge d/t weight

        start, end, w = edge
        self.adj[start].append((end, w))

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int        
        """
        
        # incase of loop
        count = 0
        
        visited, stack = set(), []
        res = []
        
        stack.append([node1, 0]) # distance of source form source = 0
        
        while stack: # < length might be misleading ?
            temp1 = stack.pop()
            node, dist = temp1
            
            visited.add(node)
            
            if node == node2:
                res.append(dist)
                continue
            
            for lst in self.adj[node]:
                nei, dist2 = lst
                
                if nei not in visited:
                    stack.append([nei, dist + dist2])
                    
        if not res:
            return -1
                    
        return min(res)
        
g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])
print(g.shortestPath(0, 3)) # return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]) # We add an edge from node 1 to node 3, and we get the second diagram above.
print(g.shortestPath(0, 3)) # return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.  

import collections

class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        self.adj = collections.defaultdict(list)
        self.length = n

        for node in edges:
            start, end, w = node
            self.adj[start].append((end, w))  # Store edges as tuples

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        start, end, w = edge
        self.adj[start].append((end, w))

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        visited = set()
        stack = []
        res = []
        
        stack.append((node1, 0))  # distance from source to source is 0
        
        while stack:
            node, dist = stack.pop()
            
            if node in visited:
                continue
            
            visited.add(node)

            if node == node2:
                res.append(dist)
                continue
            
            for nei, dist2 in self.adj[node]:
                if nei not in visited:
                    stack.append((nei, dist + dist2))

        if not res:
            return -1            
                    
        return min(res)