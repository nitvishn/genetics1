# -*- coding: utf-8 -*-
"""
Created on Wed May  3 20:49:20 2017

@author: nvishnu
"""
import random
import pylab
random.seed()
red=3
green=7
yellow=23
reproducedict={red+green:'brown', red+red:'red', green+green:'green', red+yellow:'red', green+yellow:'green', yellow+yellow:'yellow'}
colordict={red:'red', green:'green', yellow:'yellow'}
colordict2={'red':red, 'green':green, 'yellow':yellow}

class NoFishException(Exception):
    pass

class Fish(object):
    def __init__(self, gene1, gene2):
        self.gene1=gene1
        self.gene2=gene2
        self.color=reproducedict[gene1+gene2]
    def returnColor(self):
        return self.color

def removeGenes(genepool,color,numFish):
    color=colordict2.get(color, color)
    if(color=='brown'):
        newpool=[]
        numRedRemoved=0
        numGreenRemoved=0
        for gene in genepool:
            if(gene==red and numRedRemoved!=numFish):
                numRedRemoved+=1
            elif(gene==green and numGreenRemoved!=numFish):
                numGreenRemoved+=1
            else:
                newpool.append(gene)
        return newpool
                
    newpool=[]
    numremoved=0
    for gene in genepool:
        if(gene==color and numremoved!=numFish*2):
            numremoved+=1
            continue
        else:
            newpool.append(gene)
    return newpool

def makeFish(genepool):
    fishies=[]
    random.shuffle(genepool)
    for i in range(0, len(genepool), 2):
        try:
            fishies.append(Fish(genepool[i], genepool[i+1]))
        except:
            pass
    return fishies

def countFishies(fishies, color):
    counter=0
    for fish in fishies:
        if(fish.returnColor()==color):
            counter+=1
    return counter

def updateInfo(fishies, redData, yellowData, greenData, brownData):
    redData.append(countFishies(fishies, 'red'))
    yellowData.append(countFishies(fishies, 'yellow'))
    greenData.append(countFishies(fishies, 'green'))
    brownData.append(countFishies(fishies, 'brown'))

def runSimulation(numFishies, firstDeath=None, secondDeath=None, thirdDeath=None):
    genepool=[]
    for i in range(numFishies*2):
        genepool.append(random.choice([green, yellow, red]))
    redData=[]
    yellowData=[]
    greenData=[]
    brownData=[]
#    print(genepool.count(red), genepool.count(green), genepool.count(yellow))
    #start simulation
    for i in range(100):  
        fishies=makeFish(genepool)
        updateInfo(fishies, redData, yellowData, greenData, brownData)
    if(firstDeath!=None):
        for i in range(100):  
            fishies=makeFish(genepool)
            updateInfo(fishies, redData, yellowData, greenData, brownData)
            listMap={'red':redData, 'green':greenData, 'yellow':yellowData, 'brown':brownData}
            genepool=removeGenes(genepool, firstDeath, listMap[firstDeath][-1])
    
    if(secondDeath!=None):
        for i in range(100):  
            fishies=makeFish(genepool)
            updateInfo(fishies, redData, yellowData, greenData, brownData)
            listMap={'red':redData, 'green':greenData, 'yellow':yellowData, 'brown':brownData}
            genepool=removeGenes(genepool, secondDeath, listMap[secondDeath][-1])
    pylab.figure()
    pylab.plot(redData, 'r-', label='reds')
    pylab.plot(greenData, 'g-', label='greens')
    pylab.plot(yellowData, 'y-', label='yellows')
    pylab.plot(brownData, 'm-', label='browns')
    if(firstDeath!=None):
        pylab.axvline(100, label=firstDeath+'s die', ls='--', color='k')
    if(secondDeath!=None):
        pylab.axvline(200, label=secondDeath+'s die', ls='--', color='b')
    pylab.legend()
    pylab.title("Survival of the Fittest")
    pylab.xlabel("Generations")
    pylab.ylabel("Number of Fishies")
    print("\n\nPopulation at end\n")
    print('red fish:', redData[-1])
    print('yellow fish:', yellowData[-1])
    print('green fish:', greenData[-1])
    print('brown fish:', brownData[-1])

runSimulation(1000, firstDeath='red', secondDeath='green')