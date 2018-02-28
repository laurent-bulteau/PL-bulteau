
def parseListOfEdges(s):
    tuples = s.split('),(')
    out = []
    for e in tuples:
        s,t = e.strip('()').split(',')
        out.append((int(s),int(t)))
    return out
    

def spanningTree(edges, n):
    def setref(s,t,ref):
        if ref[t]!=t:
            if s<ref[t]:
                setref(s,ref[t],ref)
            if ref[t]<s:
                setref(ref[t],s,ref)
        ref[t]=ref[s]
    ref=list(range(0,n))
    if (len(edges)==0):
        return -1
    if (len(edges)<n-1):
        return -2
    if (len(edges)>n-1):
        return -3
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
    
    
def evaluator(reponse, dic):
  edges=parseListOfEdges(reponse["selectEdges"])
  n=int(dic['graphSize'])
  res= spanningTree(edges,n);
  if res==0:
    return True, "Bravo!"
  elif res==-1:
    return False, "Cliquez sur les arêtes pour les sélectionner"
  elif res==-2:
    return False, "Vous n'avez pas sélectionné suffisament d'arêtes pour espérer pouvoir tout connecter."
  elif res==-3:
    return False, "Vous avez sélectionné trop d'arêtes, je suis sûr qu'il y a un cycle quelque part."
  else:
    return False, "Le nombre d'arête est bon, mais êtes-vous sûr d'avoir bien tout connecté?<br>(Il n'y a pas de chemin entre les deux sommets entourés) <script>evaluate("+str(res)+")</script>"  

def main():
  
  reponse={'selectEdges':'(1,3),(2,4),(6,5),(5,2),(3,4)'}
  print(reponse['selectEdges'])
  dic={'graphSize':7}
  return evaluator(reponse,dic)

