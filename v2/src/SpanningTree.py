def sublist(lst1, lst2):
	return set(lst1) <= set(lst2)
			
def parseListOfEdges(s):
	s=s.replace('[','(').replace(']',')').replace(' ','')	
	tuples = s.split('),(')
	out = []
	for e in tuples:
		e=e.strip('()')
		if e!="":			
			try:
				f = e.split(',')+['0']          
				out.append((int(f[0]),int(f[1]), float(f[2])))
			except ValueError as err:
				print ("Error in parseListOfEdges with '"+s+"'\n tuples: "+str(tuples)+"\n e='"+str(e)+"'")
				print (err)
	return out
   
    
def parseListOfVertices(s):
    v = s.split(',')
    out = []
    for u in v:
        if u!="":
          out.append(int(u))
    return out
  
def removeWeights(edges):
	out=[]
	for u,v,w in edges:
		out=out+[(u,v)]
	return out
    
  
def parseSolution(reponse,dic):
	out={}
	out['edges']=parseListOfEdges(reponse.get("selectedEdges",""))
	out['vertices']=parseListOfVertices(reponse.get("selectedVertices",""))
	out['n']=int(dic.get("graphSize",10))
	out['graph']=parseListOfEdges(dic.get("edges","[]"))
	if (not sublist(out['edges'],out['graph'])):
		print("Selected:"+str(out['edges']))
		print("graph:"+str(out['graph']))
		raise ValueError("Les arêtes sélectionnées ne sont pas toutes dans le graphe d'entrée.")
	return out
  
def highlightVertices(v):
	return "<script>\n"+''.join("highlightV("+str(i)+");\n" for i in v)+"</script>"
def highlightEdges(e):
	return "<script>\n"+''.join("highlightE("+str(f[0])+","+str(f[1])+");\n" for f in e)+"</script>"


#fonction pour tester si un graphe est un arbre couvrant
# edges: ensemble des paires
# n nombre total de sommets (numérotés de 0 à n-1)
# codes de retour:
#  0: ok
# -1,-2 ou -3: nombre d'arêtes incorrect (=0, <n-1, >n-1)
#  i>0: sommet i n'est pas connecté au sommet 0

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

def isConnected (edges, n):
	ref=list(range(0,n))
	for e in edges:
		join(e[0],e[1],ref)
		print (e, ref)
	for i in range(1,n-1):
		if getref(i,ref)!=0:
			return False, i
	return True, 0
    
    





#===============
  
def isSpanningTree(edges, n):
	if (len(edges)==0):
		return False,-1
	if (len(edges)<n-1):
		return False,-2
	if (len(edges)>n-1):
		return False,-3
	return isConnected(edges, n)

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

def evaluate(reponse, dic):
  sol=parseSolution(reponse,dic)
  
  #  isSpanningTree(sol['edges'],sol['n']);
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

main()
