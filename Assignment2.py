start = [3,3,0]
goal = [0,0,1]
checkRange = range(0,4)

def DFS(state,parentList):
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

if __name__ == "__main__":
	parentList = []
	DFS(start,parentList)




			



