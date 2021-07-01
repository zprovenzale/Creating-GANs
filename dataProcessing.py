import pandas as pd

#creating boolean variables to make a data frame of info of all hand that do not have nail polish, acessories, or irregularities
noNailPolish = HandInfo[nailPolish] == 0
noAccessories = HandInfo[accessories] == 0
noIrregularities = HandInfo[irregularities] == 0

#creating a separate data frame that only includes Hand Info for hands that do not have nail polish, accessories of irregularities
newHandInfo = HandInfo[noNailPolish] & HandInfo[noAccessories] & HandInfo[noIrregularities]

#accessing a list of all the image names that do not have nail polish, accessories or irregularities
#this can be used to create a separate file of all the pictures of hands we will actually be using to train our neural network
handImageNames = newHandInfo[imageName].list()
