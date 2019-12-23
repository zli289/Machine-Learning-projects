from DataProcess import readfile,crossValidation
from Classifer import evaluation,learningCurve
from sklearn.ensemble import RandomForestClassifier

data=readfile('census-income_10percentData.csv')
training,validation=crossValidation(data)

x=[[t[10],t[11]] for t in training]
y=[t[-1] for t in training]

clf=RandomForestClassifier(criterion='entropy',n_estimators=10)
clf.fit(x,y)
accuracy,report=evaluation(validation,clf)
print(accuracy)
print(report)

learningCurve(RandomForestClassifier(criterion='entropy',n_estimators=10),x,y)

	