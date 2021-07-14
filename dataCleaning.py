#Import pandas for data wrangling
import pandas as pd
#imports below are for putting images into a list and converting them into black and white/having them as arrays as 1s and 0s
# Help converting images from https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays , and some of the code in the loop is from that
from PIL import Image # Help with images from https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays
import numpy as np 
import matplotlib.pyplot as plt
import os # help with path from https://careerkarma.com/blog/python-check-if-file-exists/
from numpy import asarray

#Read hand csv
Handdf = pd.read_csv('HandInfo.csv')

#We want to filter out accessories and nail polish
Handdf = Handdf.query('accessories == 0 & nailPolish == 0 & irregularities == 0') #creates a new dataframe
# Then get a series of the image name column
imageNameList = Handdf["imageName"]

#   WHILE LOOP FOR CONVERTING EACH IMAGE

# We need a list of the arrays for each image
images = []
# i = 0 # If we want to run a subset of images, break after that num is reached
for image in imageNameList:

    imageName = str(image)

    # Check if the image exists (some might not for human error reasons) 
    # used to check whether the specified path (the path is just a parameter, in this case we use image but path can essentially be any object) is an existing regular file or not
    if os.path.isfile(r"C:\Users\hvclab\Desktop\Creating-GANs\Hands\\" + imageName):
        print("loading images here")
        # load the image and make the image black and white
        image = Image.open(r"C:\Users\hvclab\Desktop\Creating-GANs\Hands\\" + imageName).convert('L') #there is a problem with the path that we are using but i can't figure it out
        # convert image to numpy array (numpy arrays are like a two dimensional way to store data and know its location)
        data = asarray(image)
        images.append(data)
    
    # IF WE WANT TO ONLY DO A SUBSET
    #iterate in the while loop
    #i +=1

    #if i >100:
    #    break

print("out of while loop")

# If we want to see any of the images we can run:
#plt.imshow(images[0])

# Convert the list of images to an array
listOfImages = np.asarray(images)
print(len(listOfImages))

print("added friom website to try to pull")
print("please")