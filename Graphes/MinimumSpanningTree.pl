author = Laurent Bulteau
name= Spanning Trees
title=Arbre couvrant de poids minimal
text==
Dans le graphe ci-dessous, sélectionnez des arêtes de façon à former un arbre couvrant dont le poids est minimal.

Vous pouvez déplacer les sommets en les faisant glisser.
==
type=direct
graphSize=7
truc=2
edges=[[1,3,3],[2,4,2],[3,0,8],[4,5,6],[6,5,5],[6,4,4],[5,2,1],[3,4,6],[0,6,2]]
selectEdges=true
selectVertex=true
directed=false
vertexLabel=["A","B","C","D","E","F","G"]


form=@/src/GraphForm.html
evaluator=@/src/SpanningTree.py
