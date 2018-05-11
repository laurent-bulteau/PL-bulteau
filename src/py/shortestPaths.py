import math

'''
def dijkstra (graph, n, s) :
	dist = []
	out=[]
	for i in range(0,n)
		dist=dist+[0 if s==i else math.inf]
	rest=list(range(0,n))
	while (len(rest)>0)
		out+=[list(dist)]
		m = math.inf
		im=-1
		for i in rest:
			if dist[i]<m:
				im=i
				m=dist[i]
		if im==-1:
			break
		
	
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
'''


def bellmanFord (graph, n, s) :
	dist = []
	out=[]
	print("graph for BF : "+str(graph))
	for i in range(0,n):
		dist=dist+[0 if s==i else math.inf]	
	for i in range(0,n):
		prevDist=list(dist)
		out+=[prevDist]
		for e in graph:
			d=prevDist[e[0]]+e[2]
			if d<dist[e[1]]:
				dist[e[1]] = d
	return out

'''
def listOfBFErrors(graphSol, matrixSol):
	n=graphSol['n']
	bf = bellmanFord(graphSol['graph'], n, graphSol['s'])
	errs=[]
	print(bf)
	print(matrixSol)
	for i in range (0,n):
		for j in range(0,n):
			if (bf[i][j]!=matrixSol[i][j]):
			#if (bf[i][j]==math.inf and matrixSol[i][j] != "*") or (bf[i][j]<math.inf and int(matrixSol[i][j])!=bf[i][j]):
				errs+=[str(i)+"_"+str(j)]
	return errs;
'''


def listOfBFErrors(graphSol, matrixSol):
	n=graphSol['n']
	bf = bellmanFord(graphSol['graph'], n, graphSol['s'])
	errs=[]
	print(bf)
	print(matrixSol)
	return listOfErrors(bf, matrixSol, n)
def evaluateBF(graphSol, matrixSol):
	errs=listOfBFErrors(graphSol, matrixSol)
	print(errs)
	if errs==[]:
		return True, "Bravo!"	
	else:
		return False, "Il y a "+str(len(errs))+ " erreurs."+highlightCells(errs)
	
	

	