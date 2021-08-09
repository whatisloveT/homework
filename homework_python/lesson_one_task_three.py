for i in range(1, 101):
    i = str(i)
    if i[-1] == '1' and i != '11':
        print(f'{i} процент')
    if i[-1] == '2' and i != '12':
        print(f'{i} процента')
    if i[-1] == '3' and i != '13':
        print(f'{i} процента')
    if i[-1] == '4' and i != '14':
        print(f'{i} процента')
    if i[-1] == '5' or i[-1] == '6' or i[-1] == '7' or i[-1] == '8' or i[-1] == '9' or i[-1] == '0' or i == '11' or i == '12' or i == '13' or i == '14':
        print(f'{i} процентов')