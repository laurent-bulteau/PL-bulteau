author = Laurent Bulteau
name= Construction d'une liste - Niveau 2
title=Construction d'une liste

template=/src/template/graph.pl


text==

**Construire une liste**

Représenter la liste obtenue via le code suivant:

		Liste L=NULL;
		L=cons(L, #0);
		L=cons(L, #1);
		L->succ=cons(NULL,#2)
		L=cons(L, #3);
		L=cons(L, #4);
		L->val=#5

**Mode d'emploi**

* Ajouter un lien entre "L" et le noeud contenant la première valeur de la liste demandée, puis de la première valeur à la seconde, etc.
* Pour ajouter un lien: cliquez sur le noeud de départ, puis sur le noeud d'arrivée
* Cliquez sur un lien pour le supprimer
==



addEdges=true
directed=true
vertexLabel=["L",1,2,3,4,5,6]
graphSize=7
edges=[]


before==

import random
random.seed(seed)

L=[1,2,3,4,5,6]
replaces=L
random.shuffle(replaces)
for i in range(0,len(replaces)):
	text=text.replace("#"+str(i), str(replaces[i]))

#generateEdgesFromParameters()

form+="</center>"

==
evaluator=@/src/py/graphs.py
evaluator+=@/src/py/lists.py
evaluator+=


print("evaluate")
sol=readSolution()
print(sol['addedEdges'])
correct=compareToExpectedList(sol['addedEdges'],0,[L[5],L[3],L[1],L[2]] )
grade=(correct,"Bravo!" if correct else "Désolé, ce n'est pas ça")

==



