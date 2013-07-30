import csv

# IMPORT DATA
sepal_length, sepal_width, petal_length, petal_width, species = [], [], [], [], []
with open('iris.csv', 'rU') as file:
    csv_object = csv.reader(file, delimiter=',', quotechar='"')
    for row in csv_object:
        sepal_length.append(row[0])
        sepal_width.append(row[1])
        petal_length.append(row[2])
        petal_width.append(row[3])
        species.append(unicode(row[4], 'utf-8'))

# Remove header row
sepal_length = sepal_length[1:]
sepal_width = sepal_width[1:]
petal_length = petal_length[1:]
petal_width = petal_width[1:]
species = species[1:]

# Set numbers to proper format
sepal_length = [float(x) for x in sepal_length]
sepal_width = [float(x) for x in sepal_width]
petal_length = [float(x) for x in petal_length]
petal_width = [float(x) for x in petal_width]



# SETUP
unknown_flower = [3.1, 3.1, 5.2, 1.9]
k = 3

def distance(known, unknown):
    a = known[0] - unknown[0]
    b = known[1] - unknown[1]
    c = known[2] - unknown[2]
    d = known[3] - unknown[3]
    
    DIST = (a**2 + b**2 + c**2 + d**2) ** 0.5

    return DIST














"""
print "Writing to file..."

if os.path.isfile('/Users/acpigeon/Desktop/testingAdvertisers/output.csv'):
    os.remove('/Users/acpigeon/Desktop/testingAdvertisers/output.csv')

output_file = csv.writer(open('output.csv', 'ab'), delimiter=",", quotechar='"')
for utf8_row in output:
    row = [utf8_row[x].encode('utf8') if isinstance(utf8_row[x], unicode) else utf8_row[x] for x in range(len(utf8_row))]
    output_file.writerow(row)
"""