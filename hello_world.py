import json
import csv
#计算和
sum = 0
list = []
bright_file="/tcdata/num_list.csv"
csvFile = open(bright_file, "r")
reader1=csv.reader(csvFile)
for item in reader1:
    sum+=int(item[0])
#计算最大的10个
temp=[]
csvFile2 = open(bright_file, "r")
reader2=csv.reader(csvFile2)
for item in reader2:
    temp.append(int(item[0]))
temp.sort(reverse = True)
for i in range(10):
    list.append(temp[i])

data = {"Q1": "Hello world", "Q2": sum, "Q3": list}

with open("result.json","w") as fw:
    data2 = json.dumps(data)
    fw.write(data2)
