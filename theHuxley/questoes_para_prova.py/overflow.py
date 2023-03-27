n = int(input())
P, C, Q = input().split()
if C == '*':
    if (int(P) * int(Q)) <= n:
        print('OK')
    else:
        print('OVERFLOW')
elif C == '+':
    if (int(P) + int(Q)) <= n:
        print('OK')
    else:
        print('OVERFLOW')
