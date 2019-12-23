import re
def readfile(filename):
	file=open(filename,'r')
	data=re.split(r'\n',file.read())
	while(data[0]!='@DATA'):
		data.pop(0);
	result=[]
	for row in data[1:]:
		raw=re.split(r',',row)
		raw[:4]=[float(x) for x in raw[:4]]
		raw[-1]= 1 if raw[4]=="Iris-setosa" else -1		
		result.append([1]+raw)
	return result;