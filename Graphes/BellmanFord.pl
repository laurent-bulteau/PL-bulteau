author = Laurent Bulteau
name= Bellman Ford
title=Bellman Ford

template=/src/template/graphAndMatrix.pl

text==
Dans la matrice ci-dessous, saisir dans chaque ligne le tableau de distances calculé à chaque itération de l'algorithme de Bellman-Ford (dans sa version de base), en utilisant le sommet A comme sommet de départ.

La ligne "0" correspond à l'initialisation.
Une case vide est comptée comme 0, utilisez le charactère "*" pour une valeur infinie.
==

directed=true
weighted=true


graphSize=6
matrix = [["","A","B","C","D","E","F"],[0],[1],[2],[3],[4],[5]]
copyLineButton=true
sourceVertex=0

evaluator=@/src/py/graphs.py
evaluator+=@/src/py/matrices.py
evaluator+=@/src/py/shortestPaths.py
evaluator+=




grade=evaluateBF(readSolution(), readIntMatrix(valueForBlank))

==


