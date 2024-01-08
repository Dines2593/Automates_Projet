import networkx as nx
import matplotlib.pyplot as plt

def draw_automaton(automaton):
    G = nx.DiGraph()

    # Add states and transitions
    for state in automaton.states:
        G.add_node(state.name, isInitial=state.isInitial, isFinal=state.isFinal)
        for symbol, transitions in state.transitions.items():
            for target_state in transitions:
                G.add_edge(state.name, target_state, label=symbol)

    # Set node and edge attributes for visualization
    node_labels = {node: node for node in G.nodes}
    node_colors = ["green" if G.nodes[node]["isInitial"] else "red" if G.nodes[node]["isFinal"] else "white" for node in G.nodes]
    edge_labels = {(source, target): label for source, target, label in G.edges(data="label")}

    # Draw the graph
    pos = nx.spring_layout(G)  # You can use different layouts based on your preference
    nx.draw_networkx_nodes(G, pos, node_color=node_colors)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()

# Draw the result_automate

