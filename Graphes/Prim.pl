author = Laurent Bulteau
name= Prim
title=Algorithme de Prim

template=/src/template/graphAndMatrix.pl

text==


**Calcul d'un arbre couvrant de poids minimal en utilisant l'algorithme de Prim**

Dans la matrice ci-dessous, saisir dans chaque ligne le tableau de distances calculé à chaque itération de l'algorithme de Prim, en utilisant le sommet A comme sommet de départ. 
En cas d'égalité, les sommets sont choisis par ordre alphabétique.
Dans le graphe, sélectionnez les arêtes données en sortie de l'algorithme.


**Mode d'emploi**

* La ligne **0** correspond à l'initialisation.
* Utilisez le charactère ***** pour une valeur infinie.
* Vous pouvez déplacer les sommets en les faisant glisser.
* Cliquez sur une arête pour la (dé)sélectionner.
* Pour vous aider, vous pouvez sélectionner un sommet en cliquant dessus, cette sélection n'est pas comptabilisée dans la solution.

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


