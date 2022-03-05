# importing csv module
import csv
import json

# csv file name
filename = "data.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows
print('\nFirst 3 rows are:\n')
for row in rows[:3]:
    # parsing each column of a row
    for col in row:
        print("%10s"%col,end=" "),
    print('\n')
    print(type(row))
print(set(row))
print(len(row))

#new program
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-4: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
new_list=[1, 2, 4, 1, 2, 3, (5, 6), ['For', 'Geeks']]
#print(type(new_list))
#print(set(new_list))
input_file = csv.DictReader(open("data.csv"))
#for row in input_file:
#print(json.dumps(rows).replace('nikki','kinni'))
#print(json.dumps(rows).join(['oo','cc','ll']))
#print(json.dumps(rows).find('kinni'))
#print(json.dumps(rows).capitalize())
#a='ab'
#print(a.capitalize())
#print(json.dumps(rows).format())
a='ai how are you doing'
print(a.join('h?'))
a=[9,1,2]
set(a)
print(set(a))
print(set(a).discard(9))

#y = json.dumps('data.csv')
#print(y)
#print(set(y))
#a=open('data.csv')
#a.append()
#print(a)
#print(ty)