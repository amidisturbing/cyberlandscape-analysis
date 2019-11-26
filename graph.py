import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup



path = "../cyberlandscape/data.graphml"

with open(path) as file:
    soup = BeautifulSoup(file, "lxml")

    nodes = soup.findAll("key",{"for":"node"})
    edges = soup.findAll("key",{"for":"edge"})
    print("edges ", edges)

#print " --- edge attr names --- "
for edge in edges:
    print (edge['id'])
    if edge.has_attr('attr.name'):
    	print (edge['attr.name'])

G =nx.read_graphml(path)
#nx.draw(G)
#plt.show()
#print(G.nodes(), G.edges)
print(G.number_of_nodes(), G.number_of_edges())
