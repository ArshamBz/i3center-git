#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:12:09 2021

@author: arshambz
"""

'''
Assume that you are going to track a coloured object from a live video
Define command-line arguments
The “circle.jpg” path +
Hue Low Range [0, 180] +
Saturation Low Range [0, 255] +
Value Low Range [0, 255] +
Hue Up Range [0, 180] +
Saturation Up Range [0, 255] +
Value Up Range [0, 255] +
Import your PC's Camera
Create a track bar
Detect the object you desire based on its colour
'''


'''
HLR = Hue Low Range
HUR = Hue Up Range
SUR = Saturation Up Range
SLR = Saturation Low Range
VUR = Value Up Range
VLR = Value Low Range

'''



# Import Required Modules
import cv2
import sys
import argparse
import numpy as np


# Use CLA to define the variables

def parse_args(arguments):
    Parser = argparse.ArgumentParser(description="The variables are defined here")

    Parser.add_argument("--Circle_Image_Path",
                        help="Raw_Image Path",
                        default=r"/Users/arshambz/Desktop/i3center/tamrin/6/circles.jpg")

    Parser.add_argument("--Hue_Low_Range",
                        help="Hue_Low_Range",
                        default=[0, 180])

    Parser.add_argument("--Saturation_Low_Range",
                        help="Saturation_Low_Range",
                        default=[0, 255])

    Parser.add_argument("--Value_Low_Range",
                        help="Value_Low_Range",
                        default=[0, 255])

    Parser.add_argument("--Hue_Up_Range",
                        help="Hue_Up_Range",
                        default=[0, 180])

    Parser.add_argument("--Saturation_Up_Range",
                        help="Saturation_Up_Range",
                        default=[0, 255])

    Parser.add_argument("--Value_Up_Range",
                        help="Value_Up_Range",
                        default=[0, 255])

    return Parser.parse_args(arguments)


# =============================================================================
# Call the variables
All_arguments = sys.argv[1:]
All_arguments = parse_args(All_arguments)
Circle_Image_Path = All_arguments.Circle_Image_Path
Hue_Low_Range = All_arguments.Hue_Low_Range
Saturation_Low_Range = All_arguments.Saturation_Low_Range
Value_Low_Range = All_arguments.Value_Low_Range
Hue_Up_Range = All_arguments.Hue_Up_Range
Saturation_Up_Range = All_arguments.Saturation_Up_Range
Value_Up_Range = All_arguments.Value_Up_Range

Raw_Image = cv2.resize(cv2.imread(Circle_Image_Path, 1), (512, 512))

my_camera = cv2.VideoCapture(0)

# Find HSV corresponding to RGB values for Blue, Green, and Red to track

Blue_HSV = cv2.cvtColor(np.uint8([[[255, 0, 0]]]), cv2.COLOR_BGR2HSV)
Green_HSV = cv2.cvtColor(np.uint8([[[0, 255, 0]]]), cv2.COLOR_BGR2HSV)
Red_HSV = cv2.cvtColor(np.uint8([[[0, 0, 255]]]), cv2.COLOR_BGR2HSV)

HSV_Image = cv2.cvtColor(Raw_Image, cv2.COLOR_BGR2HSV)

# Create an empty track bar namely “Tracking Platform”
cv2.namedWindow("Tracking_Platform")


def On_Change_Nothing(Input):
    pass


Hue_Low_Range = cv2.createTrackbar("HLR",
                                   "Tracking_Platform",
                                   0,
                                   180,
                                   On_Change_Nothing)

Saturation_Low_Range = cv2.createTrackbar("SLR",
                                          "Tracking_Platform",
                                          0,
                                          255,
                                          On_Change_Nothing)

Value_Low_Range = cv2.createTrackbar("VLR",
                                     "Tracking_Platform",
                                     0,
                                     255,
                                     On_Change_Nothing)

Hue_Up_Range = cv2.createTrackbar("HUR",
                                  "Tracking_Platform",
                                  0,
                                  180,
                                  On_Change_Nothing)

Saturation_Up_Range = cv2.createTrackbar("SUR",
                                         "Tracking_Platform",
                                         0,
                                         255,
                                         On_Change_Nothing)

Value_Up_Range = cv2.createTrackbar("VUR",
                                    "Tracking_Platform",
                                    0,
                                    255,
                                    On_Change_Nothing)

# Show both of the imported circle image and tracking platform together

while (True):

    Hue_Low_Range_ = cv2.getTrackbarPos("Hue_Low_Range",
                                        "Tracking_Platform")
    Saturation_Low_Range = cv2.getTrackbarPos("Saturation_Low_Range",
                                              "Tracking_Platform")
    Value_Low_Range = cv2.getTrackbarPos("Value_Low_Range",
                                         "Tracking_Platform")
    Hue_Up_Range = cv2.getTrackbarPos("Hue_Up_Range",
                                      "Tracking_Platform")
    Saturation_Up_Range = cv2.getTrackbarPos("Saturation_Up_Range",
                                             "Tracking_Platform")
    Value_Up_Range = cv2.getTrackbarPos("Value_Up_Range",
                                        "Tracking_Platform")
    ret, frame = my_camera.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    HSV_Image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask from HSV image made in range a blue HSV colour space
    # take [H-10, 50, 50] and [H+10, 255, 255]

    lowerb = np.array([Hue_Low_Range_, Saturation_Low_Range, Value_Low_Range])
    upperb = np.array([Hue_Up_Range, Saturation_Up_Range, Value_Up_Range])
    Mask = cv2.inRange(HSV_Image, lowerb, upperb)

    # Detect your desired object by using a bit-wise “AND”
    Detected_Object = cv2.bitwise_and(frame, frame, mask=Mask)

    # Show the outputs

    cv2.imshow("Tracking_Platform", frame)
    cv2.imshow("Mask", Mask)
    cv2.imshow("Detected_Object", Detected_Object)
    # cv2.imshow('my camera', frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

my_camera.release()
cv2.destroyAllWindows()