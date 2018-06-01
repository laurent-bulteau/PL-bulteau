author = Laurent Bulteau
name= Arbre couvrant min
title=Arbre couvrant minimal

template=/src/template/graph.pl

text==

**Calcul d'un arbre couvrant de poids minimal**

Dans le graphe ci-dessous, sélectionnez des arêtes de façon à former un arbre couvrant dont le poids est minimal.

**Mode d'emploi**

* Vous pouvez déplacer les sommets en les faisant glisser.
* Cliquez sur une arête pour la (dé)sélectionner.
==



selectEdges=true
weighted=true
graphSize=7




evaluator=@/src/py/graphs.py
evaluator+=@/src/py/spanningTrees.py
evaluator+=

print("EVALUATE seed : "+str(seed))
sol=readSolution()


grade=evaluateMST(sol)

==



