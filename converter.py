##open files
inputPath = raw_input('Please enter the path to the data file: ')
input = open(inputPath, 'r')
open('converted.arff', 'w')
output = open('converted.arff', 'a')

##count how many attributes based on commas
line = input.readline()
numAttributes = line.count(',') + 1

##header
output.write('@RELATION ')
output.write(raw_input('Please enter the relation name: ') + '\n')

x = 0
while (x < numAttributes):
    name = raw_input('Please enter attribute name (' + str(x+1) + '/' + str(numAttributes) +'): ')
    type = raw_input('Please enter the data type for "' + name + '": ')

##    shortcuts
    if type == 'nu':
        type = 'NUMERIC'
    elif type == 'no':
        type = '{' + raw_input('Please enter possible cases: ') + '}'
    elif type == 'st':
        type = 'STRING'
    elif type == 'da':
        type = 'DATE'
						
		
    output.write('\n@ATTRIBUTE ' + str(name) + ' ' + str(type) )

    x+= 1

##copy over data from input file
output.write('\n\n@DATA\n' + line)
for line in input:
    output.write(line)

##tidying up
input.close()
output.close()
