import pandas as pd
import numpy as np
list1={'name':['Jack','Jill','Lio', 'Lisa','neo'],'age':[1,2,3,4,5]}
df=pd.DataFrame(list1)
print('dataframe')
print(df)
#name selection
print('selecting single column')
print(df[['name']])
#row selection
print('selecting row')
data = pd.read_csv('data.csv',index_col='last_name')
first = data.loc["naidu"]
#second = data.loc["biddy"]


print(first) #"\n\n\n", second)
data = pd.read_csv("data.csv", index_col ="last_name")

# retrieving columns by indexing operator
first = data["first_name"]
print('unique elements in first_name:')
print(set(first))
data = pd.read_csv("data.csv", index_col ="first_name")

# retrieving columns by indexing operator
last = data["last_name"]
print('unique elements in last_name:')
print(set(last))


df = pd.DataFrame(data)
data = pd.read_csv("data.csv")
df = pd.DataFrame(data)

# select two columns
print('selecting 2 columns')
print(df[['first_name', 'last_name']])
print('new list')
new_list=df[['first_name', 'last_name']]
print(new_list)

#print(df)



#print(first)
data = pd.read_csv("data.csv", index_col ="contact")


# retrieving rows by iloc method
row_using_index = data.iloc[3]
print('rows using indexing')
print(row_using_index)

#isnull function
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, np.nan, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}

# creating a dataframe from list
df = pd.DataFrame(dict)

# using isnull() function
df.isnull()