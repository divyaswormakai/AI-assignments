using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AstarAlgo : MonoBehaviour
{
    int[,] currState;
    int[,] goalState;
    void Start()
    {
        SetStartState();
        SetGoalState();
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            CreateNextBranch();
        }
    }

    void CreateNextBranch()
    {
        int[,] tempMatrix = new int[3, 3];
        
        //LRUD operation as 0123
        for(int i = 0; i < 4; i++)
        {
            for (int ii = 0; ii < 3; ii++)
            {
                for (int j = 0; j < 3; j++)
                {
                    tempMatrix[ii, j] = currState[ii, j];
                }
            }

            if (i == 0)             //Left
            {

            }
            else if (i == 1)        //Right
            {

            }
            else if (i == 2)        //Up
            {

            }
            else                    //Down
            {

            }
        }
    }
    void SetStartState()
    {
        currState = new int[3,3];
        currState[0, 0] = 2;
        currState[0, 1] = 8;
        currState[0, 2] = 3;
        currState[1, 0] = 1;
        currState[1, 1] = 6;
        currState[1, 2] = 4;
        currState[2, 0] = 7;
        currState[2, 1] = 0;
        currState[2, 2] = 5;
    }

    void SetGoalState()
    {
        goalState = new int[3, 3];
        goalState[0, 0] = 1;
        goalState[0, 1] = 2;
        goalState[0, 2] = 3;
        goalState[1, 0] = 8;
        goalState[1, 1] = 0;
        goalState[1, 2] = 4;
        goalState[2, 0] = 7;
        goalState[2, 1] = 6;
        goalState[2, 2] = 5;
    }
}
