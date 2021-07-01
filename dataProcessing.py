import pandas as pd

#creating boolean variables to make a data frame of info of all hand that do not have nail polish, acessories, or irregularities
noNailPolish = HandInfo[nailPolish] == 0
noAccessories = HandInfo[accessories] == 0
noIrregularities = HandInfo[irregularities] == 0

#creating a separate data frame that only includes Hand Info for hands that do not have nail polish, accessories of irregularities
newHandInfo = HandInfo[noNailPolish] & HandInfo[noAccessories] & HandInfo[noIrregularities]

