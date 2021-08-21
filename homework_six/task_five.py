import sys

users, hobbys, combined = sys.argv[1:]
if __name__ == 'main':
    from itertools import zip_longest

    print(dir(sys.argv))
    with open(users, 'r') as us, open(hobbys, 'r') as hob:
        names = [i.replace(';', ' ') for i in
                 us.read().splitlines()]
        hobby = [i.replace(';', ',') for i in hob.read().splitlines()]

    users_hobbys_gen = ((names, hobby) for names, hobby in zip_longest(names, hobbys, fillvalue='None'))

    with open(combined, 'w', encoding='utf-8') as f:
        for users_hobbys in users_hobbys_gen:
            f.write(f'{users_hobbys[0]} : {users_hobbys[1]}\n')

    exit()
