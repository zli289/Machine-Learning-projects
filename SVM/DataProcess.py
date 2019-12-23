import csv
import re
import statistics
from info_gain import info_gain
import matplotlib.pyplot as plt

def readfile(filename):
	data=[]
	with open(filename, newline='') as file:
		spamreader=csv.reader(file, delimiter=' ',quotechar='|')
		for row in spamreader:
			instance=re.split(',',row[0])
			data.append(instance)
	data.pop(0)
	replaceMissing(data)
	convertfeatures(data)
	return data

def showMissing(data):
	nums=[0 for i in range(len(data[0]))]
	columns=[]
	for row in data:
		for index, attr in enumerate(row):
			if attr=='?':
				nums[index]+=1
				if index not in columns:
					columns.append(index)
	print(columns)
	plt.bar(titles,nums)
	plt.show()
#	2-1	Replacing missing features
def replaceMissing(data):
	# find modes for each attributes
	columns=[1,6,13]	
	modes={}
	for index in columns:
		modes[index]=(statistics.mode([x[index] for x in data]))
	# replace missisng with modes
	for row in data:
		for index in columns:
			if row[index] =='?':
				row[index]=modes[index] 
	return data
#	2-2	 Dealing with discrete (categorical) features
def convertfeatures(data):
	features=[{} for i in range(9)]
	nums=[0 for i in range(9)]
	for row in data:
		#numerics
		for column in [0,2,4,10,11,12]:
			row[column]=int(row[column])
			if column in [2,10,11]:
				row[column]*=0.0001
		#nominals
		for index,column in enumerate([1,3,5,6,7,8,9,13,14]):
			value=row[column]
			if value not in features[index]:
				features[index][value]=nums[index]
				nums[index]=1 if column in [8,13] else nums[index]+1
			row[column]=features[index][value]
	#for f in features:
	#	print(f)
	return data
#	2-3	 10-fold-cross validation
def crossValidation(data):
	k=int(len(data)/10)
	y_train=[]
	y_test=[]
	y_tes=[]
	for i in range(10):
		# splitting data set
		training=data[:]
		validation=training[i*k:i*k+k]
		del training[i*k:i*k+k]

		y_train.extend(training)
		y_test.extend(validation)

	return y_train,y_test
#	2-4	information gain	
def infomationGain(data):
	label=[x[-1] for x in data]
	for i in range(len(data[0])-1):
		attribute=[x[i] for x in data]
		ig=info_gain.info_gain_ratio(label,attribute)
		print(ig)
	draw(data)

def draw(data):
	x=[]
	y=[]
	col=[]
	for row in data:
		x.append(row[10])
		y.append(row[11])
		if row[-1]==1:
			col.append('r')
		else: col.append('b')
	
	plt.scatter(x,y,color=col)
	plt.show()
	





