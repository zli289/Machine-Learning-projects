#Change the hyper-parameter C from small to larger values. 
#Report your observations on how the value of C would aﬀect SVM’s performance. 
#Draw the decision boundaries and margins with smaller and larger values of C to explain its eﬀect in two separate ﬁgures.
from DataProcess import readfile,crossValidation
from Classifer import evaluation,drawBoundary
from sklearn.svm import LinearSVC

data=readfile('census-income_10percentData.csv')
training,validation=crossValidation(data)

x=[[t[10],t[11]] for t in training]
y=[t[-1] for t in training]

for i in range(-5,5):
	clf = LinearSVC(C=10.0**i,dual=False) 
	clf.fit(x,y)
	print('C=',10**i,end=' accuracy:')
	accuracy,report=evaluation(validation,clf)
	print(accuracy)

for c in [1e-4,1.0]:
	clf = LinearSVC(C=c,dual=False) 
	clf.fit(x,y)
	drawBoundary(clf,x,y)
