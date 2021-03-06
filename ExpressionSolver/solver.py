import add
import multiply

class Solver:

	def getListOfReactionsToPlot(self):
		list1 = []
		finalAnswer = 'x' + str(self.chemicalNumber - 1)
		list1.append(finalAnswer)

		return list1

	def getEstimatedTimeForCompletion(self):
		return self.estimatedTime + int(0.05*self.estimatedTime)

	def getTheoriticalResult(self):
		return self.currVal

	def __init__(self,initValue):
		self.chemicalNumber = 0
		self.functionNumber = 1

		self.currVal = initValue
		self.estimatedTime = 0

		self.reactions = []
		self.absenseDict = dict()
		self.initDict = dict()

		startChemical = 'x' + str(self.chemicalNumber)
		self.initDict[startChemical] = initValue

		self.initDict['g'+str(self.functionNumber)] = 1

		self.chemicalNumber+=1

	def multiply(self,value):
		x = self.currVal
		y = value
		self.estimatedTime += (x*(x+1) + 2*x*(y+2) + 1)
		self.currVal*=value;

		input1 = 'x' + str(self.chemicalNumber - 1)
		input2 = 'x' + str(self.chemicalNumber)
		output = 'x' + str(self.chemicalNumber + 1)

		self.initDict[input2] = value

		self.reactions.extend(multiply.getListOfReactions(input1,input2,output,self.absenseDict,self.functionNumber))

		self.chemicalNumber+=2
		self.functionNumber+=1

		self.reactions.append('')

	def add(self,value):
		x = self.currVal
		y = value
		self.estimatedTime += (x + y + 1)
		self.currVal+=value;

		input1 = 'x' + str(self.chemicalNumber - 1)
		input2 = 'x' + str(self.chemicalNumber)
		output = 'x' + str(self.chemicalNumber + 1)

		self.initDict[input2] = value

		self.reactions.extend(add.getListOfReactions(input1,input2,output,self.absenseDict,self.functionNumber))

		self.chemicalNumber+=2
		self.functionNumber+=1

		self.reactions.append('')

	def getStringFromDict(self,myDict):
		finalAnswer = []

		for key in myDict:
			val = myDict[key]
			finalAnswer.append(key+' -> '+str(val)+'\n')

		return ''.join(finalAnswer)

	def getStringFromList(self,myList):
		finalAnswer = []

		for val in myList:
			finalAnswer.append(val+'\n')

		return ''.join(finalAnswer)


	def printTxt(self,fileName):
		reactionFile = open(fileName,'w')

		reactionFile.write('Absence:\n')
		reactionFile.write(self.getStringFromDict(self.absenseDict))

		reactionFile.write('\n')

		reactionFile.write('Reactions:\n')
		reactionFile.write(self.getStringFromList(self.reactions))

		reactionFile.write('\n')

		reactionFile.write('Concentrations:\n')
		reactionFile.write(self.getStringFromDict(self.initDict))




