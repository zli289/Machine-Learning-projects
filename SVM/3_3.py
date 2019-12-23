#Train the SVM using all the features. 
#Find a way to determine the optimal value of C. 
#Report your methodology and accuracy from stratiﬁed 10-fold-cross-validation by using learning curves.
from DataProcess import readfile,crossValidation
from Classifer import evaluation,learningCurve
from sklearn.svm import LinearSVC

data=readfile('census-income_10percentData.csv')
training,validation=crossValidation(data)

x=[t[:14] for t in training]
y=[t[-1] for t in training]

for i in range(-5,5):
	clf = LinearSVC(C=10.0**i,dual=False) 
	clf.fit(x,y)
	print('C=',10**i,end=' accuracy:')
	accuracy,report=evaluation(validation,clf,True)
	print(accuracy)

learningCurve(LinearSVC(C=10000,dual=False) ,x,y)
