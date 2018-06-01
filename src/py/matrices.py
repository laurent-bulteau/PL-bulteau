
import random
import json
from functools import reduce
	
			
def extractMatrixKeys(matrixID, m, valueForBlank):
	i=0
	out=[]	
	while matrixID+"_"+str(i)+"_0" in m:
		row=[]
		j=0		
		while matrixID+"_"+str(i)+"_"+str(j) in m:
			val = m[matrixID+"_"+str(i)+"_"+str(j)]
			if val=="":
				val=valueForBlank
			row+=[val]
			j+=1
		out+=[row]	
		i+=1
	return out


def parseElementToInt(x):   
	return math.inf if x=="*" else 0 if x=="" else int(x)

def parseMatrixToInt(m):
	return [[parseElementToInt(x) for x in row] for row in m]


def readMatrix(valueForBlank, matrixID="matrix"):
	return extractMatrixKeys(matrixID,response, valueForBlank)

def readIntMatrix(valueForBlank, matrixID="matrix"):
	return parseMatrixToInt(readMatrix(valueForBlank, matrixID))

def highlightCells(cells,  matrixID="matrix"):
	return "<script>\n"+''.join("highlightCell('"+x+"', '"+matrixID+"');\n" for x in cells)+"</script>"

def drawAnotherMatrix(name, params):
	return  '<script>\n drawMatrix("'+name+'",'+json.dumps(params)+");\n </script>"


def increaseToSize(mat, n):
	mat=(mat+[[]]*n)[0:n]
	mat=list(map(lambda row:(row+[None]*n)[0:n], mat))
	return mat


def addHeaders(mat, cols, rows):
	cols=[""]+list(cols)
	mat=list(mat)
	rows=list(rows)
	for i in range(0, len(mat)):
		mat[i]=[rows[i]]+mat[i]
	#mat=list(map(lambda x:[x[0]]+x[1], zip(list(rows), mat)))
	l=reduce(lambda m, row: max(m, len(row)), mat, 0)	
	mat=[cols[0:l]]+mat 		
	return mat

def addCharHeaders(mat):
	return addHeaders(mat, map(chr, range(65,91)), map(chr, range(65,91)))

def encodeMatrixToStrings(mat):
#	return map(lambda row:map(lambda x:(x==math.inf?"*":str(x)), row), mat)
	return list(map(lambda row:list(map(lambda x:'0' if x==0 else str(x).replace('inf','*').rstrip("0").rstrip("."), row)), mat))


def encodeMatrixToSingleString(mat):
	return str(encodeMatrixToStrings(k)).replace("'",'"')

def listOfErrors(reference, solution, n):	
	errs=[]
	for i in range (0,n):
		for j in range(0,n):
			if (reference[i][j]!=solution[i][j]):			
				errs+=[str(i)+"_"+str(j)]
	return errs;


