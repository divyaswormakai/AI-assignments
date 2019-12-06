from anytree import Node,RenderTree
from anytree.exporter import DotExporter
from graphviz import render

start = [3,3,0,[]]
final = [0,0,1,[]]
goal = [0,0,1]
checkRange = range(0,4)
depthCounter =0

def MyMethod(currState):
	men =currState[0]
	cannibal = currState[1]
	side = currState[2]
	tempParents = currState[3]

	if(men ==0 and cannibal==0 and side == 1):
			tempParents.append(currState)
			for state in tempParents:
				print(str(state[0])+str(state[1])+str(state[2]))
			print("-----------")

	if(men>=0 and cannibal>=0 and men<=3 and cannibal<=3):
		if(men == 0 or men ==3 or men == cannibal):
			if(currState not in tempParents):
				tempParents.append(currState)
				if(side==0):
					side = 1-side
					MyMethod([men-1,cannibal,side,tempParents])
					MyMethod([men,cannibal-1,side,tempParents])
					MyMethod([men-1,cannibal-1,side,tempParents])
					MyMethod([men-2,cannibal,side,tempParents])
					MyMethod([men,cannibal-2,side,tempParents])
				else:
					side =toggleSide(side)
					MyMethod([men+1,cannibal,side,tempParents])
					MyMethod([men,cannibal+1,side,tempParents])
					MyMethod([men+1,cannibal+1,side,tempParents])
					MyMethod([men+2,cannibal,side,tempParents])	
					MyMethod([men,cannibal+2,side,tempParents])
	

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
		print(currState)
		if(currMen == 0 and currCannibal ==0 and currSide==1):	#Condition Complete
			completeLength = counter
			complete = True
			continue
		elif currSide==2:  	 #for error
			counter+=1
			continue
		else:
			if(currMen>=0 and currMen<=3 and currCannibal>=0 and currCannibal<=3):		#To check if within bounds
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
						if(val[0]>=0 and val[0]<=3 and val[1]>=0 and val[1]<=3):		#if the added value is within range
							valSet=[val[0],val[1],val[2]]
							if(valSet not in compareSet):				#if the state already exists in the tree
								stateSet.append(val)


		counter+=1

	print("---------------------")
	counter = 1
	nodes =[]
	nodes.append(Node(str([3,3,0,0])))
	while counter<completeLength+1:
		parentNode = nodes[(stateSet[counter][3])]
		nodes.append(Node(str(stateSet[counter]),parent = parentNode))
		counter+=1
	# for pre, fill, node in RenderTree(nodes[0]):
	# 	print("%s%s" %(pre,node.name))

	fileLoc = "E:/7th Sem/Artificial Intelligence/Assignments/BFSTree.dot"
	DotExporter(nodes[0]).to_dotfile(fileLoc)
	render('dot','png',fileLoc)

# Building the tree

	# while(counter>=0):
	# 	curr = stateSet[counter]
	# 	if(curr[0]==0 and curr[1]==0 and curr[2]==1):		#get final state
	# 		print(curr)
	# 		counter = curr[3]
	# 		break
	# 	else:
	# 		counter-=1
	# while(counter>=0):
	# 	curr = stateSet[counter]
	# 	if(curr[0]==3 and curr[1]==3 and curr[2]==0):		#get intital state
	# 		print(curr)
	# 		counter =-1
	# 	else:												#get every possible statein between
	# 		print(curr)
	# 		counter = curr[3]


def DFS(state,parentList,treeNodes,parentNode):
	if(state == goal):
		parentList.append(state)
		PrintAllStates(parentList)
		print("-------------------\n")
		return 0
	else:
		men = state[0]
		cannibal = state[1]
		side = state[2]
		if(men in checkRange and cannibal in checkRange and CheckPossible(men,cannibal)):
			if(state in parentList):
				return 0
				
			else:
				parentList.append(state)
				treeNodes.append(Node(str(state),parent = parentNode))
				if(side==0):
					side = 1-side
					DFS([men-1,cannibal,side],parentList,treeNodes,str(state))
					DFS([men-2,cannibal,side],parentList,treeNodes,str(state))
					DFS([men-1,cannibal-1,side],parentList,treeNodes,str(state))
					DFS([men,cannibal-1,side],parentList,treeNodes,str(state))
					DFS([men,cannibal-2,side],parentList,treeNodes,str(state))

				elif(side ==1):
					side = 1-side
					DFS([men+1,cannibal,side],parentList,treeNodes,str(state))
					DFS([men+2,cannibal,side],parentList,treeNodes,str(state))
					DFS([men+1,cannibal+1,side],parentList,treeNodes,str(state))
					DFS([men,cannibal+1,side],parentList,treeNodes,str(state))
					DFS([men,cannibal+2,side],parentList,treeNodes,str(state))
		else:
			return 0

def PrintAllStates(parentList):
	for i in parentList:
		print(i)

def CheckPossible(men,cannibal):
	if(men==0 or men == 3 or men == cannibal):
		return True
	return False

if __name__ == '__main__':
	# MyMethod(start)
	print("BFS METHOD")
	BFSMethod()

	# treeNodes= []
	# treeNodes.append(Node(str([3,3,0])))
	# print("\n\nDFS METHOD")
	# DFS([3,3,0],[],treeNodes,treeNodes[0])
	# fileLoc = "E:/7th Sem/Artificial Intelligence/Assignments/DFSTree.dot"
	# DotExporter(treeNodes[0]).to_dotfile(fileLoc)
	# render('dot','png',fileLoc)
	


