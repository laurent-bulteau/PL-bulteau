author = Laurent Bulteau
name= Prim
title=Algorithme de Prim

template=/src/template/graphAndMatrix.pl

text==
Dans la matrice ci-dessous, saisir dans chaque ligne le tableau de distances calculé à chaque itération de l'algorithme de Prim, en utilisant le sommet A comme sommet de départ. En cas d'égalité, les sommets sont choisis par ordre alphabétique.

Sélectionnez les arêtes de l'arbre couvrant correspondant. Vous pouvez sélectionner des sommets pour vous aider, ils ne seront pas comptabilisés.

La ligne "0" correspond à l'initialisation.
Utilisez le charactère "*" pour une valeur infinie.

==

directed=false
weighted=true
selectEdges=true
selectVertices=true
randomDensity=2

graphSize=6
matrix = [["","A","B","C","D","E","F"],[0],[1],[2],[3],[4],[5]]
copyLineButton=true
sourceVertex=0

evaluator=@/src/py/graphs.py
evaluator+=@/src/py/matrices.py
evaluator+=@/src/py/spanningTrees.py
evaluator+=


sol=readSolution()
print(sol)
mat=readIntMatrix(valueForBlank)

print(mat)

grade=evaluatePrim(sol, mat)

==
