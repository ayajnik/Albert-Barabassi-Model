# -*- coding: utf-8 -*-
"""abm

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bx7bFbVNlpP_qSKjHRbnhsqFRWYiSTs-
"""

!pip install networkx

#importing the libraries
import networkx as nx
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

#function for main displaying graph
def display_graph(G,i,ne):
  pos = nx.circular_layout(G)
  if i == ' ' and ne == ' ':
    new_nodes = []
    rest_nodes = G.nodes()
    new_edges = []
    rest_edges = G.edges()
  else:
    new_nodes = [i]
    rest_nodes = list(set(G.nodes())- set(new_node))
    new_edges = ne
    rest_edges = list(set(G.edges())-set(new_edges)-set([(b,a) for (a,b) in new_edges]))
    nx.draw_networkx_nodes(G, pos, nodelist = new_nodes,node_color = 'g')
    nx.draw_networkx_nodes(G, pos, nodelist = rest_nodes,node_color = 'b')
    nx.draw_networkx_nodes(G, pos, edgelist = new_edges,edge_color = 'y',style = "dashdot")
    nx.draw_networkx_nodes(G, pos, edgelist = rest_edges,edge_color = 'r')
    plt.show()

#defining the albert barabassi phenomenan
def add_node_barabassi(G,n,m0):
  m = m0 - 1
  
  for i in range(m0+1,n+1):
    G.add_node(i)
    #preprocessing
    degress - nx.degree(G)
    node_probabilities = {}
    
    for each in G.nodes():
      node_probabilities[each] = (float)degress[each]/sum(degrees.values())
    node_prob_cum = []
    prev = 0
    
    for n,p in node_probabilities.items():
      temp = [n,prev+p]
      node_prob_cum.append(temp)
      prev = prev +p
      
    new_edges = []
    new_edges_added = []
    target_nodes = []
    
    while (new_edges_added < m):
      prev_cum = 0
      r = random.random()
      k = 0
      while(not(r>prev_cum and r<= node_prob_cum[k][1])):
        prev_cum = node_prob_cum[k][1]
        k+=1
      target_node = node_prob_cum[k][0]
      if target_node in target_nodes:
        cotinue
      else:
        target_nodes.append(target_node)
      G.add_edge(i,target_node)
      new_edges_added += 1
      new_edges.append((i,target_nodes))
      
    print (new_edges_added,"Edges Added !")
    display_graph(G,i,new_edges)
  return G

      
      
    

#creating our main function
def main():
  n = int(input("Enter the value of total number of users:"))
  m0 = random.randint(2,n/5)
  G = nx.path_graph(m0)
  m = m0 - 1
  
  display_graph(G, " "," ")
  G = add_node_barabassi(G,n,m0)
main()

