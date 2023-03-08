def equacao(n):
  maxima=0
  while 1:
    maxima+=1
    if n <= 1:
      return maxima
    elif n % 2 == 0:
        n = n//2
    else:
        n = (n*3)+1
  return 0

lista=[]
contador=0
while 1:
  try:
      pri,sec=input('').split()
  except:
      break
  lista.append([])
  i, j = int(pri),int(sec)
  if(i>j):
    i,j=j,i
  for index in range(i, j+1,1):
      lista[contador].append(equacao(index))
  print(pri,sec,max(lista[contador]))
  contador+=1
  
