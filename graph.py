import networkx as nx
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import json

path = "../cyberlandscape/data.graphml"

#START get  Edge Attribute Fields with id----------------NEEDED?
e_attr_types = []

with open(path) as file:
    soup = BeautifulSoup(file, "lxml")
    edges = soup.findAll("key",{"for":"edge"})

for edge in edges:
    #print (edge['id'])
    if edge.has_attr('attr.name'):
        e_attr_types.append({'id': edge['id'], 'attr':edge['attr.name']})
#STOP get Node Attribute Fields and Edge Attribute Fields with id------------------------

G = nx.read_graphml(path)
edges = G.edges
nodes = G.nodes
nodes_data = nodes.data()
#node ids
nodes_values = nodes.values()
edges_data =  edges.data()
#edge ids
edges_values = edges.values()

def get_subgraph_by_edge_attr(attr):
    #grouping edges by edge attribute
    edges_by_key = []
    for e, datadict in G.edges.items():
        #example: attr = 'oversight.legal'
        key = attr
        if key in datadict:
            #print('datadict by key ;;;;;;;;;;;;;;', datadict[key])
            edges_by_key.append(e)
    G_e_key = G.edge_subgraph(edges_by_key)
    #print(G_e_key.edges.data())
    return G_e_key

#calculate grid for mathplot
e_attr_types_count = len(e_attr_types)
r_count = e_attr_types_count / 2
c_count = e_attr_types_count - r_count
#p=1 left most column
p = 0
count = 0

#get subgraphs for all edge attr
for item in e_attr_types:
    (key, val) = item.items()
    current_edge_attr_type =val[1]
    current_graph =  get_subgraph_by_edge_attr(current_edge_attr_type)

    #print("test+++++++++++++++++++++++++++++", r,c,p)

#data to JSON to use with D3
data1 = json_graph.node_link_data(G)
#print(data1)
s1 = json.dumps(data1)
#print(s1)

pos = nx.spectral_layout(G)
nx.draw(G, with_labels=True, font_weight='bold')
#print('DEBUG: ---',edges_data)
plt.show()
#print(G.number_of_nodes(), G.number_of_edges())