
#fonction pour tester si un graphe est un arbre couvrant
# edges: ensemble des paires
# n nombre total de sommets (numérotés de 0 à n-1)
# codes de retour:
#  0: ok
# -1: nombre d'arêtes incorrect 
#  i: sommet i n'est pas connecté au sommet 0

def spanningTree(edges, n):
	def setref(s,t,ref):
		if ref[t]!=t:
			if s<ref[t]:
				setref(s,ref[t],ref)
			if ref[t]<s:
				setref(ref[t],s,ref)
		ref[t]=ref[s]
	ref=list(range(0,n))
	if (len(edges)!=n-1):
		return -1
	for (s,t) in edges:
		if s<t:
			setref(s,t,ref)
		if t<s:
			setref(t,s,ref)
		print(s,t,ref)	
	for i in range(1,n-1):
		if i==ref[i]:
			return i
	return 0



def test():
	edges=[(1,3),(2,4),(3,0),(4,5),(6,5),(6,4)]
	return spanningTree(edges, 7)	

