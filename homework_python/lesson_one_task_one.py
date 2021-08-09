second = None
minute = None
hour = None
day = None
final_print = None
for i in range(5):
    duration = int(input('Введите кол-во секунд : '))
    if duration // 60 != 0:
        second = str(duration % 60) + ' sec '
        duration //= 60
        if duration // 60 != 0:
            minute = str(duration % 60) + ' min '
            duration //= 60
            if duration // 24 != 0:
                hour = str(duration % 24) + ' hour '
                duration //= 24
                day= str(duration % 365) + ' day '
                final_print = day + hour + minute + second
            else:
                hour = str(duration % 24) + ' hour '
                final_print = hour + minute + second
        else:
            minute = str(duration % 60) + ' min '
            final_print = minute + second
    else:
        second = str(duration % 60) + ' sec '
        final_print = second
    print(final_print)
