import math

import csv
with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):
    n=len(data)
    total = 0
    for x in data:
        total += int(x)

    mean = total/n
    return mean
squared_list =[]
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squared_list.append(a)


sum = 0
for i in squared_list:
    sum = sum +1

result = sum/(len(data)-1)

sDeviation = math.sqrt(result)
print(sDeviation)
            
