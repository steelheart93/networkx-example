import networkx as nx
import matplotlib.pyplot as plt


# https://networkx.org/documentation/stable/reference/classes/generated/networkx.DiGraph.add_edge.html?highlight=add_edge#networkx.DiGraph.add_edge
# Note: The nodes u and v will be automatically added if they are not already in the graph.
def agregar_arista(G, u, v, w=1, di=True):
    G.add_edge(u, v, weight=w)

    # Si el grafo no es dirigido
    if not di:
        # Agrego la arista 
        G.add_edge(v, u, weight=w)


if __name__ == '__main__':
    # Instantiate the DiGraph
    G = nx.DiGraph()

    # Add node/edge pairs
    agregar_arista(G, "A", "B", 5, False)

    # Draw the networks
    nx.draw(G, with_labels=True)
    plt.show()
