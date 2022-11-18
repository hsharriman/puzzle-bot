import cv2
import numpy as np
import pprint
from os import listdir
from os.path import isfile, join

threshold = 250

def edge_detection(imgPath):
    # Read the original image
    img = cv2.imread(imgPath)
    
    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #invert image
    img_gray = cv2.bitwise_not(img_gray)
    
    #perform edge detection
    thresh = cv2.Canny(img_gray, threshold, threshold * 2)
    pprint.pprint(thresh)
    show_piece(thresh, 'Binary image')
    cv2.imwrite('image_thres1.jpg', thresh)

    contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    print(contours)
                                      
    # draw contours on the original image
    image_copy = img.copy()
    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(255, 0, 0), thickness=1, lineType=cv2.LINE_8)
                    
    # see the results
    show_piece(image_copy, 'None approximation')
    cv2.imwrite('contours_none_image1.jpg', image_copy)

def load_puzzle_images():
    path = "../assets/4pc"
    onlyfiles = [join(path, f) for f in listdir(path) if isfile(join(path, f))]
    return onlyfiles 
    
def show_piece(piece, title="", waitKey=0):
    cv2.imshow(title, piece)
    cv2.waitKey(waitKey)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    for f in load_puzzle_images():
        print(f)
        edge_detection(f)
    #start with solving a 2x2, then a 3x3, then a 4x4, then we can try moving on to bigger puzzles with some weirder pieces
    #read in the puzzle pieces
        #perform edge detection on each piece, correct distortion etc.
        #convert puzzle piece data to point cloud and split into sides
        #create data structure to represent a puzzle piece
        #note whether an edge is concave/convex if applicable
        #not whether piece is an edge 