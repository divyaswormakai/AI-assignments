import queue

start = [3,3,0,[]]
final = [0,0,1,[]]
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
			print("DONE")

	if(men>=0 and cannibal>=0 and men<=3 and cannibal<=3):
		if(men == 0 or men ==3 or men == cannibal):
			if(currState not in tempParents):
				tempParents.append(currState)
				if(side==0):
					side =toggleSide(side)
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

	while not complete:
		currState = stateSet[counter]

		currMen = currState[0]
		currCannibal = currState[1]
		currSide = currState[2]
		parentState =currState[3]

		if(currMen == 0 and currCannibal ==0 and currSide==1):	#Condition Complete
			complete = True
		elif currSide==2:  	 #for error
			counter+=1
			continue
		else:
			if(currMen>=0 and currMen<=3 and currCannibal>=0 and currCannibal<=3):		#To check if within bounds
				if(currMen==0 or currMen==3 or currMen==currCannibal):		#For conditions where cannibal outnumber men
					side = toggleSide(currSide)
					temp =[]				#TempSet variable

					compareSet =[]			#Set without the parent index
					for val in stateSet:
						compareSet.append([val[0],val[1],val[2]])

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

	total = len(stateSet)
	# print(stateSet )
	tempSet =[]
	print("---------------------")
	counter = total-1
	while(counter>=0):
		curr = stateSet[counter]
		if(curr[0]==0 and curr[1]==0 and curr[2]==1):		#get final state
			print(curr)
			counter = curr[3]
			break
		else:
			counter-=1
	while(counter>=0):
		curr = stateSet[counter]
		if(curr[0]==3 and curr[1]==3 and curr[2]==0):		#get intital state
			print(curr)
			counter =-1
		else:												#get every possible statein between
			print(curr)
			counter = curr[3]
	

def toggleSide(side):
	if(side == 1):
		side =0
	else:
		side =1			
	return side

if __name__ == '__main__':
	# MyMethod(start)
	BFSMethod()


