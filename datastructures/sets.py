import csv

f=open('data.csv','a',newline='')
tuple0=('first_name','last_name','contact')
tuple1=('nikki','shetty',4455)
tuple2=('biddy','naidu',3344)
tuple3=('nikki','shetty',5566)
tuple4=('jack','jill',2345)
writer=csv.writer(f)

writer.writerow(tuple0)
writer.writerow(tuple1)
writer.writerow(tuple2)
writer.writerow(tuple3)
writer.writerow(tuple4)
#print(set[data.csv])

list1=['nikki','shetty',3344,
       'biddy','naidu',5566,
       'nikki','naidu',4567]
print(set(list1))
type(list1)




f.close()
