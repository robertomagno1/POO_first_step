"""This file contains an implementation of Dijkstra's algorithm
and a number of supporting functions for running the tests.
The results of Dijkstra's algorithm are compared with the results
of a brute force algorithm that explores all possible paths between
the source and the destination and then selects the one with the lowest
weight."""

import sys

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

nodes_positions = {}


#support function
"""plot a graph"""
def plot_graph(ad_matrix, unvisited_nodes, previous_nodes, title):
    node_color_list = []
    for i in range(len(ad_matrix)):
        if i in unvisited_nodes:
            node_color_list.append("#1f78b4")
        else:
            node_color_list.append("#ffff00")
    edge_color_list=[]
    graph = nx.from_numpy_array(ad_matrix)
    for e in nx.edges(graph):
        key1 = previous_nodes.get(e[0])
        key2 = previous_nodes.get(e[1])
        if key1 is not None and key1 == e[1] or key2 is not None and key2 == e[0]:
            edge_color_list.append("#008a00")
        else:
            edge_color_list.append("#a8a8a8")

    global nodes_positions
    if len(nodes_positions) == 0:
        nodes_positions=nx.spring_layout(graph)
    plt.title(title)
    nx.draw_networkx(graph, nodes_positions, node_color=node_color_list, edge_color=edge_color_list, node_size = 500, width = 1.5)
    nx.draw_networkx_edge_labels(graph, nodes_positions, font_size=8, rotate=False, clip_on=False)
    plt.savefig('graph.png')
    #manager = plt.get_current_fig_manager()
    #manager.window.maximize()
    plt.show()

#support function
"""print the best paths and the weights"""
def print_paths(previous_nodes, weights, start_node, size):

    for target_node in range(size):
        if target_node == start_node:
            continue
        path = []
        node = target_node
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        path.append(start_node)

        rev_path = []
        for e in reversed(path):
            rev_path.append(e)
        print("Best path from node", start_node,  "to node", target_node, "(weight: ", weights[target_node],")", rev_path)

#support function
"""generate a random graph"""
def generate_random_graph(size):
    prob_no_edge = 0.6
    weights = np.arange(10)
    prob = (1 - prob_no_edge) / (len(weights) - 1)
    probs = [prob for i in range(len(weights) - 1)]
    probs.insert(0, prob_no_edge)
    retry = True
    while retry:
        ad_matrix = np.random.choice(weights, size=(size, size), p=probs)
        np.fill_diagonal(ad_matrix, 0)
        ad_matrix = (ad_matrix + ad_matrix.T) / 2
        # check if the graph is connected
        retry = False
        for i in range(size):
            if sum(ad_matrix[i]) == 0:
                retry = True
                break

    return ad_matrix

#support function
"""this function is used by the brute force algorithm"""
def find_all_paths(ad_matrix, node_list, visited_nodes, start_node, end_node, current_path, current_path_weight, all_paths, all_path_weights):

    if len(current_path)==0:
        current_path.append(start_node)
    if start_node == end_node:
        all_paths.append(current_path.copy())
        all_path_weights.append(current_path_weight)
        return

    visited_nodes.append(start_node)

    for node in range(len(ad_matrix)):
        if node not in visited_nodes:
            if ad_matrix[node, start_node]:
                # the node is a neighbor
                current_path.append(node)
                current_path_weight+= ad_matrix[node, start_node]
                find_all_paths(ad_matrix, node_list, visited_nodes, node, end_node, current_path, current_path_weight, all_paths, all_path_weights)
                current_path.remove(node)
                current_path_weight -= ad_matrix[node, start_node]

    visited_nodes.remove(start_node)

    return

#support function
"""brute force algorithm"""
def brute_force(graph_ad_matrix, start_node):
    for end_node in range(len(graph_ad_matrix)):
        if start_node!= end_node:
            all_paths = []
            all_path_weights = []
            find_all_paths(graph_ad_matrix, range(number_of_nodes), [], start_node, end_node, [], 0, all_paths, all_path_weights)
            i = 0
            best_path=None
            best_path_weight = float('inf')
            for l in all_paths:
                print("Path weight:", all_path_weights[i], "\tpath", l)
                if best_path_weight>all_path_weights[i]:
                    best_path=i
                    best_path_weight=all_path_weights[i]
                i += 1

            print("Best path from node", start_node,  "to node", end_node, "(weight:", best_path_weight,")", all_paths[best_path])



"""Dijkstra's algorithm"""
def dijkstra(ad_matrix, start_node, plot):
    n = len(ad_matrix)
    unvisited_nodes = set(range(n))
    previous_nodes = {}
    path_weights = np.full(n,float('inf'))
    path_weights[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        # Iterate over nodes in unvisited_nodes
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif path_weights[node] < path_weights[current_min_node]:
                current_min_node = node

        unvisited_nodes.remove(current_min_node)

        for node in unvisited_nodes:
            if ad_matrix[node,current_min_node]:
                # the node is a neighbor
                weight = path_weights[current_min_node]+ad_matrix[node,current_min_node]
                if weight < path_weights[node]:
                    path_weights[node]=weight
                    previous_nodes[node]=current_min_node
        if len(unvisited_nodes) >0:
            print("Unvisited nodes: ", unvisited_nodes)

        if plot:
           plot_graph(ad_matrix, unvisited_nodes, previous_nodes, "Dijkstra Algorithm - Visited nodes:" + str(n - len(unvisited_nodes)))

    return path_weights, previous_nodes


"""---Entry point---"""
# initialize variables
number_of_nodes = 5
start_node = 0
#remove the following comment to repeat always the same execution
#np.random.seed(1)
graph_ad_matrix = generate_random_graph(number_of_nodes)
#plot graph
plot_graph(graph_ad_matrix, range(number_of_nodes), {},  "Graph")
#run dijkstra algorithm
print("\nRunning Dijkstra algorithm...")
path_weights, previous_nodes=dijkstra(graph_ad_matrix, start_node, True)
# print paths and weights
print_paths(previous_nodes, path_weights, start_node, number_of_nodes)
#plot paths
plot_graph(graph_ad_matrix,range(number_of_nodes), previous_nodes, "Dijkstra Algorithm - Shortest paths")
print("\nRunning brute force algorithm...")
brute_force(graph_ad_matrix, start_node)
