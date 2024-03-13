# n = int(input())
template = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
for _ in range(int(input())): 
    ml = [int(i) for i in input().split()]
    if sorted(ml) == template:
        print('YES')
    else:
        print('NO')