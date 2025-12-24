import osmnx as ox
def load_graph(place, mode = 'drive'):
    graph = ox.graph_from_place(place, network_type=mode)
    return graph