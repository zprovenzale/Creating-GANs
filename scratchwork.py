import pandas as pd
#imports below are for putting images into a list and converting them into black and white/having them as arrays as 1s and 0s
# Help converting images from https://www.pluralsight.com/guides/importing-image-data-into-numpy-arrays , and some of the code in the loop is from that
import numpy as np


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

'''
def replaceLabel(string, num):
    print("string:", string, "num:", num, 'str(num):', str(num))
    newLabels = [sub.replace(string, str(num)) for sub in imageLabelsFull]
    print('newLabels[:20]:', newLabels[:20])
    for numStr in newLabels:
        numStr = int(numStr)
    return newLabels
'''

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



print(imageLabels[0:20])
print(imageLabelsFull[0:20])



numTrainingImages = 9000

trainingImageNames = imageNameList[:numTrainingImages]
training_labels = imageLabels[:numTrainingImages]

testImageNames = imageNameList[numTrainingImages:]
test_labels = imageLabels[numTrainingImages:]





# TRAINING LABELS


# import data, read into df
HandInfoData = pd.read_csv("HandInfo - HandInfo.csv")

handInfo = pd.DataFrame(HandInfoData)

#I only imported the first 229 photos
handInfo = handInfo[0:50]

handLabel = handInfo["aspectOfHand"]

#make array
training_labels = np.asarray(handLabel)

len(training_labels)