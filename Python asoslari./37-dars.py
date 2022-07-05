#import math
#uzunlik = lambda pi, r : 2*r*pi
#print(uzunlik(math.pi, 10))


#kvadrat = lambda x,y : x**y
#print(kvadrat(3, 2))

#def daraja(n):
#    return lambda x :x**n

#kvadrat = daraja(2)

#
#sonlar = list(range(11))
#ildizlar = list(map(sqrt,sonlar))
#print(ildizlar)

#def daraja2(x): 
#    return x*x

#print(list(map(daraja2, sonlar)))

#kvadratlar = list(map(lambda x:x*x, sonlar))
#print(kvadratlar)

#a = [3, 4, 8 ]
#b = [4, 5, 9 ]

#a_plus_b = list(map(lambda x,y:x+y,a,b))
#print(a_plus_b)

import random as r
sonlar  = r.sample(range(100),10)
print(sonlar)
def juftmi(x):
    """x juft bosa true aks holda false qaytaradi"""
    return x%2==0

juft_sonlar = list(filter(juftmi, sonlar))

juft_sonlar = list(filter(lambda x: x%2==0, sonlar))
print(juft_sonlar)


#№2
mevalar = ['olma', 'anjir', 'nok', 'banan', 'klubnika', 'shaftoli', 'uzum']
harf = "a"
mevalar_b = list(filter(lambda  meva:meva.startswith(harf), mevalar))
print(mevalar_b)

mevalar_2= list(filter(lambda meva:len(meva)<=5, mevalar))
print(mevalar_2)
