author = Laurent Bulteau
name= Spanning Trees
title=Arbres Couvrants
text==
Dans le graphe ci-dessous, sélectionnez des arêtes de façon à former un arbre couvrant.

Vous pouvez déplacer les sommets en les faisant glisser.
==
type=direct
graphSize=7
truc=2
edges=[[1,3],[2,4],[3,0],[4,5],[6,5],[6,4],[5,2],[3,4],[0,6]]
selectEdges=true
selectVertex=true
directed=false
vertexLabel=["A","B","C","D","E","F","G"]


before=@/src/SpanningTree.py

form=@/src/GraphForm.html

evaluator==
#grade=(True,"Yeah") 
grade=evaluate(response, globals())
==


