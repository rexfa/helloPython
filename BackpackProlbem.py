class Item(object):
    def __init__(self,name,value,weight):
        self.name = name
        self.value = value
        self.weight = weight
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        return '<'+self.name+','+self.value+','+self.weight+'>'
    def getDensity(self):
        return self.value/self.weight

def greedy(items,maxWeight,keyFunction):
    itemsCopy = sorted(items,key=keyFunction,reverse=True)
    result = []
    totalValue,totalWeight = 0,0
    for i in range(len(itemsCopy)):
        if (totalWeight+itemsCopy[i].getWeight())<=maxWeight:
            result.append(itemsCopy[i])
            totalWeight = totalWeight + itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()
    return (result,totalValue)
