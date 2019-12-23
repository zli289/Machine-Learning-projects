import csv
import re

def readfile(filename):
	data=[]
	with open(filename, newline='') as file:
		spamreader=csv.reader(file, delimiter=' ',quotechar='|')
		for row in spamreader:
			instance=re.split(',',row[0])
			data.append(instance)
	return data

def split(data):
	l_training=int(len(data)*0.8)
	l_validation=int(len(data)*0.9)

	d_training=data[:l_training]
	d_validation=data[l_training:l_validation]
	d_test=data[l_validation:]

	return d_training, d_validation, d_test

def split_scale(data):
	negtive=[]
	postive=[]
	for i in data:
		if i[8]=='1':
			postive.append(i)
		else: negtive.append(i)

	pset=split(postive)
	nset=split(negtive)

	return nset[0]+pset[0],nset[1]+pset[1],nset[2]+pset[2]

def distance(x,z,d,p):
	sum=0
	for i in range(d):
		sum+=abs(float(x[i])-float(z[i]))**p
	return sum**(1/p)

def knn(target,d,k):
	predict=0
	dists=[]
	for index,row in enumerate(d_training):
		dists.append([index,distance(target,row,d,p=1)])
	dists.sort(key=lambda x:x[1])
	for i in range(k):
		if d_training[dists[i][0]][8]=='1':
			predict+=1
		else: predict-=1

	return True if predict>=0 else False

def loss(data,k):
	accuracy=0
	matrix={'false positive':0,'false negative':0,'true positive':0,'true negative':0}
	for instance in data:
		prediction=knn(instance,8,k)
		if(prediction!=int(instance[8])):
			accuracy+=1
			if int(instance[8])==1:
				matrix['false positive']+=1
			else: matrix['false negative']+=1
		else:
			if int(instance[8])==1:
				matrix['true positive']+=1
			else: matrix['true negative']+=1

	return accuracy/len(data), matrix

def evaluation(data,ks):
	results=[]
	print('k 	loss')
	for i in range(ks):
		goal,matrix=loss(data,i+1)
		print(i+1,goal)
		results.append(goal)
	return results.index(min(results))+1


data=readfile('data/diabetes.csv')
demensions=data.pop(0)
d_training,d_validation,d_test=split_scale(data)

k_optimal=evaluation(d_validation,15)
print('optimal k=',k_optimal)
p,matrix=loss(d_test,k_optimal)
print('loss of test set is',p)
for row in matrix.items():
	print(row)