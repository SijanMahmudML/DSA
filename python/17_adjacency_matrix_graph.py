""" Adjacency Matrix Implementation of Graph """

class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_matrix= [[0]*vno for e in range(vno)]
    def add_edge(self,u,v,weight=1):
        if 0<= u <self.vertex_count and 0<= v < self.vertex_count :
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("invalid vertex")
    def remove_edge(self,u,v):
        if 0<= u < self.vertex_count and 0<= v < self.vertex_count :
            self.adj_matrix[u][v]=0
            self.adj_matrix[v][u]=0
        else:
            print("invalid vertex")
    def has_edge(self,u,v):
        if 0<= u < self.vertex_count and 0<= v < self.vertex_count :
            return self.adj_matrix[u][v]!=0
        else:
            print("invalid vertex")
            return False
    def print_adj_matrix(self):
        for row_list in self.adj_matrix:
            print(" ".join(map(str,row_list)))
        
""" Driver Code """

g1= Graph(5)
g1.add_edge(0,1)
g1.add_edge(2,1)
g1.add_edge(1,3)
g1.add_edge(4,3)
g1.add_edge(4,2)

g1.print_adj_matrix()
    

