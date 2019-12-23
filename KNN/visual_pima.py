import csv
import re
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
#import seaborn as sns 
#sns.set()
#import warnings
#warnings.filterwarnings('ignore')


def readfile(filename):
	data=[]
	with open(filename, newline='') as file:
		spamreader=csv.reader(file, delimiter=' ',quotechar='|')
		for row in spamreader:
			instance=re.split(',',row[0])
			data.append(instance)
	return data

def scatter_plot(data):
	p=scatter_matrix(data,figsize=(30,30))
	plt.show()
def histogram(data):
	data.hist(figsize=(20,20))
	plt.show()

data=pandas.read_csv('data/diabetes.csv')
histogram(data)
