'''
Вам предстоит реализовать простейший алгоритм компрессии последовательности чисел, который предполагает,
что последовательность состоит из подряд идущих возрастающих или убывающих отрезков чисел.
Например, если искомая последовательность имела вид 
a=[3,2,1,0,−1,0,6,6,7], то результат сжатия может иметь вид 
[3,−3,−1,1,6,0,6,1]
Другой возможный результат сжатия: 
[3,−4,0,0,6,0,6,1]
'''


n = int(input())

for _ in range(n):
    m = int(input())


    ml = [int(i) for i in input().split()]

    nl = [ml[0]]

    up_counter = 0
    down_counter = 0

    for i in range(1, len(ml)):
        x = ml[i]
        y = ml[i - 1]
        
        if x - y == 1:
            if down_counter == 0:
                up_counter += 1
            else:
                nl.append(-down_counter)
                down_counter = 0
                nl.append(x)

        elif x - y == -1:
            if up_counter == 0:
                down_counter += 1
            else:
                nl.append(up_counter)
                up_counter = 0
                nl.append(x)

        else:
            if up_counter == 0 and down_counter == 0:
                nl.append(0)
                nl.append(x)

            elif up_counter != 0 and down_counter == 0:
                nl.append(up_counter)
                up_counter = 0
                nl.append(ml[i])
            
            elif up_counter == 0 and down_counter != 0:
                nl.append(-down_counter)
                down_counter = 0
                nl.append(ml[i])

    if up_counter == 0 and down_counter == 0:
        nl.append(0)

    elif up_counter != 0 and down_counter == 0:
        nl.append(up_counter)
    
    elif up_counter == 0 and down_counter != 0:
        nl.append(-down_counter)

    print(len(nl))
    print(*nl)




        


