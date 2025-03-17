from pyvis.network import Network
import networkx as nx
import pyvis.network as net

def plot_knowledge_graph(input_data, mode='show'):
    # Create a directed graph
    knowledge_graph = nx.DiGraph()
    nt = net.Network(notebook=True)

    # Add nodes from the input data
    for node in input_data["nodes"]:
        knowledge_graph.add_node(node["id"], type=node["type"], description=node["description"])

    # Add edges from the input data
    for edge in input_data["edges"]:
        knowledge_graph.add_edge(edge["source"], edge["target"], label=edge["relationship"])

    # Determine node depth and assign colors accordingly
    node_colors = {}
    for node in knowledge_graph.nodes():
        ancestors = nx.ancestors(knowledge_graph, node)
        depth = len(ancestors)
        if depth == 0:
            node_colors[node] = "lightgreen"  # Root parent nodes
        elif depth == 1:
            node_colors[node] = "lightblue"  # Children nodes
        else:
            node_colors[node] = "pink"  # Grandchildren nodes

    # Create a pyvis graph

    pyvis_graph = Network(
        height="511px",
        width="631px",
        directed=True,
        notebook=True,
        bgcolor="#333333",  # Set the background color here (e.g., light gray)
    )
    # Add nodes to the pyvis graph with colors and descriptions
    for node_id, node_data in knowledge_graph.nodes(data=True):
        pyvis_graph.add_node(

            node_id,
            label=node_id,
            color=node_colors[node_id],
            title=node_data["description"], 
            font={"color":"#dce4ee"}
             # Add description as a tooltip
        )

    # Add edges to the pyvis graph
    for edge in knowledge_graph.edges(data=True):
        pyvis_graph.add_edge(edge[0], edge[1], title=edge[2]["label"],font={"color":"#dce4ee"})

    # Layout the graph


    # Show or save the visualization
    if mode == 'show':
        pyvis_graph.show("nx.html")
    elif mode=='save':
        pyvis_graph.save_graph(".\\nx.html")
