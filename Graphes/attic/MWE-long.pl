author = Laurent Bulteau
name= Spanning Trees
title=MWE2


text==
Dans le graphe ci-dessous, sélectionnez des arêtes de façon à former un arbre couvrant dont le poids est minimal.

Vous pouvez déplacer les sommets en les faisant glisser.
==


graphSize=7

selectVertex=false
selectEdges=true

weighted=false
directed=false
minRandomWeight=2
maxRandomWeight=10
randomDensity=1
sourceVertex=-1
vertexLabel=["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","T","U","V","W","X","Y","Z"]


form=@/src/html/mainForm.html
form+=@/src/html/graphElement.html

type=direct


before=@/src/py/graphs.py

before+=
form+="</center>"

import random
random.seed(seed)


print(graphSize)

edges=str(generateRandomGraph(int(graphSize), float(randomDensity), False, int(sourceVertex)))
==



evaluator=@/src/py/graphs.py
evaluator+=@/src/py/spanningTrees.py
evaluator+=

grade=evaluateMST(readSolution())

==
