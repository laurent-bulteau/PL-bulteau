


import random
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
	v = s.replace(' ','').strip('()[]').split(',')
	out = []
	for u in v:
		if u!="":
			try:
				out.append(int(u))
			except ValueError as err:
				print ("Error in parseListOfVertices with '"+s+"'\n  u='"+str(u)+"'")
				print (err)
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
	out['s']=int(dic.get("sourceVertex",0))
	out['t']=int(dic.get("targetVertex",0))
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


def isConnected (edges, n):
	ref=list(range(0,n))
	for e in edges:
		join(e[0],e[1],ref)
	for i in range(1,n-1):
		if getref(i,ref)!=0:
			return False, i
	return True, 0


def isNewEdge(e, u, v):
	if u==v:
		return False
	for x in e:
		if u==x[0] and v==x[1]:
			return False
	return True


def subsetOfUndirectedEdges(s,t):
	for e in s:
		found=False
		for f in t:
			if (e[0]==f[0] and e[1]==f[1]) or (e[1]==f[0] and e[0]==f[1]):
				found=True 
		if not found:
			return False
	return True


def sameUndirectedEdges(s,t):
	return subsetOfUndirectedEdges(s,t) and subsetOfUndirectedEdges(t,s)




#generates a connected graph with density*n extra edges beyond a tree (edges are picked randomly among n^2, and discarded if already used or self-loops
#density of 0 yields a tree, density of 1000*n*n would almost surely yield a clique


def generateRandomGraph(n, density, directed, source=-1):
	e=[]
	rndStr=str(random.randint(0,9))
	nodes= list(range(0, n))
	random.shuffle(nodes) 
	rndStr+=str(nodes)
	
	if source>=0:
		nodes.remove(source)
		nodes=[source] + nodes
	for i in  range(1,n):		
		e+=[[nodes[random.randint(0,i-1)], nodes[i]]]	
	rndStr+=str(e)
	for i in range(0, int(density*n)):
		u=random.randint(0,n-1)
		v=random.randint(0,n-1)
		if isNewEdge(e,u,v)  and ( directed or  isNewEdge(e,v,u)):
			e=e+[[u,v]]
		rndStr+=str((u,v))
	print("Random witness" + rndStr)
	print("Generated graph: ")
	print(e)
	return str(e)	
	
	
def generateRandomWeightedGraph(n, density, directed, minWeight, maxWeight, source=-1):	
	e=[]
	nodes= list(range(0, n))
	random.shuffle(nodes) 
	if source>=0:
		nodes.remove(source)
		nodes=[source] + nodes
	for i in  range(1,n):
		e+=[[nodes[random.randint(0,i-1)], nodes[i], random.randint(minWeight, maxWeight)]]
	for i in range(0, int(density*n)):
		u=random.randint(0,n-1)
		v=random.randint(0,n-1)
		if isNewEdge(e,u,v)  and ( directed or  isNewEdge(e,v,u)):
			e=e+[[u,v, random.randint(minWeight, maxWeight)]]
	print("Generated graph: "+str(e))
	return str(e)	

def boolean(s):
	if (s=="true"):
		return True
	else :
		return False
	
def generateEdgesFromParameters():
	if 'edges' not in globals():
		global edges
		if boolean(weighted):		
			edges=generateRandomWeightedGraph(int(graphSize), float(randomDensity), boolean(directed),int(minRandomWeight),int(maxRandomWeight), int(sourceVertex))
		else:
			edges=generateRandomGraph(int(graphSize), float(randomDensity), boolean(directed), int(sourceVertex))
	else:
		print("Input graph: " + str(edges))
		

def readSolution():
	return parseSolution(response,globals())






