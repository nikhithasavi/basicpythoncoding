import csv
file=open("data.csv")
csvreader=csv.reader(file)
header=next(csvreader)
print(header)
rows=[]
for row in csvreader:
    rows.append(row)
print(rows)
file.close()
print("Total no. of rows: %d"%(csvreader.line_num))

