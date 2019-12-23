count=0
epochs=100000
train_errors=[]

class Weights():
	def __init__(self,arr,rate):
		self.arr=arr
		self.length=len(arr)
		self.rate=rate
		self.result=0

	def activation(self,x):
		self.result=0
		for i in range(self.length):
			self.result+= self.arr[i]*x[i] 
		return 1 if self.result>=0 else -1

	def update(self,x):
		for i in range(self.length):
			self.arr[i]+=x[i]*x[-1]*self.rate

def perceptron(data,weights):
	global count	# Control epochs
	global train_errors	#store accuracy in diffierent epochs
	while(count<epochs):
		count+=1
		errors=0
		for x in data:
			if weights.activation(x)!= x[-1]:
				weights.update(x)
				errors+=1
		train_errors.append(round(1-errors/len(data),3))
		#print("misclassifications: ",errors)
		if errors==0:
			break
	return weights

def crossvalidation(data,k,rate):
	accuracy=0
	weights=Weights(initalweights, rate)
	for i in range(k):
		# splitting data set
		training=data[:]
		validation=training[i*k:i*k+k]
		del training[i*k:i*k+k]
		# training data
		weights=perceptron(training,weights)
		# evaulation weights
		count=0
		for sample in validation:
			if weights.activation(sample)==sample[-1]:
				count+=1
		accuracy+=count/len(validation)

	weights.arr=[round(x,3) for x in weights.arr]
	#print("weights: ",weights.arr)
	return accuracy/k,weights.arr