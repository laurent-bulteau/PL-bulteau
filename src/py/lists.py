def interpretAsList(edges, start):
	out=[]	
	ok=True
	while ok:
		ok=False
		next=-1
		for e in edges:
			if  e[0]==start:
				if ok:
					return False, []	
				if e[1] in out:
					return False, []
				next=e[1]
				ok=True
		if ok:
			out+=[next]
			start=next		
		
	return (True, out)


def compareToExpectedList(edges, start, expected):
	ok, sol=interpretAsList(edges, start)
	print (expected)
	if not ok:
		return False
	return sol==expected





