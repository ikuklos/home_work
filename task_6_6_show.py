import sys
print(len(sys.argv))
if len(sys.argv) <= 1:
    with open('bakery.csv', 'r') as bakery:
        for line in bakery:
            print(line[:-1])
elif len(sys.argv) == 2:
    with open('bakery.csv', 'r') as bakery:
        count = 0
        for line in bakery:
            count += 1
            if int(sys.argv[1]) == count:
                print(line[:-1])
else:
    with open('bakery.csv', 'r') as bakery:
        count = 0
        _temp_list = []
        for line in bakery:
            count += 1
            if int(sys.argv[2]) >= count and int(sys.argv[1]) <= count:
                _temp_list.append(line)
        for element in _temp_list:
            print(element[:-1])