#Import pandas for data wrangling
import pandas as pd
#imports below are for putting images into a list and converting them into black and white/having them as arrays as 1s and 0s
# Help converting images from https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays , and some of the code in the loop is from that


from PIL import Image # Help with images from https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays
import numpy as np 
#import matplotlib.pyplot as plt
import os # help with path from https://careerkarma.com/blog/python-check-if-file-exists/
from numpy import asarray


#Read hand csv
Handdf = pd.read_csv('HandInfo - HandInfo.csv')

#We want to filter out accessories and nail polish
Handdf = Handdf.query('accessories == 0 & nailPolish == 0 & irregularities == 0') #creates a new dataframe


# Then get a series of the image name column and the labels (i.e. "aspect of hand")
imageNameList = Handdf['imageName']
imageLabelsFull = Handdf['aspectOfHand']

#Convert image labels into numbers instead of strings -- method from https://www.geeksforgeeks.org/python-replace-substring-in-list-of-strings/
# dorsal right - 0
# dorsal left - 1
# palmar right - 2
# palmar left - 3

def replaceLabel(string, num):
    newLabels = [sub.replace(string, str(num)) for sub in imageLabelsFull]
    for numStr in newLabels:
        numStr = int(numStr)
    return newLabels

imageLabels = replaceLabel('dorsal right', 0)
imageLabels = replaceLabel('dorsal left', 1)
imageLabels = replaceLabel('palmar right', 2)
imageLabels = replaceLabel('palmar left', 3)

#hi = map(replaceLabel, (('dorsal right', 0), ('dorsal left', 1), ('palmar right', 2), ('palmar left', 3))) #help with map() from https://www.w3schools.com/python/ref_func_map.asp
#imageLabels = list(hi)
print(imageLabels[0:20])


"""
numTrainingImages = 9000

trainingImageNames = imageNameList[:numTrainingImages]
training_labels = imageLabels[:numTrainingImages]

testImageNames = imageNameList[numTrainingImages:]
test_labels = imageLabels[numTrainingImages:]





# TRAINING LABELS

make sure to convert labels to numbers
"""
# import data, read into df
#HandInfoData = pd.read_csv("HandInfo - HandInfo.csv")
"""
handInfo = pd.DataFrame(HandInfoData)

#I only imported the first 229 photos
handInfo = handInfo[0:50]
"""
#handLabel = handInfo["aspectOfHand"]

#make array
#training_labels = np.asarray(handLabel)

#len(training_labels)




# Note: right now it's imageNameList that's the list of all of the images in the .csv (that weren't filtered out). We need to get it so that there are two for loops, one converting a list of training images and the other converting a list of testing images.



"""
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
        # load the image and make the image black and white and resize them so they are all 96x96 pixels
        image = Image.open(r"C:\Users\hvclab\Desktop\Creating-GANs\Hands\\" + imageName).convert('L').resize((96,96))
        #Hiiiii is the problem that you need 2 backslashes between each folder?
        # convert image to numpy array (numpy arrays are like a two dimensional way to store data and know its location)
        #data = asarray(image)
        #images.append(data)
    
    # IF WE WANT TO ONLY DO A SUBSET
    #iterate in the while loop
    #i +=1

    #if i >100:
    #    break


# If we want to see any of the images we can run:
#plt.imshow(images[0])

# Convert the list of images to an array
#listOfImages = np.asarray(images)
#print(len(listOfImages))

# notes on github
# it wouldn't push and had issues -- solved with https://stackoverflow.com/questions/46175462/vs-code-git-push-is-not-pushing-the-code-to-remote
# also look at https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html