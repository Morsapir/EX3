from unittest import TestCase
from DiGraph import *
from DiGraph import DiGraph
from Edges import Edges

pos1 = (1, 1, 1)
pos2 = (2, 2, 2)
pos3 = (3, 3, 3)
pos4 = (4, 4, 4)
pos5 = (5, 5, 5)
pos6 = (6, 6, 6)
edge1 = Edges(1, 2, 0)
edge2 = Edges(2, 3, 0)
edge3 = Edges(3, 4, 0)
edge4 = Edges(4, 5, 0)
edge5 = Edges(5, 6, 0)
edge6 = Edges(6, 1, 0)
graph = DiGraph()
graph.add_node(1, pos1)
graph.add_node(2, pos2)
graph.add_node(3, pos3)
graph.add_node(4, pos4)
graph.add_node(5, pos5)
graph.add_node(6, pos6)


class testDiGraph(TestCase):

    def test_v_size(self):
        self.assertTrue(graph.numOfNodes == 6)

    def test_e_size(self):
        self.assertTrue(graph.numOfEdges == 6)

    def test_Mc(self):
        self.assertTrue(graph.Mc == 6)

    def test_add_edge(self):
        a = graph.e_size()
        graph.add_edge(1, 5, 0)
        b = graph.e_size()
        self.assertTrue(a + 1 == b)

    def test_add_node(self):
        pos7 = (7, 7, 7)
        graph.add_node(7, pos7)
        b = graph.v_size()
        self.assertTrue(7 == b)

    def test_remove_node(self):
        a = graph.v_size()
        graph.remove_node(6)
        b = graph.v_size()
        self.assertTrue(a == b+1)

    def test_remove_edge(self):
        a = graph.v_size()
        graph.remove_edge(1, 2)
        b = graph.v_size()
        self.assertTrue(a - 1 == b)
