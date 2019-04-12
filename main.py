import database_util
import mailling_util

import cv2
import DetectChars
import CheckPlates

showSteps = False

SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

def main():
    DetectChars.loadKNNDataAndTrainKNN()
    path=input()

    imgOriginalScene  = cv2.imread("Images/"+path)

    listOfPossiblePlates = CheckPlates.detectPlatesInScene(imgOriginalScene)
    listOfPossiblePlates = DetectChars.detectCharsInPlates(listOfPossiblePlates)  

    #cv2.imshow("imgOriginalScene", imgOriginalScene)

    if len(listOfPossiblePlates) == 0:                   
        print("\nno license plates were detected\n") 
    else:

        listOfPossiblePlates.sort(key = lambda possiblePlate: len(possiblePlate.strChars), reverse = True)

        licPlate = listOfPossiblePlates[0]

       # cv2.imshow("imgPlate", licPlate.imgPlate)
       # cv2.imshow("imgThresh", licPlate.imgThresh)

        if len(licPlate.strChars) == 0:                   
            print("\nno characters were detected\n\n")  
            return

        print("\nlicense plate read from image = " + licPlate.strChars + "\n")
        if database_util.query(licPlate.strChars)==0:
            print("intrusion is detected alerting the security system through email!!!")
            mailling_util.email(licPlate.strChars)
        else:
            print("safe to move!!!")
    cv2.waitKey(0)

    return
if __name__ == "__main__":
    main()