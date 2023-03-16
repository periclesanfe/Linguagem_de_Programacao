# description: zerinho ou um

A, B, C = int(input()), int(input()), int(input())

if A == B and A != C:
    print('C\n')
elif B == C and B != A:
    print('A\n')
elif A == C and A != B:
    print('B\n')
else:
    print('*\n')
