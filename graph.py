import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup



path = "../cyberlandscape/data.graphml"
n_names = []
e_names = []

with open(path) as file:
    soup = BeautifulSoup(file, "lxml")

    nodes = soup.findAll("key",{"for":"node"})
    edges = soup.findAll("key",{"for":"edge"})
    print("edges ", edges)

#TODO: Namen mit id speichern
#print " --- node attr names --- "
for node in nodes:
    #print (node['id'])
    if node.has_attr('attr.name'):
    	n_names.append({'id': node['id'], 'attr':node['attr.name']})

for edge in edges:
    print (edge['id'])
    if edge.has_attr('attr.name'):
    	e_names.append({'id': edge['id'], 'attr':edge['attr.name']})

print (n_names, e_names)
G = nx.read_graphml(path)
#nx.draw(G)
#plt.show()
#print(G.nodes(), G.edges)
#print(G.number_of_nodes(), G.number_of_edges())