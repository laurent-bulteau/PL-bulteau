author = Laurent Bulteau
name= Spanning Trees
title=Arbres Couvrants

template=/src/template/graph.pl

text==
Dans le graphe ci-dessous, sélectionnez des arêtes de façon à former un arbre couvrant.

Vous pouvez déplacer les sommets en les faisant glisser.
==


selectEdges=true
graphSize=8



evaluator=@/src/py/graphs.py
evaluator+=@/src/py/spanningTrees.py
evaluator+=

sol=readSolution()


grade=evaluateST(sol)

==

