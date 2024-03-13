'''10
10 9 2022
21 9 2022
29 2 2022
31 2 2022
29 2 2000
29 2 2100
31 11 1999
31 12 1999
29 2 2024
29 2 2023
'''



n = int(input())
for i in range(n):
    ml = [int(i) for i in input().split()]
    if ml[1] in (4, 6, 9, 11):
        print('YES' if ml[0] < 31 else 'NO')
    elif ml[1] in (1, 3, 5, 7, 8, 10, 12):
        print('YES' if ml[0] < 32 else 'NO')
    else:
        if (ml[2] % 4 == 0 and ml[2] % 100 != 0) or ml[2] % 400 == 0:
            print('YES' if ml[0] < 30 else 'NO')
        else:
            print('YES' if ml[0] < 29 else 'NO')


