author = Laurent Bulteau
name= Bellman Ford
title=Algorithme de Bellman Ford

template=/src/template/graphAndMatrix.pl

text==
**Calcul des plus courts chemins**

Dans la matrice ci-dessous, saisir dans chaque ligne le tableau de distances calculé à chaque itération de l'algorithme de Bellman-Ford (sans optimisation), en utilisant le sommet **A** comme sommet de départ.

**Mode d'emploi**

* La ligne **0** correspond à l'initialisation. 
* Utilisez le charactère ***** pour une valeur infinie. 
* Le bouton à la fin de chaque ligne permet de recopier la ligne précédente.
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







