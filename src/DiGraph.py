import copy

from GraphInterface import GraphInterface
from Node import Node

from src.Edges import Edges


class DiGraph(GraphInterface):

    def __init__(self):
        self.numOfNodes = 0
        self.numOfEdges = 0
        self.Mc = 0
        self.Nodes = []
        self.inEdges = []
        self.outEdges = []

    def v_size(self) -> int:
        return self.numOfNodes

    def e_size(self) -> int:
        return self.numOfEdges

    def get_all_v(self) -> dict:
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        list={}
        for i in range(len(self.inEdges)):
            if self.inEdges[i].getsrc == id1:
                list[self.inEdges[i].getsrc]=self.inEdges[i].get_weight
        return list

    def all_out_edges_of_node(self, id1: int) -> dict:
        list = {}
        for i in range(len(self.inEdges)):
            if self.inEdges[i].getdest == id1:
                list[self.inEdges[i].getsrc] = self.inEdges[i].get_weight
        return list

    def get_mc(self) -> int:
        return self.Mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        for i in range(len(self.inEdges)):
            if self.inEdges[i].getsrc!=id1 or self.inEdges[i].getdest!=id2:
             x: bool =True
            if x:
                edge = Edges(id1,id2,weight)
                self.inEdges.__add__(edge)
                self.Mc = self.Mc + 1
                self.numOfEdges = self.numOfEdges + 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id not in self.Nodes:
            node = Node(node_id, pos)
            self.Nodes.insert(node_id,node)
            self.Mc = self.Mc+1
            self.numOfNodes = self.numOfNodes+1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        if self.Nodes.__contains__(node_id):
            for i in range(len(self.inEdges)):
                if self.inEdges[i].getsrc == node_id or self.inEdges[i].getdest == node_id:
                    self.inEdges.pop(i)
                    self.Mc = self.Mc + 1
            if self.outEdges[i].getsrc == node_id or self.outEdges[i].getdest == node_id:
                self.outEdges.pop(i)
        self.Mc = self.Mc + 1
        self.numOfNodes = self.numOfNodes-1
        return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:

        if len(self.Nodes) !=0:
            for i in range(len(self.inEdges)):
                if self.inEdges[i].getsrc == node_id1 and self.inEdges[i].getdest == node_id2:
                   self.inEdges.pop(i)
                   self.Mc = self.Mc + 1
                   return True

        return False

