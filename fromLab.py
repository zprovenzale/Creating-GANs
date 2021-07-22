#Import pandas for data wrangling
import pandas as pd
#imports below are for putting images into a list and converting them into black and white/having them as arrays as 1s and 0s
# Help converting images from https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays , and some of the code in the loop is from that


from PIL import Image # Help with images from https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays
import numpy as np 
import matplotlib.pyplot as plt
import os # help with path from https://careerkarma.com/blog/python-check-if-file-exists/
from numpy import asarray
import tensorflow as tf
from tensorflow.python.ops.gen_nn_ops import Conv2D

#sets parameter type variables
numPixels = 200 #number of pixels on each side of square
incIrregs = 0 #include irregularities in images, 1 for yes, 0 for no
incAccessories = 0 #include accessories in images, 1 for yes, 0 for no
incNailPolish = 0 #include nail polish in images, 1 for yes, 0 for no
numTrainingImages = 5000 #sets the number of images we want to be training

#Initializes variables
trainingImages = []
testImages = []
n = 0

#name of the text file that stores or will store an list of the cleaned numpy array version of files
npImgsFileName = "npImgs" + str(numPixels) + "px" + str(incIrregs) + "i" + str(incAccessories) + "a" + str(incNailPolish) + "n" + ".txt"

#Saves list of the numpy array version of the images to a .txt file
def writeToFile():
    list = []

    #Goes through each training image and then test image, turns the numpy array into a string, and add it to the list
    for i in range(numTrainingImages):
        string = np.array_str(trainingImages[i])
        string += "\n"
        list.append(string)
    for i in range(len(testImages)):
        string = np.array_str(testImages[i])
        string += "\n"
        list.append(string)

    file = open(npImgsFileName, "w")
    file.writelines(list)
    file.close()

#turns .txt file into trainingImages and testImages lists of the numpy array version of images
def readFromFile():
    file = open(r"C:\Users\hvclab\Desktop\Creating-GANs\\" + npImgsFileName,"r")
    string = ""
    n = 0
    
    #Reads lines from the file one at a time. For the first 5000 (Or however many training images we pick), it
    #adds that line to the trainingImages list. Once we finish with those, adds the rest of the lines to the testImages list
    for i in range(500000):
        line = file.readline()
        if (line[:2] == "[["):
            npArray = np.fromstring(string)
            trainingImages.append(npArray)
            string = ""
            n += 1
            if (n == numTrainingImages):
                break
        string += line
        #print("string: ", string)
        #print(len(trainingImages))
        #print(i, " n: ", n)
    for i in range(totalNumImgs - numTrainingImages):
        line = file.readline()
        if (line == ""):
            break
        if (line[:2] == "[["):
            npArray = np.fromstring(string)
            testImages.append(npArray)
            string = ""
            n += 1
        string += line
        #print("string: ", string)
        #print(len(trainingImages))
        #print(i, " n: ", n)

 

    file.close()
    #TODO add something that makes sure this was done successfully, and that the image here is connected
    #to the right image name and other data. Perhaps by checking the length of the lists and pick a few images
    #as a sample and test if they're name connection is right. Right now we are just depending on the index in the
    #arrays to match and there are enough in between steps that we want to be careful. We could also add some if 
    #stamtemnts to see if each line is approximately what we expect in size  and stuff

#Converts image to a numpy array
def imgToNpArray(image):
    #   FOR LOOP FOR CONVERTING EACH IMAGE

    imageName = str(image)

    # Check if the image exists (some might not for human error reasons) 
    # used to check whether the specified path (the path is just a parameter, in this case we use image but path can essentially be any object) is an existing regular file or not

    if os.path.isfile(r"C:\Users\hvclab\Desktop\Creating-GANs\Hands\\" + imageName):
        #this is to keep track of what image we are on
      #  if n % 100 == 0: 
       #     print("loading training image number", n)
        # load the image and make the image black and white and resize them so they are all 96x96 pixels
        image = Image.open(r"C:\Users\hvclab\Desktop\Creating-GANs\Hands\\" + imageName).convert('L').resize((200,200)) #CHANGE BOTH BABE
        # convert image to numpy array (numpy arrays are like a two dimensional way to store data and know its location)
        data = asarray(image)
        image.close()
        return data
    else:
        print("wtf")
    
    # IF WE WANT TO ONLY DO A SUBSET (also to keep track of what we are on)
    #iterate in the for loop
   # n +=1

    #if n >100:
    #    break

    # If we want to see any of the images we can run:
    #plt.imshow(testImages[0])

#Read hand csv
Handdf = pd.read_csv('HandInfo - HandInfo.csv')

#We want to filter out accessories and nail polish
Handdf = Handdf.query('accessories == ' + str(incAccessories) + ' & nailPolish == ' + str(incNailPolish) + ' & irregularities == ' + str(incIrregs)) #creates a new dataframe

# Then get a series of the image name column and the labels (i.e. "aspect of hand")
imageNameList = Handdf['imageName']
imageLabelsFull = Handdf['aspectOfHand']
totalNumImgs = len(imageNameList)

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

#********************************************************************************
#DRIVER STARTS HERE

#makes a list of all the images and labels we use for training. this makes a list of the first 5000 images
trainingImageNames = imageNameList[:numTrainingImages]
trainingLabels = imageLabels[:numTrainingImages]

#makes a list of all the images and labels used for training. this makes a list of the remaining ~2000 images
testImageNames = imageNameList[numTrainingImages:]
testLabels = imageLabels[numTrainingImages:]

#makes testlabels and traininglabels into np arrays that can be used in tensorflow
testLabels = np.asarray(testLabels)
print(type(testLabels))
trainingLabels = np.asarray(trainingLabels) 
print(type(trainingLabels))

#If we have numpy arrays with the same number of pixels and same filters on file, load that.
#Otherwise, turn the images into numpy arrays to use this time and save it in case we need it again
if os.path.isfile(r"C:\Users\hvclab\Desktop\Creating-GANs\\" + npImgsFileName):
    readFromFile()
else:
    n = 0
    for image in trainingImageNames:
        data = imgToNpArray(image)
        trainingImages.append(data)
        n += 1
        if (n%100==0):
            print("loading image ", n)
    for image in testImageNames:
        data = imgToNpArray(image)
        trainingImages.append(data)
        n += 1
        if (n%100==0):
            print("loading image ", n)
    writeToFile()

# Convert the lists of images to an array
#Maybe incorporate this into the file saving situation, I didn't notice these until it was too late
trainingImages = np.asarray(trainingImages)
testImages = np.asarray(testImages)


#adding trainingImages and testImages to the global list networkData to be used in other files
print('this is the length of the training images', len(trainingImages))
print('this is the length of the testing images', len(testImages))


######NEURAL NETWORK TRAINING########
#making each value in the numpy array between 0 and 1
trainingImages = trainingImages / 255.0
testImages = testImages / 255.0

#####define model#####
#for sources on how we did this, look at tensorflow tutorial 
model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(64, (3, 3), activation = 'relu',
                                        input_shape = (5000, 200, 200, 1)),
                                    tf.keras.layers.MaxPooling2D(2, 2),
                                    tf.keras.layers.Flatten(),
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu), #changed from 128 to 400
                                    tf.keras.layers.Dense(4, activation=tf.nn.softmax)])

model.summary()

########define model######
model.compile(optimizer = tf.keras.optimizers.Adam(),
                loss = 'sparse_categorical_crossentropy',
                metrics = ['accuracy'])

######training guidlines######
model.fit(trainingImages, trainingLabels, epochs = 5)
print('done training')

######test model#######
model.evaluate(testImages, testLabels)
print('done testing')


# notes on github
# it wouldn't push and had issues -- solved with https://stackoverflow.com/questions/46175462/vs-code-git-push-is-not-pushing-the-code-to-remote
# also look at https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html

#first change: size of image increase fro, 96 to 128
#second change: epoch to 10 instead of 5 (changed back)
#third: changed loss to loss_fn
#changed loss to binary_crossentropy (this one did HORRIBle and also threw an error (ValueError I am unsure on what to do about this))
#tried categorical crossentropy (also had huge lossed and an error)