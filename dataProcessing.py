import pandas as pd

#creating boolean variables to make a data frame of info of all hand that do not have nail polish, acessories, or irregularities
noNailPolish = HandInfo[nailPolish] == 0
noAccessories = HandInfo[accessories] == 0
noIrregularities = HandInfo[irregularities] == 0

