import numpy as np
import matplotlib
import PIL
from PIL import Image #64bit
import matplotlib.pyplot as plt
import time
from functools import reduce
from collections import Counter


def whatThisImage(filePath):
    matchedAr=[]
    loadExamples=open("numberExample.txt", 'r').read()
    loadExamples=loadExamples.split('\n')
    
    i=Image.open(filePath)
    iar=np.array(i)
    iar1=iar.tolist();
   
    iQuestion = str(iar1)
    
    for eachExample in loadExamples :
        if len(eachExample) > 3 :
            splitEx = eachExample.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            
            eachPixEx = currentAr.split('],')
            
            eachPixInQ = iQuestion.split('],')
            
            x=0
            
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                    
                x += 1        
                        
    x = Counter(matchedAr)
    graphX=[]
    graphY=[]
    
    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
        
    fig =plt.figure()
    ax1 = plt.subplot2grid((4,4),(0,0),rowspan=1, colspan=4)
    ax2 = plt.subplot2grid((4,4),(1,0),rowspan=3, colspan=4)
    
    ax1.imshow(iar)
    ax2.bar(graphX,graphY, align = 'center')
    plt.ylim(400)
    plt.show()






def createExamples() :
    numberArrayExamples=open("numberExample.txt", 'a')
    numberWeHave= range(0,10)
    versionsWeHave=range(1,10)
    
    for eachNum in numberWeHave:
        for eachVer in versionsWeHave:
            imgFilePath= 'Images/numbers/'+ str(eachNum)+'.'+ str(eachVer) +'.png'            
            ei = Image.open(imgFilePath)
            eiar=np.array(ei)
            eiar1=str(eiar.tolist())
            lineToWrite= str(eachNum)+'::'+ eiar1 +'\n'
            numberArrayExamples.write(lineToWrite)






#converting image black and white to  remove case of hue .and create threshold
def threshold(imageArray):
    balanceAr=[]
    newAr=imageArray
    for eachrow in imageArray:
        for eachPix in eachrow:
            #print(eachpixel)
            avgNum=reduce(lambda x,y: x + y, eachPix[:3])/len(eachPix[:3])
            #print(avgNum)
            balanceAr.append(avgNum)
            balance=reduce(lambda x,y: x + y, balanceAr)/len(balanceAr)
    for eachrow in newAr:
        for eachpix in eachrow:
            eachpix.setflags(write=1)
            if reduce(lambda x,y: x + y, eachpix[:3])/len(eachpix[:3]) > balance:
               # print('in if','balance: ',balance,'reduce: ',reduce(lambda x,y: x + y, eachPix[:3])/len(eachPix[:3]))
                #white
                eachpix[0]=255
                eachpix[1]=255
                eachpix[2]=255
                eachpix[3]=255
            else:
                #Balck and White
                eachpix[0]=0
                eachpix[1]=0
                eachpix[2]=0
                eachpix[3]=255
            
            
    return newAr  




whatThisImage('Images/three.png')
  

          
            
            
            
            
            


