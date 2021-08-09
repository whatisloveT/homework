original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for val in original_list:
    if val.isdigit():
        val = f'"{int(val):02d}"'
    elif val.startswith('+') and val[1:].isdigit():
        val = f'"+{int(val[1:]):02d}"'
    print(val, end=' ')