author = Laurent Bulteau
name= Kruskall
title=Algorithme de Kruskall

template=/src/template/graphAndMatrix.pl

text==
Dans la matrice ci-dessous, saisir l'....

La ligne "0" correspond à l'initialisation.
Une case vide est comptée comme 0, utilisez le charactère "*" pour une valeur infinie.
==

directed=true
weighted=true


graphSize=6
matrix = [["","A","B","C","D","E","F"],[0],[1],[2],[3],[4],[5]]
copyLineButton=true
sourceVertex=0


before=@/src/py/graphs.py
before+=@/src/py/matrices.py

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
	
matrix=matrix.replace("2","2,22")
form+=drawAnotherMatrix("other", {'mat':[["","A","B","C","D","E","F"],[0],[1],[2],[3],[4],[5]]})	

==


evaluator=@/src/py/graphs.py
evaluator+=@/src/py/matrices.py
evaluator+=@/src/py/shortestPaths.py
evaluator+=


sol=readSolution()
print(sol)
mat=readIntMatrix(valueForBlank)

print(mat)


grade=evaluateBF(sol, mat)

==
