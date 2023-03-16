while True:
    sub = float(input())
    if sub == -1:
        break
    if sub < 7:
        print("ACIDA")
    elif sub > 7:
        print("BASICA")
    else:
        print("NEUTRA")
