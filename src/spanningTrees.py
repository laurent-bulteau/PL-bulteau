





def getref(s,ref):
	if ref[s]!=s:
		ref[s]=getref(ref[s], ref)
	return ref[s]
  
def join(s,t,ref):
	r1=getref(s,ref)
	r2=getref(t,ref)
	if r1<r2:
		ref[r2]=r1
	elif r2<r1:
		ref[r1]=r2  
    
  
def buildMinimumSpanningTree (graph, n) :
	sortedEdges = sorted(graph, key=lambda e: e[2])
	ref=list(range(0,n))
	out=[]
	wTree=0
	for (s,t,w) in sortedEdges:
		if (getref(s,ref)!=getref(t,ref)):
			out=out+[(s,t,w)]
			join(s,t,ref)
			wTree+=w
	return (out,wTree)
#===============
  
def isSpanningTree(edges, n):
	if (len(edges)==0):
		return False,-1
	if (len(edges)<n-1):
		return False,-2
	if (len(edges)>n-1):
		return False,-3
	return isConnected(edges, n)

#fonction pour tester si un graphe est un arbre couvrant
# edges: ensemble des paires
# n nombre total de sommets (numérotés de 0 à n-1)
# codes de retour:
#  0: ok
# -1,-2 ou -3: nombre d'arêtes incorrect (=0, <n-1, >n-1)
#  i>0: sommet i n'est pas connecté au sommet 0

def isMinimumSpanningTree(graph, edges, n):
	if (len(edges)==0):
		return False,-1
	if (len(edges)<n-1):
		return False,-2
	if (len(edges)>n-1):
		return False,-3
	(a,b) = isConnected(edges, n)
	if (a==False):
		return a,b
	w=0
	for e in edges:
		w= w+e[2]
	(opt, wOpt)=buildMinimumSpanningTree(graph, n)
	print(wOpt)
	if (w>wOpt):
		return False, -4
	return True,0


#grade=evaluateST()


def evaluateST():  
  res, code= isSpanningTree(sol['edges'],sol['n']); 
  if res:
    return True, "Bravo!"
  elif code==-1:
    return False, "Cliquez sur les arêtes pour les sélectionner"
  elif code==-2:
    return False, "Vous n'avez pas sélectionné suffisament d'arêtes pour espérer pouvoir tout connecter."
  elif code==-3:
    return False, "Vous avez sélectionné trop d'arêtes, je suis sûr qu'il y a un cycle quelque part."
  elif code==-4:
    return False, "Ceci est bien un arbre couvrant, mais il n'est pas de poids minimal"
  else:
    return False, "Le nombre d'arêtes est bon, mais êtes-vous sûr d'avoir bien tout connecté?<br>(Il n'y a pas de chemin entre les deux sommets entourés)"+highlightVertices([0,code])



def evaluateMST():  
  res, code= isMinimumSpanningTree(sol['graph'], sol['edges'],sol['n']); 
  if res:
    return True, "Bravo!"
  elif code==-1:
    return False, "Cliquez sur les arêtes pour les sélectionner"
  elif code==-2:
    return False, "Vous n'avez pas sélectionné suffisament d'arêtes pour espérer pouvoir tout connecter."
  elif code==-3:
    return False, "Vous avez sélectionné trop d'arêtes, je suis sûr qu'il y a un cycle quelque part."
  elif code==-4:
    return False, "Ceci est bien un arbre couvrant, mais il n'est pas de poids minimal"
  else:
    return False, "Le nombre d'arêtes est bon, mais êtes-vous sûr d'avoir bien tout connecté?<br>(Il n'y a pas de chemin entre les deux sommets entourés)"+highlightVertices([0,code])

def main():
# reponse={'selectedEdges':'(1,3),(2,4),(6,5),(5,2),(3,4),(2,6)', 'selectedVertices':''}
  reponse={'selectedEdges':'(1,3,3),(2,4,2),(6,4,1),(5,2,1),(3,4,3),(0,6,2)', 'selectedVertices':''}
  dic={'graphSize':7, 'edges':'[[1,3,3],[2,4,2],[3,0,8.33],[4,5,6],[6,5,4],[6,4,1],[5,2,1],[3,4,3],[0,6,2]]'}
  #print (str(evaluate(reponse,dic)))
  
#main()