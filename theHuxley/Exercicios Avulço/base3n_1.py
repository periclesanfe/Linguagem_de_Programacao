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

lista=[]
cont=0
while 1:
    try:
        jIni,iIni=input("").split()
    except:
        break
    lista.append([])
    j,i=int(jIni),int(iIni)
    if(j<i):
        j,i=i,j
    for i in range(i,j+1,1): 
        lista[cont].append(contaCiclo(i))
    print(jIni,iIni,max(lista[cont]))
    cont+=1