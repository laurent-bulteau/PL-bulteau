author = Laurent Bulteau
name= Abre couvrant
title=Arbre couvrant

template=/src/template/graph.pl

text==

**Calcul d'un arbre couvrant**

Dans le graphe ci-dessous, sélectionnez des arêtes de façon à former un arbre couvrant.

**Mode d'emploi**

* Vous pouvez déplacer les sommets en les faisant glisser.
* Cliquez sur une arête pour la (dé)sélectionner.
==


selectEdges=true
graphSize=8



evaluator=@/src/py/graphs.py
evaluator+=@/src/py/spanningTrees.py
evaluator+=

sol=readSolution()


grade=evaluateST(sol)

==




