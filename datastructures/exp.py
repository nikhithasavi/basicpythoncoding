import csv
#file=open('data.csv')
input_file = csv.DictReader(open("data.csv"))
#csvreader=csv.reader(file)
header=next(input_file)
print(header)
custs=set()
for row in input_file:
   #custs.add(row.)
#print(type(row))
    #print(row)

print(custs)
    #rows.append(row)

#input_file.close()
customers=[['nikki', 'shetty', '4455'], ['biddy', 'naidu', '3344'], ['nikki', 'shetty', '5566'], ['jack', 'jill', '2345']]
new_customers=[]
for customer in customers:
    new_customers.append(customer[0]+" "+customer[1])
print(set(new_customers))
#new_file=open('new_users.txt','w')
#new_file.write('new_users')
#new_file.read()
#new_file.close()
#input_file = csv.DictReader(open(".csv"))






