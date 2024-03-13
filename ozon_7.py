'''
Необходимо напечатать документ из k страниц. Его страницы пронумерованы от 1 до k.
Некоторые его страницы были уже предварительно напечатаны.
Известно, что на принтер было отослано одно задание, которое содержало список страниц для печати.

Этот список содержит хотя бы одну страницу, и хотя бы одна страница от 1 до k не попадает в этот список.
Список страниц состоит из перечисленных через единичную запятую элементов списка, где каждый элемент — это:

∙ либо конкретный номер одной страницы (целое число от 1 до k),
∙ либо диапазон страниц

Выведите кратчайший список страниц в аналогичном формате, который надо дополнительно послать на печать,
чтобы в итоге напечатать все страницы от 1 до k, не напечатанные ранее.
Иными словами, найдите такую наиболее короткую строку,
которая является корректным списком страниц и содержит те и только те страницы, которые еще не были напечатаны.
'''



def del_def(s):
    ml = s.split(',')
    nl = []
    for elem in ml:
        if elem.isdigit():
            nl.append(int(elem))
        elif '-' in elem:
            x = elem.split('-')
            dia = list(range(int(x[0]), int(x[-1]) + 1))
            nl.extend(dia)
    return set(nl)
final_answer = []

n = int(input())

for _ in range(n):
    
    all_pages = int(input())

    already_printed = input()

    ml = del_def(already_printed)
    counter = 0 
    al = set(range(1, all_pages + 1))
    list_to_print = sorted(al.difference(ml))
    ans = []

    for i in range(1, len(list_to_print)):        
        x = list_to_print[i]
        y = list_to_print[i - 1]

        if x - y != 1:
            if counter == 0:
                ans.append(str(y))
            else:
                ans.append(f'{y - counter}-{y}')
                counter = 0
        else:
            counter += 1

    if counter == 0:
        ans.append(str(list_to_print[-1]))
        counter = 0
    else:
        ans.append(f'{list_to_print[-1] - counter}-{list_to_print[-1]}')
        counter = 0

    string_answer = ''
    for elem in ans:
        string_answer += f'{elem},'

    final_answer.append(string_answer.rstrip(','))

print(*final_answer, sep='\n')







