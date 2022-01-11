import csv
import math

with open("c105assign/data.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data=file_data[0]
def mean(data):
    sum=0
    for value in data:
        sum +=int(value)
    mean_result=sum/len(data)
    return mean_result

sqr_list=[]
add=0

for val in file_data:
    diff= int(val)- mean(file_data)
    sqr=diff**2
    sqr_list.append(sqr)
    add += sqr

result=add/(len(file_data)-1)
std=math.sqrt(result)
print("Standard deviation is",std)