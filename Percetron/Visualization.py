import matplotlib.pyplot as plt
import pandas as pd

def RatesComparsion(y):
	x=['0.005','0.001','0.00005']

	plt.title('Each weight in different rates') 
	plt.xlabel('Rates')
	plt.ylabel('Values')

	for i in range(5):
		plt.plot(x,[y[0][i],y[1][i],y[2][i]],color='blue', marker='o')
	plt.show()

def AccuracyInEpochs(y,epochs):
	x=[]
	for i in range(epochs):
		x.append(i+1)
	colors=['r','g','b']
	labels=[0.005,0.001,0.00001]

	plt.title('Classiﬁcation accuracy in epochs')
	plt.xlabel('Epochs')
	plt.ylabel('Accuracy')

	for i in range(3):
		plt.plot(x,y[i], marker='o',label=labels[i],color=colors[i])
	plt.legend()
	plt.show()

def scatterplot(data):
	x1=[]
	y1=[]
	x2=[]
	y2=[]

	for row in data[:50]:
		x1.append(row[1]+row[2])
		y1.append(row[3]+row[4])
	for row in data[51:]:
		x2.append(row[1]+row[2])
		y2.append(row[3]+row[4])

	plt.scatter(x1,y1,color='r')
	plt.scatter(x2,y2,color='g')
	plt.xlabel('Length')
	plt.ylabel('Width')
	plt.show()

def confidence(x,y,col):
	for i in range(len(x)):
		plt.scatter(x[i],y[i],color=col[i])
	
	plt.xlabel('Confidence')
	plt.ylabel('Classiﬁcation')
	plt.show()
