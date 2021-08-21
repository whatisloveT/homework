import sys

if __name__ == 'main':
    interval = list(map(sys.argv[1:]))
    with open('bakery.csv') as f:
        text = f.readlines()
        if len(interval) == 2:
            for line in text[interval[0]-1:interval[1]]:
                print(line.strip())
        elif len(interval) == 1:
            for line in text[interval[0]:]:
                print(line.strip())
        else:
            for line in text:
                print(line.strip())
    exit()