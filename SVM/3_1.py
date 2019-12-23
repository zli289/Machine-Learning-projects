#Train your SVM with stratiﬁed 10-fold-cross-validation on the 2 features with the highest information gain 
#Visualize your boundary. 
from DataProcess import readfile, infomationGain,crossValidation
from Classifer import drawBoundary 
from sklearn.svm import SVC  

data=readfile('census-income_10percentData.csv')
print('information Gain for all features:')
infomationGain(data)

training,validation=crossValidation(data)

x=[[t[10],t[11]] for t in training]
y=[t[-1] for t in training]

clf = SVC(C=1.0,gamma='scale',kernel='linear') 
clf.fit(x,y)
drawBoundary(clf,x,y,True)



