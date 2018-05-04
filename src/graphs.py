
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
		print (e, ref)
	for i in range(1,n-1):
		if getref(i,ref)!=0:
			return False, i
	return True, 0


def isNewEdge(e, u, v):
	if u==v:
		return False
	if [u,v] in e:
		return False
	return True



#generates a connected graph with density*n extra edges beyond a tree (edges are picked randomly among n^2, and discarded if already used or self-loops
#density of 0 yields a tree, density of 1000*n*n would almost surely yield a clique


def generateRandomGraph(n, density, directed):
	print(dir())
	for key in globals().keys():
		print (key)
	e=[]
	nodes= list(range(0, n))
	random.shuffle(nodes) 
	for i in  range(1,n):
		e+=[[nodes[random.randint(0,i-1)], nodes[i]]]
	for i in range(0, int(density*n)):
		u=random.randint(0,graphSize-1)
		v=random.randint(0,graphSize-1)
		if isNewEdge(e,u,v)  and ( directed or  isNewEdge(e,v,u)):
			e=e+[[u,v]]
	print("Generated graph: ")
	print(e)
	return str(e)	
	

def readSolution():
	global sol
	sol=parseSolution(response,globals())
'''	
key=12

for key in locals().keys():
	print (key)
print(dir())
print(f(120))

seed=5
directed="false"
graphSize=12
import random
random.seed(seed)
if (directed=="false"):
	directed=False
else:
	directed=True

print(isNewEdge([],2,5))
'''
#generateRandomGraph(int(graphSize), 1.2,directed)









