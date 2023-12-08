# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:28:18 2023

@author: xack0
"""

import csv
import random
import os



if os.path.exists("TestData.csv"):
  os.remove("TestData.csv")
  



import csv
import time
import math

# Specify the file path for the CSV
csv_file_path = "TestData.csv"

# Open the CSV file for writing
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["Time", "Position", "Angle"])


def write_to_csv(Data):
    
    
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write the header row      
        writer.writerow(Data)
    
    


Data = [23,33,44]


write_to_csv(Data)
    
        
     