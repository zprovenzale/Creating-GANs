import pandas as pd

#creating a data frame 
handInfo = pd.read_csv('HandInfo - HandInfo.csv')

#creating boolean variables to make a data frame of info of all hand that do not have nail polish, acessories, or irregularities
noNailPolish = handInfo[nailPolish] == 0
noAccessories = handInfo[accessories] == 0
noIrregularities = handInfo[irregularities] == 0

#creating a separate data frame that only includes Hand Info for hands that do not have nail polish, accessories of irregularities
newHandInfo = handInfo[noNailPolish] & handInfo[noAccessories] & handInfo[noIrregularities]

#accessing a list of all the image names that do not have nail polish, accessories or irregularities
#this can be used to create a separate file of all the pictures of hands we will actually be using to train our neural network
handImageNames = newHandInfo[imageName].list()
