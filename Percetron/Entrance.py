import Readfile
import Perceptrons
import Visualization

def question1():
	ws=[]
	for rate in [0.005,0.001,0.00001]:
		Perceptrons.initalweights=[-1,1,1,1,1]
		accuracy,arr=Perceptrons.crossvalidation(data,10,rate)
		ws.append(arr)
		print("learning rate: ",rate)
		print("accuracy: ",accuracy)
		print("weights:",arr,'\n')
	Visualization.RatesComparsion(ws)

def question2():
	Perceptrons.epochs=20
	ys=[]
	for rate in [0.005,0.001,0.00001]:
		print("learning rate: ",rate)
		Perceptrons.count=0
		Perceptrons.train_errors=[]

		Perceptrons.initalweights=[-1,1,1,1,1]
		accuracy,arr=Perceptrons.crossvalidation(data,10,rate)
		print(Perceptrons.train_errors,'\n')
		ys.append(Perceptrons.train_errors)
	Visualization.AccuracyInEpochs(ys,20)


def question3():
	rate=0.00005
	count=0
	con_ws=Perceptrons.Weights([-1,0,0.5,-0.5,0.5], rate)
	cla_ws=Perceptrons.Weights([-1.101,-0.008,0.652,-0.372,0.412], rate)
	conf=[]
	classf=[]
	col=[]
	for sample in data:
		if con_ws.activation(sample)==sample[-1]:
			count+=1
			col.append('g')
		else: col.append('r')
		conf.append(round(con_ws.result,3))
		cla_ws.activation(sample)
		classf.append(round(cla_ws.result,3))
	Visualization.confidence(conf,classf,col)
	print(count/len(data))

	
data= Readfile.readfile("iris.arff")
#question1()
question2()
#question3()
#question 4
#Visualization.scatterplot(data)
