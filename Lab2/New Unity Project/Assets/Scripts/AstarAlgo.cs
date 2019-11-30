using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class AstarAlgo : MonoBehaviour
{
    public TextMeshProUGUI txt;
    public Image green, red;

    public GameObject prevLeft, prevRight, prevUp, prevDown,Lpos,Upos,Rpos,Dpos;

    int[,] currState;
    int[,] goalState;
    int activeX, activeY;                           //For the position of 0 which will be moved
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
                print("Already Complete");
            }
            else
            {
                CreateNextLevel();
            }
        }
    }

    bool CheckComplete()
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
        int[,] tempMatrix = new int[3, 3];
        int[,] toReplaceState = new int[3,3];
        int minVal = 50;
        int opertionVal = 5;
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

            int val = tempMatrix[activeX, activeY];

            if (i == 0)            //Left
            {
                if (activeY - 1 >= 0)
                {
                    TextMeshProUGUI leftMat = Instantiate(txt, Lpos.transform.position, Quaternion.identity) as TextMeshProUGUI;
                    leftMat.transform.parent = prevLeft.transform;
                    tempMatrix[activeX, activeY] = tempMatrix[activeX, activeY - 1];
                    tempMatrix[activeX, activeY - 1] = val;
                    SetString(tempMatrix, leftMat);
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
                    SetString(tempMatrix, rightMat);
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
                    SetString(tempMatrix, upMat);
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
                    SetString(tempMatrix, downMat);
                }
                Image img = Instantiate(red, Dpos.transform.position, Quaternion.identity) as Image;
                img.transform.parent = prevDown.transform;

            }

            //Calculate Manhataan distance
            int manhattan = CalculateManhattan(tempMatrix);
            print(manhattan);
            if (manhattan <= minVal)
            {
                minVal = manhattan;
                opertionVal = i;
                for (int ii = 0; ii < 3; ii++)
                {
                    for (int j = 0; j < 3; j++)
                    {
                        toReplaceState[ii, j] = tempMatrix[ii, j];
                    }
                }
            }
        }

        switch (opertionVal)
        {
            case 0:
                {
                    Image img = Instantiate(green, Lpos.transform.position, Quaternion.identity) as Image;
                    img.transform.parent = prevLeft.transform;
                    activeY -= 1;
                    print("LEFT");
                    break;
                }
            case 1:
                {
                    Image img = Instantiate(green, Rpos.transform.position, Quaternion.identity) as Image;
                    img.transform.parent = prevRight.transform;
                    activeY += 1;
                    print("RIGHT");
                    break;
                }
            case 2:
                {
                    Image img = Instantiate(green, Upos.transform.position, Quaternion.identity) as Image;
                    img.transform.parent = prevUp.transform;
                    activeX -= 1;
                    print("UP");
                    break;
                }
            case 3:
                {
                    Image img = Instantiate(green, Dpos.transform.position, Quaternion.identity) as Image;
                    img.transform.parent = prevDown.transform;
                    activeX += 1;
                    print("DOWN");
                    break;
                }
            default:
                {
                    break;
                }
        }

        Vector2 dec = Upos.transform.position;
        dec.y -= 300f;
        Upos.transform.position = dec;

        dec = Dpos.transform.position;
        dec.y -= 300f;
        Dpos.transform.position = dec;

        dec = Lpos.transform.position;
        dec.y -= 300f;
        Lpos.transform.position = dec;

        dec = Rpos.transform.position;
        dec.y -= 300f;
        Rpos.transform.position = dec;

        string temp = "Curr State \n";

        for (int ii = 0; ii < 3; ii++)
        {
            for (int j = 0; j < 3; j++)
            {
                temp+= toReplaceState[ii, j] + "\t";
                currState[ii,j] = toReplaceState[ii, j];
            }
            temp += "\n";
        }
        print(temp);
    }

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
                    int[] goalValues = FindGoalPosition(currVal);
                    int tempManhattan = System.Math.Abs(goalValues[0] - i) + System.Math.Abs(goalValues[1] - j);
                    totalManhattan += tempManhattan;
                }
            }
        }
        return totalManhattan;
    }

    int[] FindGoalPosition(int val)
    {
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

    void SetString(int[,] mat, TextMeshProUGUI text)
    {
        string temp = "";
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                temp += mat[i, j] + "\t";
            }
            temp += "\n";
        }
        text.SetText(temp);
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
        activeX = 2;
        activeY = 1;
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
