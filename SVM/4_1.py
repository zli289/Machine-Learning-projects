# Compare the performance (precision, recall, f1-score, and variance) of diﬀerent kernels: Linear, RBF, and polynomial.
from DataProcess import readfile,crossValidation
from Classifer import evaluation
from sklearn.svm import SVC

data=readfile('census-income_10percentData.csv')
training,validation=crossValidation(data)

x=[[t[10],t[11]] for t in training]
y=[t[-1] for t in training]

linear= SVC(C=1.0,gamma='scale',kernel='linear') 
rbf= SVC(C=1.0,gamma='auto',kernel='rbf')
poly= SVC(C=1.0,gamma='scale',kernel='poly')  

clfs=[linear,poly,rbf]
labels=['linear','poly','rbf']
for i,clf in enumerate(clfs):
	clf.fit(x,y)
	accuracy,report=evaluation(validation,clf)
	print(labels[i],accuracy)
	print(report)

	