import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import bipartite
import os

G = nx.Graph()


def newGraph():
    G.clear()


def buildGraph(vertices, fileName, action, source=-1, target=-1):
    # print(action, vertices, fileName, action, source)
    G.clear()
    pos = nx.spring_layout(G)
    for i in range(0, len(vertices) - 1, 2):
        G.add_edge(vertices[i], vertices[i + 1], color="green", weight=7)

    colors = nx.get_edge_attributes(G, 'color').values()
    weights = nx.get_edge_attributes(G, 'weight').values()

    if action == "dfs":
        try:
            traverse = []
            T = nx.dfs_tree(G, source=source)
            for i in T.edges():
                traverse.append(i[0])
                traverse.append(i[1])
            ans = []
            for i in range(len(traverse) - 1):
                if traverse[i] != traverse[i + 1]:
                    ans.append(traverse[i])
            ans.append(traverse[len(traverse) - 1])
            traverse = ans

            nx.draw(G, with_labels=True, edge_color=colors, width=list(weights), node_size=1005)
            plt.savefig('./static/images/' + fileName)
            return traverse
        except:
            return "Error"

    if action == "bfs":

        try:
            traverse = []
            T = nx.bfs_tree(G, source=source)
            for i in T.edges():
                traverse.append(i[0])
                traverse.append(i[1])
            ans = []
            for i in range(len(traverse) - 1):
                if traverse[i] != traverse[i + 1]:
                    ans.append(traverse[i])
            ans.append(traverse[len(traverse) - 1])
            traverse = ans

            nx.draw(G, with_labels=True, edge_color=colors, width=list(weights), node_size=1005)
            plt.savefig('./static/images/' + fileName)
            return traverse
        except:
            return "Error"

    if action == "shortest path":

        try:
            traverse = []
            T = nx.bidirectional_shortest_path(G, source=source, target=target)
            print(T)
            for i in range(len(T) - 1):
                G.add_edge(T[i], T[i + 1], color='r', weight=10)
                traverse.append(T[i])
            traverse.append(T[len(T) - 1])
            print(traverse)
            colors = nx.get_edge_attributes(G, 'color').values()
            weights = nx.get_edge_attributes(G, 'weight').values()

            nx.draw(G, edge_color=colors, with_labels=True, width=list(weights), node_size=1005)
            plt.savefig('./static/images/' + fileName)
            return traverse

        except:
            return "Error"

    if action == "bipartite":

        if bipartite.is_bipartite(G):
            color = []
            T = bipartite.color(G)
            weight = []
            node_size = []
            for node in G:
                if T[node] == 0:
                    color.append('red')
                    weight.append(6)
                    node_size.append(1005)
                else:
                    color.append('green')
                    weight.append(6)
                    node_size.append(1005)

            nx.draw(G, node_color=color, width=weight, node_size=node_size, with_labels=True)
            plt.savefig('./static/images/' + fileName)
            return True
        else:
            return False

    if action == "cycle":
        try:
            traverse = []
            T = nx.find_cycle(G, orientation="original")
            for i in range(len(T)):
                G.add_edge(T[i][0], T[i][1], color='r', weight=10)
                traverse.append(T[i][0])
            print(traverse)
            colors = nx.get_edge_attributes(G, 'color').values()
            weights = nx.get_edge_attributes(G, 'weight').values()

            nx.draw(G, edge_color=colors, with_labels=True, width=list(weights), node_size=1005)
            plt.savefig('./static/images/' + fileName)
            return traverse

        except:
            return "Not Contain A Cycle"
