import networkx as nx
from networkx.readwrite import json_graph
import json
from outronome import Addons
import matplotlib.pyplot as plt
import scipy
from networkx.drawing.nx_agraph import graphviz_layout
import pylab
import numpy as np

class Graph(object):
    def __init__(self):
        self.G = nx.Graph()
        Addons.CreateLog(self,"Grafo criado!\n")
        Addons.CreateCalculusLog(self,"Log de calculos criado!\n")
    
    def AddNode(self,node):
        self.G.add_node(node)
        Addons.Log(self,"Nó "+node+" adicionado com sucesso!\n")
    
    def AddMultNodes(self,nodes):
        self.G.add_nodes_from(nodes)
        Addons.Log(self,"Nós "+nodes+" adicionados com sucesso!\n")
    
    def AddEdge(self,init_node,end_node):
        edge = (init_node,end_node)
        self.G.add_edge(*edge)
        Addons.Log(self,"Aresta "+str(edge)+" adicionada com sucesso!\n")
    
    def AddMultEdges(self,edges):
        self.G.add_edges_from(edges)
    
    def ShowNodes(self):
        print(self.G.nodes())
        Addons.Log(self,"Visualização de nós !\n")
        
    def ShowEdges(self):
        print(self.G.edges())
        Addons.Log(self,"Visualização de arestas !\n")
        
    def ShowListAdj(self):
        print(self.G.adj)
        Addons.Log(self,"Lista de adjacencia gerada !\n")
    
    def ShowDegreeNode(self,node):
        print(self.G.degree(node))
        Addons.Log(self,"Visualização do grau do nó "+node+" !\n")
    
    def ClearGraph(self):
        self.G.clear()
        Addons.Log(self,"Limpeza do grafo concluida !\n")
        
    def dump_json_graph(self,name):
        print("--> Gerando grafo no arquivo: " + name + ".json")
        jsondata = json_graph.node_link_data(self.G)
        with open(name + '.json', 'w') as fp:
            json.dump(jsondata, fp)
        print("--> Completo")
        Addons.Log(self,"Json gerado com sucesso !\n")

    def WritePajek(self):
        nx.write_pajek(self.G,"grafo.net")
        Addons.Log(self,"Arquivo Pajek gerado com sucesso !\n")
        
    def ReadPajek(self):
        nx.read_pajek("grafo.net")
        Addons.Log(self,"Arquivo Pajek carregado com sucesso !\n")
        
    def PlotGraph(self):
        nx.draw(self.G,with_labels=True, font_weight='bold')
        plt.savefig("grafo.png")
        
    def CircularGraph(self):
        nx.draw_circular(self.G,with_labels=True, font_weight='bold')
        plt.savefig("grafo_circular.png")
        
    def RandomGraph(self):
        nx.draw_random(self.G,with_labels=True, font_weight='bold')
        plt.savefig("grafo_aleatorio.png")
    
    def KamadaGraph(self):
        nx.draw_kamada_kawai(self.G,with_labels=True, font_weight='bold')
        plt.savefig("grafo_kamada.png")
        
    def FruchtermanGraph(self):
        pos=nx.spring_layout(self.G)
        nx.draw_spring(self.G,with_labels=True,font_weight='bold')
        plt.savefig("Fruchterman.png")
        
    def NumberOfNodes(self):
        print(len(self.G))
        Addons.CalculusLog(self,"Numero de nós: " + len(self.G))
        
    def NumberOfEdges(self):
        print(self.G.number_of_edges())
        Addons.CalculusLog(self,"Numero de arestas: " + self.G.number_of_edges())
        
    def NumberOfComponents(self):
        print(self.G.number_of_edges()+len(self.G))
        Addons.CalculusLog(self,"Numero de componentes: " + self.G.number_of_edges()+len(self.G))
        
    def ShortestPath(self,init,end):
        print(nx.shortest_path(self.G,source=init,target=end))
        
    def GraphDensity(self):
        print(nx.density(self.G))
        
    def AverageClustering(self):
        print(nx.average_clustering(self.G))
    
    def ReadCSV(self):
        self.G = nx.read_adjlist('AdjGraph.csv',delimiter=',')
    
    def ReadCSVDirectedGraph(self):
        self.G = nx.read_adjlist('AdjGraph.csv',delimiter=',',create_using=nx.DiGraph())
    
    def AdjMatrix(self):
        #A = nx.adjacency_matrix(self.G)
        A = nx.to_numpy_matrix(self.G)
        print(A)
        
    
    
    """def HierarchyGraph(self,root):
        pos = nx.flow_hierarchy(self.G,root)
        nx.draw(self.G, pos=pos, with_labels=True)
        plt.savefig("grafo_arvore.png")
        
    def plot_tree(self):
        # this plot requires pygraphviz package
        pos = nx.nx_agraph.graphviz_layout(self.G, prog='dot')
        nx.draw(self.G, pos, with_labels=False, node_size=10,
                node_color=[[.5, .5, .5]], arrowsize=4)
        plt.savefig("grafo_arvore.png")"""
