

#graph parameters
# - number of vertices:
graphSize=10
# - edges (leave blank for generating a random graph:
#   list of pairs/triples (source, target, [weight])
#edges = [[1,2,3.5],[1,3,4.2]]
# - should the student select edges?
selectEdges=false
# - should the student select vertices?
selectVertex=false
# - show edge weights
weighted=false
# - show arc directions
directed=false
# - parameters for random graph generation
minRandomWeight=2
maxRandomWeight=10
randomDensity=1.2
# - create a vertex connected to every other (id of vertex or -1 for "no such vertex")
sourceVertex=-1
# - labels to be drawn on the vertices
vertexLabel=["A","B","C","D","E","F","G", "H","I","J","K","L","M","N","O","P","Q","R","T","U","V","W","X","Y","Z"]


#matrix parameters:
# - use first column(s) for title (ignore in column indexing)
titleColumns=1
# - use first row(s) for title (ignore in row indexing)
titleRows=1
# - default value for blank cells
valueForBlank=-1
# - show a new-line button
newLineButton=false
# - show a copy-line button
copyLineButton=false




##### template:

form=@/src/html/mainForm.html
form+=@/src/html/matrixElement.html
form+=@/src/html/graphElement.html

type=direct

before=@/src/py/graphs.py

before+=
form+="</center>"

import random
random.seed(seed)

pyDirected=False
if (directed=="true"):
	pyDirected=True
else :
	directed="false"
	
pyWeighted=False
if (weighted=="true"):
	pyWeighted=True
else :
	weighted="false"

print(graphSize)

try:
	edges	
except NameError:	
	if pyWeighted:		
		edges=generateRandomWeightedGraph(int(graphSize), float(randomDensity), pyDirected,int(minRandomWeight),int(maxRandomWeight), int(sourceVertex))
	else:
		edges=generateRandomGraph(int(graphSize), float(randomDensity), pyDirected, int(sourceVertex))

==



