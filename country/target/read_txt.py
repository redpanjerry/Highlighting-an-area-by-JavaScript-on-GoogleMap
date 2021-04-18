# import re

# path = '/Users/jerryw/Desktop/map/test/gix_coutry/target/taiwan.txt'
# file = open(path, 'r')

# for line in file:
#     line = line.replace(' ', '\r\n')
#     print(str(line))

# file.close()

import re

path = '/Users/jerryw/Desktop/map/test/gix_coutry/target/taiwan.txt'
file = open(path, 'r')

for line in file:
    line = line.replace(' ', '\r\n')
    print(line)

file.close()
