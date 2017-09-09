input = open('abalone/abalone.data', 'r')
output = open('output.data', 'w')

line = input.readline()
numAttributes = line.count(line, ',')

output.append('@REALATION ')
output.append(raw_input('Please enter the relation name: '))

# output.append('@DATA ')
# for (i = 0, i <= numAttributes + 1 , i++)

input.close()
output.close()