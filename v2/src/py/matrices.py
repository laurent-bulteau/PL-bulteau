
import random
import json

	
			
def extractMatrixKeys(matrixID, m, valueForBlank):
	i=0
	out=[]	
	while matrixID+"_"+str(i)+"_0" in m:
		row=[]
		j=0		
		while "matrix_"+str(i)+"_"+str(j) in m:
			val = m["matrix_"+str(i)+"_"+str(j)]
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



def listOfErrors(reference, solution, n):	
	errs=[]
	for i in range (0,n):
		for j in range(0,n):
			if (reference[i][j]!=solution[i][j]):
			
				errs+=[str(i)+"_"+str(j)]
	return errs;


