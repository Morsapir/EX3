*Contributers: Mor Sapir * * in this project I'm assigned to implement a Directed Weighted Graph, * and run algorithms on it. and asked to build a GUI were you could load graphs using a JSON file. * in this project I was asked to be able to generate large graphs up to 1,000,000 Nodes and 10,000,000 Edges * * * * class- * edgeData interface EdgeData-

* Node-
 def getid(self) -> int: return the node id
 def getpos(self) -> tuple: return pos
 
* edges-
  def get_src(self): return src
  def get_dest(self): return dest
  def get_weight(self): return weight

* DiGraph interface GraphInterface
    def v_size(self) -> int:     Returns the number of vertices in this grap
    def e_size(self) -> int:   Returns the number of edges in this graph
    def get_all_v(self) -> dict: return a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data)
    def all_in_edges_of_node(self, id1: int) -> dict: return a dictionary of all the nodes connected to (into) node_id ,
                                                       each node is represented using a pair (other_node_id, weight) 
    def all_out_edges_of_node(self, id1: int) -> dict: return a dictionary of all the nodes connected from node_id , each node is represented using a pair
                                                       (other_node_id, weight)
    def get_mc(self) -> int:  Returns the current version of this graph,  on every change in the graph state - the MC should be increased
    def add_edge(self, id1: int, id2: int, weight: float) -> bool: @return: True if the edge was added successfully, False o.w.
                                                             Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
    def add_node(self, node_id: int, pos: tuple = None) -> bool:  @return: True if the node was added successfully, False o.w.
                                                                   Note: if the node id already exists the node will not be added
    def remove_node(self, node_id: int) -> bool: @return: True if the node was removed successfully, False o.w.
                                                 Note: if the node id does not exists the function will do nothing
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:  @return: True if the edge was removed successfully, False o.w.
                                                                  Note: If such an edge does not exists the function will do nothing

 * GraphAlgo interface GraphAlgoInterface-
     def get_graph(self) -> GraphInterface: return: the directed graph on which the algorithm works on.
     def load_from_json(self, file_name: str) -> bool: @returns True if the loading was successful, False o.w.
     def save_to_json(self, file_name: str) -> bool:  @return: True if the save was successful, False o.w.
     def shortest_path(self, id1: int, id2: int) -> (float, list): @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])

    def TSP(self, node_lst: List[int]) -> (List[int], float): :return: A list of the nodes id's in the path, and the overall distance
    def centerPoint(self) -> (int, float): return: The nodes id, min-maximum distance
    def plot_graph(self) -> None:  Plots the graph.
       
