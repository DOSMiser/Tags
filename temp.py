# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:29:04 2023

@author: xack0
"""

import numpy as np
import time
import csv
import os
import math
import cv2
import datetime
from pupil_apriltags import Detector



if os.path.exists("TestData.csv"):
  os.remove("TestData.csv")

cap = cv2.VideoCapture(0)
 
start = time.time()



# Specify the file path for the CSV
csv_file_path = "TestData.csv"

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["Time", "Position", "Angle"])


def write_to_csv(X):
    
    
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write the header row      
        writer.writerow(X)

 

def TagRead():
    
  

    ret, frame = cap.read()
    
    
    # You can now use the 'frame' variable for further processing, saving, or displaying
    # For example, you can save it to a file using cv2.imwrite()
    cv2.imwrite('captured_image.jpg', frame)
    
    # You can also display the image if needed
    
    ############################################################
    # Path to the input image
    image_path = 'captured_image.jpg'
    
    # Load the image using OpenCV
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize the image for better visualization (optional)
    scale_factor = 1  # Adjust the scale factor as needed
    image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)
    
    
    detector = Detector(families='tag36h11', nthreads=1, quad_decimate=1.0, quad_sigma=0.0)
     
     # Detect AprilTags in the image
    tags = detector.detect(image)
     # Loop through detected tags and print their information
    for tag in tags:
     (f"Tag ID: {tag.tag_id}")
     (f"Tag Center: ({tag.center[0]}, {tag.center[1]})")
     (f"Tag Corners: {tag.corners}")
     (f"Tag Homography: {tag.homography}")
     (f"Tag Decision Margin: {tag.decision_margin}\n")
     
     
     center = tag.center
     
     Corners = tag.corners ;
     
     
     
     x = ((Corners[0,0] - Corners[0,1])**2)
     y = ((Corners[1,0] - Corners[1,1])**2)
     
     S = math.sqrt(x+y)
     
     direction = (math.tan((Corners[1,0] - Corners[1,1])/(Corners[0,0] - Corners[0,1])))*180/(math.pi*2)
    
     
     t = time.time() - start
     
     return [t,S,direction]

while True:

    Data = TagRead()
    
    
    
    if Data is not None:
        
        print("recorded")
        write_to_csv(Data)



 ############################## Calibration #########################
 

    
 

cv2.destroyAllWindows()
cap.release()