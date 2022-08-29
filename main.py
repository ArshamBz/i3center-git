import cv2
import numpy as np
import argparse
import sys

class Class_Final_Exam():
    def __init__(self,
                 name=None,
                 help=None,
                 default=None,
                 Video_Path = None,
                 text = None,
                 textfont = cv2.FONT_HERSHEY_SIMPLEX,
                 textColor = (255,0,0)):

       self.name = name
       self.help = help
       self.default = default
       self.Video_Path = Video_Path
       self.text = text
       self.textfont = textfont
       self.textColor = textColor

    def parse_args(self):
        Parser_HSV = argparse.ArgumentParser(description="Command Line Arguments")
        Parser_HSV.add_argument(name=self.name, help=self.help, default=self.default)
        return Parser_HSV.parse_args()
    def Video_Import(self):
        my_video = cv2.VideoCapture(self.Video_Path)
        return my_video
    def Insert_Text(self):
        Ptext=cv2.putText(self.textColor,self.textfont,self.text)
        return Ptext


HL = Class_Final_Exam("--HL","Hue Low Range",[0,180])
HL_ = Class_Final_Exam.parse_args(HL)
HU = Class_Final_Exam("--HU","Hue Up Range",[0,180])
HU_ = Class_Final_Exam.parse_args(HU)
SL = Class_Final_Exam("--SL","Saturation Low Range",[0,255])
SL_ = Class_Final_Exam.parse_args(SL)
SU = Class_Final_Exam("--SU","Saturation Up Range",[0,255])
SU_ = Class_Final_Exam.parse_args(SU)
VL = Class_Final_Exam("--VL","Value Low Range",[0,255])
VL_ = Class_Final_Exam.parse_args(SU)
VU = Class_Final_Exam("--VU","Value up Range",[0,255])
VU_ = Class_Final_Exam.parse_args(VU)
myvideo =Class_Final_Exam(Video_Path=(r'/Users/arshambz/Desktop/exaam/tree.avi'))
myvideo_ = Class_Final_Exam.Video_Import(myvideo)

cv2.namedWindow("Tracking_Platform")


def onChange(X):
    pass


cv2.createTrackbar("HL", "Tracking_Platform", HL_[0], HL_[1], onChange)
cv2.createTrackbar("SL", "Tracking_Platform", SL_[0], SL_[1], onChange)
cv2.createTrackbar("VL", "Tracking_Platform", VL_[0], VL_[1], onChange)
cv2.createTrackbar("HU", "Tracking_Platform", HU_[0], HU_[1], onChange)
cv2.createTrackbar("SU", "Tracking_Platform", SU_[0], SU_[1], onChange)
cv2.createTrackbar("VU", "Tracking_Platform", VU_[0], VU_[1], onChange)

# Detect the object you desire based on its colour
# Working with Frames

while (myvideo_.isOpened):

    Captured_Boolean, Frame = myvideo_.read()

    # Convert the frame from RGB Colour Space to HSV Colour Space
    Frame_HSV = cv2.cvtColor(Frame, cv2.COLOR_BGR2HSV)

    # Cretaing a Mask for each object
    HL_ = cv2.getTrackbarPos("HL", "Tracking_Platform")
    SL_ = cv2.getTrackbarPos("SL", "Tracking_Platform")
    VL_ = cv2.getTrackbarPos("VL", "Tracking_Platform")
    HU_ = cv2.getTrackbarPos("HU", "Tracking_Platform")
    SU_ = cv2.getTrackbarPos("SU", "Tracking_Platform")
    VU_ = cv2.getTrackbarPos("VU", "Tracking_Platform")

    Lower_Bound = np.array([HL_, SL_, VL_])
    Upper_Bound = np.array([HU_, SU_, VU_])

    Mask = cv2.inRange(Frame_HSV, Lower_Bound, Upper_Bound)

    # Detect the Object by using Bit-wise AND between Mask created and the main RGB Frame
    Object_Detected = cv2.bitwise_and(Frame, Frame, mask=Mask)

    # Show the resuls
    cv2.imshow("Tracking_Platform", Frame)
    cv2.imshow("Mask", Mask)
    cv2.imshow("Object_Detected", Object_Detected)

    if cv2.waitKey(25) & 0xFF == 27:
        break
    elif Captured_Boolean == False:
        break

myvideo_.release()
cv2.destroyAllWindows()






