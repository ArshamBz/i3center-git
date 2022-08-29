import cv2
import sys
import argparse
import numpy as np


def parse_args(arguments):
    Parser_HSV = argparse.ArgumentParser(description="Command Line Arguments")

    Parser_HSV.add_argument("--Video_Source",
                            help="The source of video",
                            default=r"C:\Users\Python_Course\Desktop\i3Center\Python_Advanced\OpenCV\Video_Test\Balls.mp4")

    Parser_HSV.add_argument("--HL",
                            help="Hue Low Range",
                            default=[0, 180])

    Parser_HSV.add_argument("--SL",
                            help="Saturation Low Range",
                            default=[0, 255])

    Parser_HSV.add_argument("--VL",
                            help="Value Low Range",
                            default=[0, 255])

    Parser_HSV.add_argument("--HU",
                            help="Hue Up  Range",
                            default=[0, 180])

    Parser_HSV.add_argument("--SU",
                            help="Saturation Up Range",
                            default=[0, 255])

    Parser_HSV.add_argument("--VU",
                            help="Value Up Range",
                            default=[0, 255])

    return Parser_HSV.parse_args(arguments)


# =============================================================================
# Import CLA
Args = sys.argv[1:]
Args = parse_args(Args)

Video_Source = Args.Video_Source
HL = Args.HL
SL = Args.SL
VL = Args.VL
HU = Args.HU
SU = Args.SU
VU = Args.VU
# =============================================================================

# Import your PC's Camera
Video_Cam = cv2.VideoCapture(0)

# Create a track bar

cv2.namedWindow("Tracking_Platform")


def onChange(X):
    pass


cv2.createTrackbar("HL", "Tracking_Platform", HL[0], HL[1], onChange)
cv2.createTrackbar("SL", "Tracking_Platform", SL[0], SL[1], onChange)
cv2.createTrackbar("VL", "Tracking_Platform", VL[0], VL[1], onChange)
cv2.createTrackbar("HU", "Tracking_Platform", HU[0], HU[1], onChange)
cv2.createTrackbar("SU", "Tracking_Platform", SU[0], SU[1], onChange)
cv2.createTrackbar("VU", "Tracking_Platform", VU[0], VU[1], onChange)

# Detect the object you desire based on its colour
# Working with Frames

while (Video_Cam.isOpened):

    Captured_Boolean, Frame = Video_Cam.read()

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

Video_Cam.release()
cv2.destroyAllWindows()