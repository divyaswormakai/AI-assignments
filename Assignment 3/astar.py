import copy
import pydot

start = [[2,8,3],[1,6,4],[7,0,5]]
goal = [[1,2,3],[8,0,4],[7,6,5]]
totalStates = []
parentList= []
depthList = []
manhattan = []
visited =[]
prevAction =[]						#1 for left, 2 for right, 3 for up, 4 for down
checkRange = [0,1,2]
action = ['Left','Right','Up','Down']

def AstarAlgorithm():
	depth = 0
	totalStates.append(start)
	parentList.append(-1)
	depthList.append(depth)
	manhattan.append(CalcManhattan(start))
	visited.append(False)
	prevAction.append(-1)

	complete = False
	while not complete:
		cost =[]
		for i in range(len(totalStates)):
			cost.append(depthList[i] + manhattan[i])
		StateIndex = GetNextValue()
		visited[StateIndex] = True
		currState = copy.deepcopy(totalStates[StateIndex])
		prevStep = prevAction[StateIndex]
		depth+=1
		if currState == goal:
			complete = True
			print("Completed")
		 	# Print the tree
			break
		else:
			tempState = copy.deepcopy(currState)

			X0,Y0 = GetZeroPosition(tempState)	#x,y position of zero in current matrix
			for i in range(1,5):
				valChange = False
				if i==1 and prevStep!=2:	#For left(1) action if previous action was not right(2)
					if(Y0 - 1 in checkRange):
						tempState[X0][Y0-1], tempState[X0][Y0] = tempState[X0][Y0],tempState[X0][Y0-1]
						valChange = True
				if i==2 and prevStep!=1:	#For right(2) action if previous action was not left(1)
					if(Y0 + 1 in checkRange):
						tempState[X0][Y0+1], tempState[X0][Y0] = tempState[X0][Y0],tempState[X0][Y0+1]
						valChange = True
				if i==3 and prevStep!=4:	#For Up(3) action if previous action was not Down(4)
					if (X0-1 in checkRange):
						tempState[X0-1][Y0], tempState[X0][Y0] = tempState[X0][Y0],tempState[X0-1][Y0]
						valChange = True
				if i==4 and prevStep!=3:	#For down(4) action if previous action was not up(3)
					if(X0+1 in checkRange):
						tempState[X0+1][Y0], tempState[X0][Y0] = tempState[X0][Y0],tempState[X0+1][Y0]
						valChange = True

				if valChange:
					totalStates.append(tempState)
					parentList.append(StateIndex)
					depthList.append(depth)
					manhattan.append(CalcManhattan(tempState))
					visited.append(False)
					prevAction.append(i)
					if(tempState==goal):
						break
					tempState = copy.deepcopy(currState)


			

	currD =0
	for i in range(len(totalStates)):
		if(currD == depthList[i]):
			print(i,parentList[i])
		else:
			print("-----------")
			currD+=1
			print(i,parentList[i])
	
def CalcManhattan(state):
	totalManHattan = 0
	for i in range(3):
		for j in range(3):
			currVal = state[i][j]
			if(currVal != 0):
				goalPos = FindInGoalPosition(currVal)
				totalManHattan += (abs(goalPos[0]-i) + abs(goalPos[1]-j))
	return totalManHattan

def FindInGoalPosition(val):
	for i in range(3):
		for j in range(3):
			if goal[i][j] == val:
				return [i,j]	
	

def GetZeroPosition(state):
	for i in range(3):
		for j in range(3):
			if(state[i][j] == 0):
				return i,j

def GetNextValue():
	minIndex =0
	minVal = 10000

	for i in range(len(totalStates)):
		if visited[i] == False:
			if (manhattan[i]+depthList[i])<minVal:
				minIndex=i
				minVal = manhattan[i]+depthList[i]
	return minIndex

if __name__ == '__main__':
	AstarAlgorithm()

	G = pydot.Dot(graph_type = 'digraph', label = "8 puzzle state-space tree using A* algorithm\n with Manhattan distance as heuristic function", fontsize = "20", fontcolor = "black")
	nodes =[]
	for i in range(len(totalStates)):
		if visited[i]:
			color = "orange"
		else:
			color="gray"
		if(i==0):
			color="yellow"
		if(i == len(totalStates)-1):
			color = "green"
		currState = totalStates[i]
		labelstr = ""
		for j in range(3):
			for k in range(3):
				labelstr+=str(currState[j][k])+"\t"
			labelstr+="\n"
		labelstr+="Manhattan: "+str(manhattan[i])+"\n"+"Depth: "+str(depthList[i])
		nodes.append(pydot.Node(str(i),shape = "box", style = "filled", fillcolor = color,label = labelstr))
		G.add_node(nodes[i])

		if i!=0:
			if(visited[i]):
				e = pydot.Edge(nodes[parentList[i]],nodes[i],label = action[prevAction[i]-1],color="red",penwidth =4)
			else:
				e = pydot.Edge(nodes[parentList[i]],nodes[i],label = action[prevAction[i]-1])
			G.add_edge(e)
		G.write_png("E:\\7th Sem\\Artificial Intelligence\\Assignments\\Assignment 3\\solution.png")



