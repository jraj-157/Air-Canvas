# Air-Canvas

## PROBLEM STATEMENT

The existing system only works with your fingers and has no highlighters, paints, or relatives. Another problem is the lack of top and down movement under the pen.The system uses one RGB camera that you can overwrite. So, every finger path is drawn, and the image will be abstract and unseen by the model. In addition, the user should know many movements to control his plan adequately.

## APPROACH

1. Read the frames and convert the captured frames to HSV color space.
2. Prepare the canvas frame and put the respective ink buttons on it.
3. Adjust the trackbar values for finding the mask of the colored marker.
4. Preprocess the mask with morphological operations. (erotion and dilation)
5. Detect the contours, find the center coordinates of the most prominent contour and keep storing them in the
array for successive frames. (arrays for drawing points on canvas)
6. Finally, draw the points stored in an array on the frames and canvas.

## Uniqueness

Our program will have more efficiency better finger readings and tracking and easily operable.

## APPLICATION

This program has the potential to challenge traditional writing methods Even adults who find it difficult to use the keyboard can easily use the program. Expanding functionality, this program can also be used to control IoT devices soon.
Wind-writing programs should listen only to their master's control touch and should not be misled by people all around. In the future, progress on Artificial Intelligence will improve the efficiency of writing in the air.

![](Screenshot%202022-07-11%20at%209.25.23%20AM.png)


## TECHSTACKS

We will be using the google collab and the code we will write that will be python we will 
use opencv ,Numpy ,Deque libraries.

