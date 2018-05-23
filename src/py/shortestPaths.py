import math
import random

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
import random
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
import copy

def kruskall(graph, n) :
	dists=[]	
	for i in range(0,n):
		dist=[]
		for j in range(0,n):
			dist=dist+[0 if i==j else math.inf]	
		dists+=[dist]
	for e in graph:
		dists[e[0]][e[1]]=e[2]
	out=[]	
	for t in range(0,n):
		last=copy.deepcopy(dists)
		out+=[last]
		for i in range(0,n):
			for j in range(0,n):
				dists[i][j]=min(dists[i][j], last[i][t]+last[t][j])		
	out+=[dists]
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
	
def nicePrintKruskall(k, n) :
	for i in range(0,n+1):
		print(i)
		for j in range(0,n):
			print("   "+str(k[i][j]).replace(",","\t "))
	
def test():
	graph= [[0, 2, 7], [2, 4, 8], [2, 1, 5], [2, 5, 2], [5, 3, 9], [4, 0, 7], [5, 4, 10], [5, 2, 2], [3, 5, 3], [3, 0, 4]]
	n= 6
	nicePrintKruskall(kruskall(graph, n), n)
	
test()	

	