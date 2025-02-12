from anytree import Node,RenderTree
from anytree.exporter import DotExporter
from graphviz import render

checkRange = range(0,4)

def BFSMethod():
	state = [3,3,0,0]
	complete = False
	stateSet = []
	stateSet.append(state)
	complete = False
	counter = 0
	completeLength =0

	while not complete:
		currState = stateSet[counter]

		currMen = currState[0]
		currCannibal = currState[1]
		currSide = currState[2]
		parentState =currState[3]
		if(currMen == 0 and currCannibal ==0 and currSide==1):	#Condition Complete
			completeLength = counter
			complete = True
			continue
		elif currSide==2:  	 #for error
			counter+=1
			continue
		else:
			if(currMen in checkRange and currCannibal in checkRange):		#To check if within bounds
				if(currMen==0 or currMen==3 or currMen==currCannibal):		#For conditions where cannibal outnumber men
					side = 1-currSide
					temp =[]				#TempSet variable

					compareSet = []			#Set without the parent index
					parentState = stateSet[currState[3]]		#Get the parent of the currentState
					compareSet.append([parentState[0],parentState[1],parentState[2]])

					if(currSide == 0):			#If in left side decrease
						temp.append([currMen-1,currCannibal,side,counter])
						temp.append([currMen,currCannibal-1,side,counter])
						temp.append([currMen-1,currCannibal-1,side,counter])
						temp.append([currMen-2,currCannibal,side,counter])
						temp.append([currMen,currCannibal-2,side,counter])
					else:						#If in right side increase
						temp.append([currMen+1,currCannibal,side,counter])
						temp.append([currMen,currCannibal+1,side,counter])
						temp.append([currMen+1,currCannibal+1,side,counter])
						temp.append([currMen+2,currCannibal,side,counter])
						temp.append([currMen,currCannibal+2,side,counter])

					for val in temp:
						if(val[0] in checkRange and val[1] in checkRange):		#if the added value is within range
							valSet=[val[0],val[1],val[2]]
							if(valSet not in compareSet):				#if the state already exists in the tree
								stateSet.append(val)


		counter+=1

	# Building the tree
	print("---------------------")
	counter = 1
	nodes =[]
	nodes.append(Node(str([3,3,0,0])))
	while counter<=completeLength:
		parentNode = nodes[(stateSet[counter][3])]
		nodes.append(Node(str(stateSet[counter]),parent = parentNode))
		counter+=1

	fileLoc = "E:/7th Sem/Artificial Intelligence/Assignments/Assignment 2/BFSTree.dot"
	DotExporter(nodes[0]).to_dotfile(fileLoc)
	render('dot','png',fileLoc)

	# Building the path only for the BFS tree
	states = []
	count = completeLength
	currState = stateSet[count]
	currCompareValues = [currState[0],currState[1],currState[2]]
	while currCompareValues!=[3,3,0]:
		states.append(currCompareValues)
		count = currState[3]
		currState = stateSet[count]
		currCompareValues = [currState[0],currState[1],currState[2]]

	states.append([3,3,0]) #It wont be added due to the while condition
	states.reverse()
	nodes =[]
	nodes.append(Node(str([3,3,0])))
	count =1
	while count < len(states):
		parentNode = nodes[count-1]
		nodes.append(Node(str(states[count]),parent = parentNode))
		count+=1

	fileLoc = "E:/7th Sem/Artificial Intelligence/Assignments/Assignment 2/BFSTreeFinal.dot"
	DotExporter(nodes[0]).to_dotfile(fileLoc)
	render('dot','png',fileLoc)

#In DFS we take values from the end of the list because we tried to mimic that of stack 
#I didnt use stack beacuse we would have to use pop operation to get the top value which would take the value
#out of stack which was necessary for the next steps
#visited boolean helped to identify if some of the nodes were already visited or not
def DFS():       
	state = [3,3,0,0,False]				#[men,cannibal,side,parent,visited]
	complete = False
	stateSet = []
	stateSet.append(state)

	complete = False
	completeLength =0
	counter =0

	while not complete:
		decCounter = 1
		counter = len(stateSet)-decCounter
		currState = stateSet[counter]
		while(currState[4]):
			decCounter+=1
			counter = len(stateSet)-decCounter
			currState = stateSet[counter]
		currState[4] = True

		currMen = currState[0]								#Getting current state values
		currCannibal = currState[1]
		currSide = currState[2]

		# print(currState)
		if(currMen == 0 and currCannibal ==0 and currSide==1):	#Condition Complete
			complete = True
			break
		elif currSide==2:  	 #for error
			continue
		else:
			if(currMen in checkRange and currCannibal in checkRange):		#To check if within bounds
				if(currMen==0 or currMen==3 or currMen==currCannibal):		#For conditions where cannibal outnumber men
					side = 1-currSide
					temp =[]				#TempSet variable

					compareSet = []			#Set without the parent index
					for i in stateSet:
						compareSet.append([i[0],i[1],i[2]])

					if(currSide == 0):			#If in left side decrease
						temp.append([currMen-1,currCannibal,side,counter,False])
						temp.append([currMen,currCannibal-1,side,counter,False])
						temp.append([currMen-1,currCannibal-1,side,counter,False])
						temp.append([currMen-2,currCannibal,side,counter,False])
						temp.append([currMen,currCannibal-2,side,counter,False])
					else:						#If in right side,counter,False increase
						temp.append([currMen+1,currCannibal,side,counter,False])
						temp.append([currMen,currCannibal+1,side,counter,False])
						temp.append([currMen+1,currCannibal+1,side,counter,False])
						temp.append([currMen+2,currCannibal,side,counter,False])
						temp.append([currMen,currCannibal+2,side,counter,False])

					for val in temp:
						if(val[0] in checkRange and val[1] in checkRange):		#if the added value is within range
							valSet=[val[0],val[1],val[2]]
							if(valSet not in compareSet):				#if the state already exists in the tree
								stateSet.append(val)


	# Building the tree
	print("---------------------")
	counter = 1
	nodes =[]
	nodes.append(Node(str([3,3,0,0])))
	for i in stateSet:
		print(str(i))
	while counter< len(stateSet):
		parentNode = nodes[(stateSet[counter][3])]
		nodes.append(Node(str([stateSet[counter][0],stateSet[counter][1],stateSet[counter][2]]),parent = parentNode))
		counter+=1

	fileLoc = "E:/7th Sem/Artificial Intelligence/Assignments/Assignment 2/DFSTree.dot"
	DotExporter(nodes[0]).to_dotfile(fileLoc)
	render('dot','png',fileLoc)

	# Building the path only for the DFS tree
	states = []
	count = len(stateSet)-1
	currState = stateSet[count]
	currCompareValues = [currState[0],currState[1],currState[2]]
	while currCompareValues!=[3,3,0]:
		states.append(currCompareValues)
		count = currState[3]
		currState = stateSet[count]
		currCompareValues = [currState[0],currState[1],currState[2]]

	states.append([3,3,0]) #It wont be added due to the while condition
	states.reverse()
	nodes =[]
	nodes.append(Node(str([3,3,0])))
	count =1
	while count < len(states):
		parentNode = nodes[count-1]
		nodes.append(Node(str(states[count]),parent = parentNode))
		count+=1

	fileLoc = "E:/7th Sem/Artificial Intelligence/Assignments/Assignment 2/DFSTreeFinal.dot"
	DotExporter(nodes[0]).to_dotfile(fileLoc)
	render('dot','png',fileLoc)

######################################################################################
######################################################################################	
##########				Main funtion 										##########

if __name__ == '__main__':
	print("BFS METHOD")
	BFSMethod()

	#Gives some result I couldn't solve so not using
	# print("\n\nDFS METHOD")
	# DFSrecur([3,3,0],[])

	print("DFS MEthod")
	DFS()

######################################################################################
######################################################################################	
##########				   Main funtion Ends								##########

	
def DFSrecur(state,parentList):
	if(state == goal):
		parentList.append(state)
		PrintAllStates(parentList)
		print("-------------------\n")
		DFSComplete=True
		return 0
	else:
		men = state[0]
		cannibal = state[1]
		side = state[2]
		parent = state[3]

		if(men in checkRange and cannibal in checkRange and CheckPossible(men,cannibal)):
			if(state in parentList):
				return 0
				
			else:
				parentList.append(state)
				if(side==0):
					side = 1-side
					DFS([men-1,cannibal,side],parentList)
					DFS([men-2,cannibal,side],parentList)
					DFS([men-1,cannibal-1,side],parentList)
					DFS([men,cannibal-1,side],parentList)
					DFS([men,cannibal-2,side],parentList)

				elif(side ==1):
					side = 1-side
					DFS([men+1,cannibal,side],parentList)
					DFS([men+2,cannibal,side],parentList)
					DFS([men+1,cannibal+1,side],parentList)
					DFS([men,cannibal+1,side],parentList)
					DFS([men,cannibal+2,side],parentList)
		else:
			return 0

def PrintAllStates(parentList):
	for i in parentList:
		print(i)

def CheckPossible(men,cannibal):
	if(men==0 or men == 3 or men == cannibal):
		return True
	return False


