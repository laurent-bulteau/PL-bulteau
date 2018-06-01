author = Laurent Bulteau
name= Kruskall
title=Algorithme de Kruskall

template=/src/template/graphAndMatrix.pl

text==


**Calcul de la matrice des plus courts chemins en utilisant l'algorithme de Kruskall**


Les deux premières étapes de l'algorithme de Kruskall ont été appliquées sur le 
graphe ci-dessous (i.e. avec les sommets **A** et **B**), ce qui nous a permis d'obtenir 
la première matrice donnée. 

Réaliser la troisème étape (avec le sommet **C**), 
en remplissant la matrice suivante.




**Mode d'emploi**

* Utilisez le charactère ***** pour une valeur infinie.

==

directed=true
weighted=true


graphSize=6
matrix = [["","A","B","C","D","E","F"],[0],[1],[2],[3],[4],[5]]


minRandomWeight=1
maxRandomWeight=10
randomDensity=2

extraForm=</center>

before=@/src/py/graphs.py
before+=@/src/py/matrices.py
before+=@/src/py/shortestPaths.py

before+=

import random
random.seed(seed)

generateEdgesFromParameters()


#run kruskall
kMatrices = kruskall(parseListOfEdges(edges), int(graphSize))

#show step 2
k=kMatrices[2]
k=addCharHeaders(k)
matrix=encodeMatrixToSingleString(k)
print(matrix)

#remember step 3
expected=kMatrices[3]
print(str(k))

#draw empty matyrix to fill In
empty=addCharHeaders(increaseToSize([[]], int(graphSize)))

form+=drawAnotherMatrix("fillIn", {'mat':empty})
#form+=drawAnotherMatrix("fillIn", {'mat':[["","A","B","C","D","E","F"],[0],[1],[2],[3],[4],[5]]})
#form+=drawAnotherMatrix("other", {'mat':encodeMatrixToStrings(k)})

form+="</center>"


==


evaluator=@/src/py/graphs.py
evaluator+=@/src/py/matrices.py
evaluator+=@/src/py/shortestPaths.py
evaluator+=

print("Proposed solution:")

mat=readIntMatrix(valueForBlank,"fillIn")
print(mat)


grade=evaluateKruskall(mat, expected,"fillIn")


==



