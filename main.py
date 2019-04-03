import matplotlib as mpl
from random import randint
mpl.use('Agg')
import matplotlib.pyplot as plt
import timeit

def desenhaGrafico(caso,x,y, yl = "Saídas",xl = "Entradas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    for i in range (len(y)):
      ax.plot(x,y[i], label = caso[i])
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(yl+'_graph.png')
 
def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def geraListaOrd(tam):
  lista = []
  for i in range(tam):
    lista.append(i)
  return lista

def geraListaInv(tam):
  lista = []
  for i in range(tam):
    lista.append(tam-i)
  return lista

def permutacao(lis):
	comb = []
	for a in lis:
		for b in lis:
			if b!=a:
				for c in lis:
					if c!=a and c!=b:
						for d in lis:
							if d!=a and d!=b and d!=c:
								for e in lis:
									if e!=a and e!=b and e!=c and e!=d:
										for f in lis:
											if f!=a and f!=b and f!=c and f!=d and f!=e:
												comb.append([a]+[b]+[c]+[d]+[e]+[f])
	return comb

def novaOrdem(ordem, lista):
  if len(lista)>5:
    z = [[],[],[],[],[],[]]
    for i in range(6):
      z[i] = novaOrdem(ordem, lista[int((len(lista)/6)*i):int((len(lista)/6)*(i+1))])
    return z[ordem[0]-1]+z[ordem[1]-1]+z[ordem[2]-1]+z[ordem[3]-1]+z[ordem[4]-1]+z[ordem[5]-1]
  else:
    z=[]
    w = ordem[:]
    for i in range(len(ordem)-len(lista)):
      w.remove(6-i)
    for i in range(len(lista)):
      z.append(lista[w[i]-1])
    return z

def mergeSort(lista):
  w = []
  z = []
  if len(lista)>1:
    w = mergeSort(lista[0:int(len(lista)/2)])
    z = mergeSort(lista[int(len(lista)/2):len(lista)])
  else:
    return lista  
  listaFinal = []
  nw=0
  nz=0
  for i in range(0, len(w)+len(z)):
    if nw < len(w):
      if nz < len(z):
        if w[nw]<z[nz]:
          listaFinal.append(w[nw])
          nw = nw+1
        else:
          listaFinal.append(z[nz])
          nz = nz+1
      else:
        listaFinal[i:] = w[nw:]
        return listaFinal
    else:
      listaFinal[i:] = z[nz:]
      return listaFinal
  return listaFinal

funcao = 'mergeSort({})'
setupfuncao = "from __main__ import "+funcao[:-4]

x = [1000, 2000, 4000, 5000]
y = [[],[],[],[],[]]

for i in x:
  lis = geraLista(i)
  y[0].append(timeit.timeit(funcao.format(lis),setup=setupfuncao,number=1))

for i in x:
  lis = geraListaOrd(i)
  y[1].append(timeit.timeit(funcao.format(lis),setup=setupfuncao,number=1))

for i in x:
  lis = geraListaInv(i)
  y[2].append(timeit.timeit(funcao.format(lis),setup=setupfuncao,number=1))

w = permutacao([1, 2, 3, 4, 5, 6])
z=[]
melhor = 0
pior = 0
for i in w:
  z.append(timeit.timeit(funcao.format(i),setup=setupfuncao,number=1))

for i in range(len(z)):
  if z[i] > z[pior]: pior = i
  if z[i] < z[melhor]: melhor = i 

for i in x:
  lista = geraListaOrd(i)
  lis = novaOrdem(w[melhor], lista)
  y[3].append(timeit.timeit(funcao.format(lis),setup=setupfuncao,number=1))

for i in x:
  lista = geraListaOrd(i)
  lis = novaOrdem(w[pior], lista)
  y[4].append(timeit.timeit(funcao.format(lis),setup=setupfuncao,number=1))

caso = ["Aleatória", "Ordenada", "Invertida","melhor casos: "+str(w[melhor]),"pior casos: "+str(w[pior])]

desenhaGrafico(caso,x,y, "Tempo")



