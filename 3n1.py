def entrada():
    entrada = input().split()
    lista_i, lista_j = [], []

    for v in range(len(entrada)):
        numero = int(entrada[v])
        if v % 2 == 0:
            lista_i.append(numero) 
        else:
            lista_j.append(numero)

    calcular_ciclos(lista_i, lista_j)
    


def calcular_ciclos(lista_i, lista_j):
    list = []
    max_cycles = []
    a = 0
    i = lista_i.pop(a)
    j = lista_j.pop(a)
    
    for n in range(i, j+1):

        while n != 1:   
            if n %2!=0:
                n = 3*n+1
                list.append(n)
        
            else:
                n = n/2
                list.append(n)
                
                if n == 1:
                    max_cycles.append(len(list)+1)
                    list=[]
            
    a = a+1
    print(i, j, max(int(number) for number in max_cycles))
    if len(lista_i) == 0:
        exit
    else:
        calcular_ciclos(lista_i, lista_j)
        
entrada()
