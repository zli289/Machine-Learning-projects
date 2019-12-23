import csv
import re

def readfile(filename):
	data=[]
	with open(filename, newline='') as file:
		spamreader=csv.reader(file, delimiter=' ',quotechar='|')
		for index,row in enumerate(spamreader):
			if index%15==0:
				instance=re.split(',',row[0])
				data.append(instance)
	return data

def split(data):
	l_training=int(len(data)*0.8)

	d_training=data[:l_training]
	d_validation=data[l_training:]

	return d_training, d_validation

def distance(x,z,d,p):
	sum=0
	for i in range(d):
		sum+=abs(float(x[i])-float(z[i]))**p
	return sum**(1/p)

def knn(target,d,k):
	predict=0
	dists=[]
	labels=[0,0,0,0,0,0,0,0,0,0]
	for index,row in enumerate(d_training):
		dists.append([index,distance(target,row[1:],d,p=2)])
	dists.sort(key=lambda x:x[1])
	for i in range(k):
		label= int(d_training[dists[i][0]][0])
		labels[label]+=1

	return labels.index(max(labels))

def loss(data,k):
	accuracy=0
	matrix=[[0]*10 for i in range(10)]
	for instance in data:
		prediction=knn(instance,784,k)
		if(prediction!=int(instance[0])):
			accuracy+=1
		matrix[int(instance[0])][prediction]+=1
	return accuracy/len(data),matrix

def evaluation(data,ks):
	results=[]
	print('k 	loss')
	for i in range(ks):
		if (i+1)%3==0:
			goal,table=loss(data,i+1)
			print(i+1,goal)
			results.append(goal)

	return results.index(min(results))+1

def test(d_test):
	result=[]
	for index,row in enumerate(d_test):
		temp=[index+1,knn(row,784,5)]
		print(temp)
		result.append(temp)

	with open('test_submission.csv','w+') as test_submission:
		csvwriter=csv.writer(test_submission,delimiter=',')
		csvwriter.writerows(result)

data=readfile('data/train.csv')
demensions=data.pop(0)
d_training,d_validation=split(data)

#k_optimal=evaluation(d_validation,15)
for k in [1,3,6,9,12]:
	p,matrix=loss(d_validation,k)
	print('loss of validation set is',p)
	for row in matrix:
		print(row)
#d_test=readfile('test.csv')
#d_test.pop(0)
#test(d_test)