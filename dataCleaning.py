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

imageLabels = []
for entry in imageLabelsFull:
    if entry == 'dorsal right':
        imageLabels.append(0)
    elif entry == 'dorsal left':
        imageLabels.append(1)
    elif entry == 'palmar right':
        imageLabels.append(2)
    elif entry == 'palmar left':
        imageLabels.append(3)
    else:
        print("Not one of the four categories wtf")



#sets the number of images we want to be training
numTrainingImages = 5000

#makes a list of all the images and labels we use for training. this makes a list of the first 5000 images
trainingImageNames = imageNameList[:numTrainingImages]
trainingLabels = imageLabels[:numTrainingImages]

#makes a list of all the images and labels used for training. this makes a list of the remaining ~2000 images
testImageNames = imageNameList[numTrainingImages:]
testLabels = imageLabels[numTrainingImages:]



#   FOR LOOP FOR CONVERTING EACH IMAGE

#TRAINING IMAGES

# We need a list of the arrays for each image
trainingImages = []
# i = 0 # If we want to run a subset of images, break after that num is reached
for image in trainingImageNames:

    imageName = str(image)

    # Check if the image exists (some might not for human error reasons) 
    # used to check whether the specified path (the path is just a parameter, in this case we use image but path can essentially be any object) is an existing regular file or not

    if os.path.isfile(r"C:\Users\hvclab\Desktop\Creating-GANs\Hands\\" + imageName):
        print("loading images here")

        # load the image and make the image black and white and resize them so they are all 96x96 pixels
        image = Image.open(r"C:\Users\hvclab\Desktop\Creating-GANs\Hands\\" + imageName).convert('L').resize((96,96))
        #Hiiiii is the problem that you need 2 backslashes between each folder?
        # convert image to numpy array (numpy arrays are like a two dimensional way to store data and know its location)
        data = asarray(image)
        trainingImages.append(data)
    else:
        print("wtf")
    
    # IF WE WANT TO ONLY DO A SUBSET
    #iterate in the while loop
    #i +=1

    #if i >100:
    #    break



# TESTING IMAGES

# We need a list of the arrays for each image
testImages = []
# i = 0 # If we want to run a subset of images, break after that num is reached
for image in testImageNames:

    imageName = str(image)

    # Check if the image exists (some might not for human error reasons) 
    # used to check whether the specified path (the path is just a parameter, in this case we use image but path can essentially be any object) is an existing regular file or not

    if os.path.isfile(r"C:\Users\hvclab\Desktop\Creating-GANs\Hands\\" + imageName):
        print("loading images here")

        # load the image and make the image black and white and resize them so they are all 96x96 pixels
        image = Image.open(r"C:\Users\hvclab\Desktop\Creating-GANs\Hands\\" + imageName).convert('L').resize((96,96))
        #Hiiiii is the problem that you need 2 backslashes between each folder?
        # convert image to numpy array (numpy arrays are like a two dimensional way to store data and know its location)
        data = asarray(image)
        testImages.append(data)
    else:
        print("wtf")
    
    # IF WE WANT TO ONLY DO A SUBSET
    #iterate in the while loop
    #i +=1

    #if i >100:
    #    break




# If we want to see any of the images we can run:
plt.imshow(testImages[0])

# Convert the lists of images to an array
trainingImages = np.asarray(trainingImages)
testImages = np.asarray(testImages)
print(len(trainingImages))
print(len(testImages))

# notes on github
# it wouldn't push and had issues -- solved with https://stackoverflow.com/questions/46175462/vs-code-git-push-is-not-pushing-the-code-to-remote
# also look at https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html
