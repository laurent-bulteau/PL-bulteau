

form=@/src/GraphForm.html

type=direct

graphSize=10
selectEdges=false
selectVertex=false
directed=false
vertexLabel=["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","T","U","V","W","X","Y","Z"]



before=@/src/graphs.py





before+=

directed=False
graphSize=12
try:
	edges	
except NameError:
	edges=generateRandomGraph(int(graphSize), 1.2, directed)

#edges=[[1,2]]

==

evaluator==
readSolution()
==