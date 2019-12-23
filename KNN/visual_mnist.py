from PIL import Image
import csv
import re
import numpy as np
def readfile(filename):
	data=[]
	with open(filename, newline='') as file:
		spamreader=csv.reader(file, delimiter=' ',quotechar='|')
		for row in spamreader:
			instance=re.split(',',row[0])
			data.append(instance)
	return data

def getimage(unit,name):	
	arr=[]
	k=0
	for i in range(28):
		row=[]
		for j in range(28):
			row.append(int(unit[k]))
			k+=1
		arr.append(row)
	pixel=np.array(arr,dtype=np.uint8)
	test=Image.fromarray(pixel)
	test.save('digits/'+name)

data=readfile('data/train.csv')
data.pop(0)


def oneround(j,round):
	index=0
	while index!=10:
		if int(data[j][0])==index:
			getimage(data[j],str(round)+'_'+str(index)+'.png')
			index+=1
		j+=1
	return j

x=oneround(0,1)
x=oneround(x,2)
x=oneround(x,3)
x=oneround(x,4)