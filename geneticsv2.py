# -*- coding: utf-8 -*-
"""
Created on Thu May  4 15:30:41 2017

@author: nvishnu
"""
import random
import pylab

white=5
red=19
colorDict={red+red:'red', white+white:'white', white+red:'pink'}

class Flower(object):
    def __init__(self, gene1, gene2):
        self.gene1=gene1
        self.gene2=gene2
        self.color=colorDict[gene1+gene2]
    
    def returnColor(self):
        return self.color
    
    def returnGenes(self):
        return (self.gene1, self.gene2)

def reproduce(Flower1, Flower2):
    gene1=random.choice(Flower1.returnGenes())
    gene2=random.choice(Flower2.returnGenes())
    return Flower(gene1, gene2)

def countFlowers(flowers):
    countDict={'white':0, 'red':0, 'pink':0}
    for flower in flowers:
        countDict[flower.returnColor()]=countDict.get(flower.returnColor(), 0)+1
    return countDict

def reproduceAll(flowers):
    for i in range(0, len(flowers), 2):
        try:
            flowers.append(reproduce(flowers[i], flowers[i+1]))
        except:
            pass

keyColors={'white':'k', 'red':'r', 'pink':'m'}
def plotData(flowerData):
    pylab.figure()
    for key in flowerData:
        pylab.plot(flowerData[key], label=key, color=keyColors[key])
    pylab.legend()
        
        
def runSingleSim(flowers, generations):
    flowerData={'pink':[], 'white':[], 'red':[]}
    for i in range(generations):
        reproduceAll(flowers)
        data=countFlowers(flowers)
        for element in data.keys():
            flowerData[element].append(data[element])
    return flowerData

def runSim(flowers, generations, numTrials):
    allFlowerData=[]
    for trial in range(numTrials):
        sim=runSingleSim(flowers, generations)
        allFlowerData.append(sim)
    realData={'white':[], 'red':[], 'pink':[]}
    
    for color in allFlowerData[0].keys():
        for index in range(generations):
            total=0
            for trial in allFlowerData:
                total+=trial[color][index]
            realData[color].append(total/numTrials)
    
    plotData(realData)
flowers=[Flower(white, red), Flower(white, red)]
runSim(flowers, 5, 10)
    
    
    
    
    
    
    
    
    
    
    
    