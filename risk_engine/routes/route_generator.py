import osmnx as ox
def generate_routes(G, origin, destination, k=3):
    # Convert lat/lon → nearest graph nodes
    orig_node = ox.nearest_nodes(G, origin[1], origin[0])
    dest_node = ox.nearest_nodes(G, destination[1], destination[0])
    # k_shortest_paths returns a generator of node-lists
    routes_generator = ox.k_shortest_paths(
        G,
        orig_node,
        dest_node,
        k,
        weight="length"
    )
    # Convert generator → list
    routes = list(routes_generator)
    return routes
