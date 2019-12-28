##########################################################################
##########################################################################

---------------------RUN THE AAlgo.exe file to run the file--------------

############################################################################
############################################################################
Using manhattan distance and using the sequence of operation of LRUD, each step 
from curernt state to goal state has been shown.

I have used 2D array to check the manhattan distance. For instance,
In current state,
2	8	3
1	6	4
7	 	3

Goal state being, 
1	2	3
8	 	4
7	6	5

the manhataan distance of 1 can be calculated in goal state position is in
[0][0] = x1,y1
and in goal state position is in
[1][0] = x2,y2

manhattan distance is thus mod(x1-x2) + mod(y1-y2).
All manhattan distance is calculated as such.

Using the A* algo Left, Right, Up, Down movement of the hole is done and overall 
manhattan distance is calculated and the step with least manhattan distance is 
taken as the next stage until the goal state is reached.