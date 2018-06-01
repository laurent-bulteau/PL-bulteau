author = Laurent Bulteau
name= Construction d'une liste
title=Construction d'une liste

template=/src/template/graph.pl


text==

**Construire une liste**

Représenter la liste obtenue via le code suivant:

      Liste l=NULL;
      l=cons(l, 1);
      l=cons(l, 2);
      l->succ=cons(NULL,3)
      l=cons(l, 4);
      l=cons(l, 5);
      l->val=6

**Mode d'emploi**

* Pour ajouter un lien: double-cliquez sur le noeud de départ, puis sur le noeud d'arrivée
* Double-cliquez sur un lien pour le supprimer
==



addEdges=true
directed=true
vertexLabel=["l",1,2,3,4,5,6]
graphSize=7
edges=[]


before==

import random
random.seed(seed)


#generateEdgesFromParameters()

form+="</center>"

==
evaluator=@/src/py/graphs.py
evaluator+=

sol=readSolution()
k=list(globals().keys())
k.sort()
print(k)

grade=(True,str(sol))

==



