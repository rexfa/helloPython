import pylab
import random
def variance(X):
    mean = sum(X)/len(X)
    tot = 0.0
    for x in X:
        tot +=(x-mean)**2
    return tot/len(X)
def stdDev(X):
    return variance(X)**0.5

def plotMeans(numDicePerTrial,numDiceThrown,numBins,legend,color,style):
    means=[]
    numTrials = numDiceThrown//numDicePerTrial
    for i in range(numTrials):
        vals=0
        for j in range(numDicePerTrial):
            vals += 5*random.random()
        means.append(vals/numDicePerTrial)
    pylab.hist(means,numBins,color = color,label=legend,weights=pylab.array(len(means)*[1])/len(means),hatch=style)
    return sum(means)/len(means),variance(means)

mean,var = plotMeans(1,10000,11,'1 die','w','*')
print('Mean of rolling 1 die =',round(mean,4),'Variance = ',round(var,4))
mean,var = plotMeans(100,10000,11,'100 dice','w','//')
print('Mean of rolling 100 dice =',round(mean,4),'Variance = ',round(var,4))
pylab.title('Rolling Continuous Dice')
pylab.xlabel('value')
pylab.ylabel('Probability')
pylab.legend()
pylab.show()
