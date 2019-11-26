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
    #print("edges ", edges)

#TODO: Namen mit id speichern
#print " --- node attr names --- "
for node in nodes:
    #print (node['id'])
    if node.has_attr('attr.name'):
    	n_names.append({'id': node['id'], 'attr':node['attr.name']})

for edge in edges:
    #print (edge['id'])
    if edge.has_attr('attr.name'):
    	e_names.append({'id': edge['id'], 'attr':edge['attr.name']})

G = nx.read_graphml(path)
#access edge sttributes: https://networkx.github.io/documentation/stable/tutorial.html#accessing-edges-and-neighbors
#<data key="d21" xml:space="preserve"><![CDATA[Dem BMVg  ist die Bw nachgeordnet.]]></data>
for s in G.edges.data('key=d31'):
    print('****S***', s)
#access node with readable info
content_n0 = G.nodes['n0']  
print(content_n0)
#nx.draw(G)
#plt.show()
#print(G.nodes('n61'), G.edges('n61'))
#print(G.number_of_nodes(), G.number_of_edges())