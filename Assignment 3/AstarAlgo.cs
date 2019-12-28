using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
using UnityEngine.SceneManagement;

public class AstarAlgo : MonoBehaviour
{
    public TextMeshProUGUI txt,completeTxt;
    public Image green, red;

    public GameObject prevLeft, prevRight, prevUp, prevDown,Lpos,Upos,Rpos,Dpos;

    int[,] currState;
    int[,] goalState;
    int activeX, activeY;                           //For the active position of 0 i.e Gap, which will be moved
    
    //Anything related to the TextMeshPro and Image are for UI purposes only.
    void Start()
    {
        SetStartState();
        SetGoalState();
    }

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (CheckComplete())
            {
                completeTxt.SetText("The Goal State has been reached.\n Press 'Esc' to start again.");
            }
            else
            {
                CreateNextLevel();
            }
        }

        if (Input.GetKeyDown(KeyCode.Escape))
        {
            SceneManager.LoadScene("SampleScene");
        }
    }

    bool CheckComplete()        //Checks if the goal State has been reached or not
    {
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 3; j++)
            {
                if(currState[i,j] != goalState[i, j])
                {
                    return false;
                }
            }
        }
        return true;
    }

    void CreateNextLevel()      
    {
        int[,] tempMatrix = new int[3, 3];          //A temporary matrix that will be operated by each side to check validity
        int[,] toReplaceState = new int[3,3];       //A temporary matrix that will be used to replace the currMatrix values
        int minVal = 50;                            //Variable to store the minimum manhattan value
        int opertionVal = 5;                        //Variable to store the best operation side
        //LRUD operation as 0123
        for(int i = 0; i < 4; i++)
        {
            //Since array as passed as reference and used as such replace the matrix of tempMatrix by currState for each side operation
            for (int ii = 0; ii < 3; ii++)
            {
                for (int j = 0; j < 3; j++)
                {
                    tempMatrix[ii, j] = currState[ii, j];               
                }
            }

            int val = tempMatrix[activeX, activeY];

            if (i == 0)            //Left
            {
                if (activeY - 1 >= 0)
                {
                    TextMeshProUGUI leftMat = Instantiate(txt, Lpos.transform.position, Quaternion.identity) as TextMeshProUGUI;
                    leftMat.transform.parent = prevLeft.transform;
                    tempMatrix[activeX, activeY] = tempMatrix[activeX, activeY - 1];
                    tempMatrix[activeX, activeY - 1] = val;
                    SetString(tempMatrix, leftMat,0);
                }
                Image img = Instantiate(red, Lpos.transform.position, Quaternion.identity) as Image;
                img.transform.parent = prevLeft.transform;
            }

            if (i == 1)        //Right
            {
                if (activeY + 1 < 3)
                {
                    TextMeshProUGUI rightMat = Instantiate(txt, Rpos.transform.position, Quaternion.identity) as TextMeshProUGUI;
                    rightMat.transform.parent = prevRight.transform;
                    tempMatrix[activeX, activeY] = tempMatrix[activeX, activeY + 1];
                    tempMatrix[activeX, activeY + 1] = val;
                    SetString(tempMatrix, rightMat,1);
                }
                Image img = Instantiate(red, Rpos.transform.position, Quaternion.identity) as Image;
                img.transform.parent = prevRight.transform;
            }

            if (i == 2)        //Up
            {
                if (activeX - 1 >= 0)
                {
                    TextMeshProUGUI upMat = Instantiate(txt, Upos.transform.position, Quaternion.identity) as TextMeshProUGUI;
                    upMat.transform.parent = prevUp.transform;
                    tempMatrix[activeX, activeY] = tempMatrix[activeX - 1, activeY];
                    tempMatrix[activeX - 1, activeY] = val;
                    SetString(tempMatrix, upMat,2);
                }
                Image img = Instantiate(red, Upos.transform.position, Quaternion.identity) as Image;
                img.transform.parent = prevUp.transform;
            }

            if(i == 3  )         //Down
            {
                if (activeX + 1 < 3)
                {
                    TextMeshProUGUI downMat = Instantiate(txt, Dpos.transform.position, Quaternion.identity) as TextMeshProUGUI;
                    downMat.transform.parent = prevDown.transform;
                    tempMatrix[activeX, activeY] = tempMatrix[activeX + 1, activeY];
                    tempMatrix[activeX + 1, activeY] = val;
                    SetString(tempMatrix, downMat,3);
                }
                Image img = Instantiate(red, Dpos.transform.position, Quaternion.identity) as Image;
                img.transform.parent = prevDown.transform;

            }

            //Calculate Manhataan distance
            int manhattan = CalculateManhattan(tempMatrix);

            if (manhattan <= minVal)                //If the current minimum manhattan value is greater than the instance of manhattan value
            {
                minVal = manhattan;                 //Change the manhattan value
                opertionVal = i;                    //Change the side of operation
                for (int ii = 0; ii < 3; ii++)      //Replace the toReplace state matrix by the tempMatrix of the current instance
                {
                    for (int j = 0; j < 3; j++)
                    {
                        toReplaceState[ii, j] = tempMatrix[ii, j];
                    }
                }
            }
        }

        //Place the green image to move selected which is stored in operationVal and increase or decrease the activeX or activeY accordingly
        switch (opertionVal)
        {
            case 0:             //Left is best option
                {
                    Image img = Instantiate(green, Lpos.transform.position, Quaternion.identity) as Image;
                    img.transform.parent = prevLeft.transform;
                    activeY -= 1;               //Decrease the activeY by 1 to match the position of 1
                    break;
                }
            case 1:             //Right is best option
                {
                    Image img = Instantiate(green, Rpos.transform.position, Quaternion.identity) as Image;
                    img.transform.parent = prevRight.transform;
                    activeY += 1;               //Increase the activeY by 1 to match the position of 1
                    break;
                }
            case 2:             //Up is best option
                {
                    Image img = Instantiate(green, Upos.transform.position, Quaternion.identity) as Image;
                    img.transform.parent = prevUp.transform;
                    activeX -= 1;                //Decrease the activeX by 1 to match the position of 1
                    break;
                }
            case 3:             //Down is best option
                {
                    Image img = Instantiate(green, Dpos.transform.position, Quaternion.identity) as Image;
                    img.transform.parent = prevDown.transform;
                    activeX += 1;                //Increase the activeX by 1 to match the position of 1
                    break;
                }
            default:
                {
                    break;
                }
        }

        //Reposition the location to generate new branch
        Vector2 dec = Upos.transform.position;
        dec.y -= 300f;
        Upos.transform.position = dec;

        dec.x = Dpos.transform.position.x;
        Dpos.transform.position = dec;

        dec.x = Lpos.transform.position.x;
        Lpos.transform.position = dec;

        dec.x = Rpos.transform.position.x;
        Rpos.transform.position = dec;
       
        
        
        string temp = "Curr State \n";          //printing in console purposes only

        for (int ii = 0; ii < 3; ii++)
        {
            for (int j = 0; j < 3; j++)
            {
                temp+= toReplaceState[ii, j] + "\t";            //printing in console only
                currState[ii,j] = toReplaceState[ii, j];        //Update the current State of the matrix by the best matrix(toReplace Matrix selected by the min manhattan distance)
            }
            temp += "\n";
        }
      //  print(temp);
    }


    //Calculating the manhattan distance
    //Since we use 2D matrix it is simple to claculate the manhattan distance
    //Adding goalState.x - currState.x and  goalState.y - currState.y will give the manhattan distance of each value
    //We add all the manhattan distance and thus the total manhattan distance is calculated
    int CalculateManhattan(int[,] mat)
    {
        int currVal;
        int totalManhattan = 0;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                currVal = mat[i, j];
                if (currVal != 0)
                {
                    int[] goalValues = FindGoalPosition(currVal);           //Find goal position of current status
                    int tempManhattan = System.Math.Abs(goalValues[0] - i) + System.Math.Abs(goalValues[1] - j);    //Calculate manthtaanfor a certain value
                    totalManhattan += tempManhattan;            //Adding the mahattan distance to the total manhattan
                }
            }
        }
        return totalManhattan;      //Total manhattan distance returned
    }


     //Take the value and give the result of the current position of the value in the goalState to calculate mahattan distance
    int[] FindGoalPosition(int val) {        
        int[] pos = new int[2];
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (goalState[i, j] == val)
                {
                    pos[0] = i;
                    pos[1] = j;
                }
            }
        }
        return pos;
    }

    //Set string of the generated branch for UI reasons only
    void SetString(int[,] mat, TextMeshProUGUI text,int side)
    {
        string temp = "";
        switch (side)
        {
            case 0: temp += "Left\n\n"; break;
            case 1: temp += "Right\n\n"; break;
            case 2: temp += "Up\n\n"; break;
            case 3: temp += "Down\n\n"; break;
        }
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (mat[i, j] == 0)
                {
                    temp += " \t";
                }
                else
                {
                    temp += mat[i, j] + "\t";
                }
            }
            temp += "\n";
        }
        text.SetText(temp);
    }

    //Set Start State
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
        activeX = 2;
        activeY = 1;
    }

    //Set End State
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
