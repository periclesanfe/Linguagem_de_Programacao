def contaCiclo(num):
  ciclo=0
  while 1:
    ciclo+=1
    if(num<=1):
      return ciclo
    if num%2==0:
      num=num//2
    else:
      num=(num*3)+1
  return 0

listaCiclo=[]
contLista=0
while 1:
    try:
        jInicial,iInicial=input("").split()
    except:
        break
    listaCiclo.append([])
    j,i=int(jInicial),int(iInicial)
    if(j<i):
        j,i=i,j
    for i in range(i,j+1,1): 
        listaCiclo[contLista].append(contaCiclo(i))
    print(jInicial,iInicial,max(listaCiclo[contLista]))
    contLista+=1