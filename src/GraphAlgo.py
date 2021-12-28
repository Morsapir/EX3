import json
import os
import sys
from math import inf
from random import random
from typing import List

from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch

from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
import heapq
from src import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        graph = DiGraph()
        Edges: list
        Nodes: list
        try:
            with open(file_name, 'r') as f:
                r = json.load(f)
                Edges = r["Edges"]
                Nodes = r["Nodes"]

                for node in Nodes:
                    try:
                        out = node["pos"].split(',')
                        pos = (float(out[0]), float(out[1]), float(out[2]))
                    except Exception:
                        pointX = random.randint(5, 50)
                        pointY = random.randint(5, 50)
                        pos = (pointX, pointY, 0.0)

                    graph.add_node(node["id"], pos)

                for edge in Edges:
                    graph.add_edge(edge["src"], edge["dest"], edge["w"])
                self.graph = graph
                return True
        except():
            return False

    def save_to_json(self, file_name: str) -> bool:
        output = {"Edges": [], "Nodes": []}
        for node in self.graph.nodesMap.values():
            dict1 = {"id": node.id}
            if node.pos is not None:
                dict1["pos"] = node.pos
            output["Nodes"].append(dict1)

            for edge in self.graph.all_out_edges_of_node(node.id):
                dict2 = {"src": node.id, "w": self.graph.all_out_edges_of_node(node.id)[edge], "dest": edge}
                output["Edges"].append(dict2)
        try:
            with open(file_name, "w") as f:
                f.write(json.dumps(output))
                return True
        except():
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        list = []

        for node in len(self.graph.Nodes):
            node.length = sys.maxsize
            node.previous = None
            list.append(node)
        self.graph.Nodes.get(id1).length = 0
        heapq.heapify(list)

        while not len(list) == 0:
            now = heapq.heappop(list)
            now1 = self.graph.all_out_edges_of_node(now.id)
            for x in now1.values():
                dist = now.length + x[1]
                if dist < self.graph.Nodes.get(x[0]).length:
                    self.graph.Nodes.get(x[0]).length = dist
                    self.graph.Nodes.get(x[0]).previous = now.id
                    heapq.heapify(list)

        listNodeId = []
        while not id2 == None:
            listNodeId.insert(0, id2)
            id2 = self.graph.Nodes.get(id2).previous

        if self.graph.Nodes.get(id2).length == sys.maxsize:
            return inf, []

        return self.graph.Nodes.get(id2).length, listNodeId

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if node_lst is None:
            return [], -1
        if len(node_lst) == 1:
            return [node_lst, 0]
        output = []
        dest = 0
        for runner in range(len(node_lst)):
            first = node_lst[runner]
            second = node_lst[runner + 1]
            current = self.shortest_path(first, second)[1]
            dest = dest + self.shortest_path(first, second)[0]

            for i in current:
                if not output.__contains__(i):
                    output.append(i)
        return output, dest

    def centerPoint(self) -> (int, float):
        x = sys.maxsize
        id1 = -1
        x1 = -1

        for node in self.graph.Nodes.values():
            self.shortest_path(node.id, 0)

            for node2 in self.graph.Nodes.values():
                if x1 < node2.length:
                    x1 = node2.length

            if x1 < x:
                x = x1
                id1 = node.id
            x1 = -1

        return id1, x

    def plot_graph(self) -> None:
      