author = Laurent Bulteau
name= MWE
title=exo

text==
Un nombre au hasard : 

==


form==
==

type=direct

before==


import random
random.seed(seed)
x=str(random.randint(0,99))
print("BUILD seed : "+str(seed)+ "  --> "+x)
text+=x


==

evaluator==
grade=True, "Ok"
==
