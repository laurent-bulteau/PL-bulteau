author = Laurent Bulteau
name= Spanning Trees
title=Arbre couvrant de poids minimal

template=/src/template/graph.pl

text==
Dans le graphe ci-dessous, sélectionnez des arêtes de façon à former un arbre couvrant dont le poids est minimal.

Vous pouvez déplacer les sommets en les faisant glisser.
==



selectEdges=true
weighted=true
graphSize=7




evaluator=@/src/py/graphs.py
evaluator+=@/src/py/spanningTrees.py
evaluator+=

sol=readSolution()


grade=evaluateMST(sol)

==
