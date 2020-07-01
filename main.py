import numpy as np
import pyautogui
import imutils
import cv2
import time
from PIL import *
# take a screenshot of the screen and store it in memory, then  (Line 18)
# convert the PIL/Pillow image to an OpenCV compatible NumPy array (Line 19)
# and finally write the image to disk (Line 20)

num_img = 0

time.sleep(10) # This is the time for you to open the window or the textbook ready for screenshoting


for num_img in range(83, 192, 1):
    
    image = pyautogui.screenshot(region=(0, 110, 1920, 968)) # Tells where to take a screenshot image = pyautogui.screenshot(region=(Left, Top, Right, Bottom)) 
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 
    cv2.imwrite("G:\DEV Current\Software Screen Capture\Images Pure 4\Page" + str(num_img) + ".png", image)


    # print(pyautogui.size()) 
    # Output (width=1920, height=1080)

    pyautogui.click(1800, 400) # Tells the place where to click pyautogui.click(width, height)
    num_img = int(num_img)
    time.sleep(60)

imagelst = []
image1 = Image.open("G:\DEV Current\Software Screen Capture\Images Pure 3\Page0.png") #Opens an image 
img1 = image1.convert("RGB") # Converts the image into a compatible numpy array form for processing

for num_img in range(1, 115, 1):
    imagen = Image.open("G:\DEV Current\Software Screen Capture\Images Pure 3\Page" + str(num_img) + ".png")
    imn = imagen.convert("RGB")
    imagelst.append(imn) # appends each image into the list imagelst

img1.save("G:\DEV Current\Software Screen Capture\Pure 3.pdf",save_all=True, append_images=imagelst) # Takes all the images in the list and saves it one below the other 
