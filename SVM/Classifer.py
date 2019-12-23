import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import learning_curve

def evaluation(validation,clf,isall=False):
	if isall:
		test=[attr[:14] for attr in validation]
	else:
		test=[[attr[10],attr[11]] for attr in validation]
	pred=clf.predict(test)
	res=[x[-1] for x in validation]
	
	count=0
	for i in range(len(res)):
		if res[i]==pred[i]:
			count+=1
	return count/len(res),classification_report(res,pred)

def drawBoundary(clf,x,y,isvec=False):
	plt.scatter([xi[0] for xi in x],[xi[1] for xi in x],c=y,s=30,cmap=plt.cm.coolwarm)
	plt.xlabel('Capital gain')
	plt.ylabel('Capital loss')
	ax = plt.gca()
	xlim = ax.get_xlim()
	ylim = ax.get_ylim()
	# create grid to evaluate model
	xx = np.linspace(xlim[0], xlim[1], 30)
	yy = np.linspace(ylim[0], ylim[1], 30)
	YY, XX = np.meshgrid(yy, xx)
	xy = np.vstack([XX.ravel(), YY.ravel()]).T
	Z = clf.decision_function(xy).reshape(XX.shape)
	# plot decision boundary and margins
	ax.contour(XX, YY, Z, colors='k', levels=[-0.5, 0, 0.5], alpha=0.5,
           linestyles=['--', '-', '--'])
	# plot support vectors
	if isvec:
		ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100,
    	    linewidth=1, facecolors='none', edgecolors='k')
	plt.show()


def learningCurve(clf,x,y):
	plt.figure()

	train_sizes, train_scores, test_scores = learning_curve(clf, x, y, cv=10)
	train_scores_mean = np.mean(train_scores, axis=1)
	train_scores_std = np.std(train_scores, axis=1)
	test_scores_mean = np.mean(test_scores, axis=1)
	test_scores_std = np.std(test_scores, axis=1)
	plt.grid()

	plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
	plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
	plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
	plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

	plt.legend(loc="best")
	plt.show()