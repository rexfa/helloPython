class Location(object):
    def __init__(self,x,y):
        self.x,self.y = x,y
    def move(self,deltaX,deltaY):
        return Location(self.x+deltaX,self.y+deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self,other):
        ox,oy= other.x,other.y 
        xDist = self.x-ox
        yDist = self.y-oy
        return(xDist**2+yDist**2)**0.5


