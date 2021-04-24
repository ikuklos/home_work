import sys
with open('bakery.csv', 'a') as bakery:
    bakery.writelines(sys.argv[1].encode(encoding='UTF-8')+'\n')