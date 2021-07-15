



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



#print(imageLabels[0:20])
#print(imageLabelsFull[0:20])
print("BEGIN")

print(len(imageLabels))


numTrainingImages = 5000

trainingImageNames = imageNameList[:numTrainingImages]
training_labels = imageLabels[:numTrainingImages]

testImageNames = imageNameList[numTrainingImages:]
test_labels = imageLabels[numTrainingImages:]


print(type(testImageNames))
print(len(testImageNames))

print(type(trainingImageNames))
print(len(trainingImageNames))

print(type(test_labels))
print(len(test_labels))

print(type(training_labels))
print(len(test_labels))

print(test_labels[0:20])
print(training_labels[0:20])

print(testImageNames[0:20])
print(trainingImageNames[0:20])








# TRAINING LABELS


