import sys

if __name__ == 'main':
    with open('bakery.csv', 'a') as f:
        f.write(sys.argv[1] + '\n')
    exit()
