import pylab

def minkowskiDistance(x,y,p):
    try:
        assert len(x)==len(y) #检查向量维度是否一致
    except AssertionError as msg:
        print(msg,"Inconsistent vector dimension")
        return -1
    length=len(x)
    d=0
    for i in range(0,length):
        d = d +abs(x[i]-y[i])**p
    d = d**(1/p)
    return d

def manhattanDistance(x,y):
    return minkowskiDistance(x,y,1)

def euclideanDistance(x,y):
    return minkowskiDistance(x,y,2)


a = (0,0)
b = (1,1)
print("Minkowski Distance p=0.5" , str(minkowskiDistance(a,b,0.5)))
print("Manhattan Distance p=1" , str(manhattanDistance(a,b)))
print("Minkowski Distance p=1.5" , str(minkowskiDistance(a,b,1.5)))
print("Euclidean Distance p=2" , str(euclideanDistance(a,b)))
print("Minkowski Distance p=3" , str(minkowskiDistance(a,b,3)))
print("Minkowski Distance p=8" , str(minkowskiDistance(a,b,8)))

#简易画出文章用的示意图
x = (a[0],b[0])
y = (a[1],b[1])
fig, axes = pylab.subplots(1, 3, figsize=(12,3))
axes[0].scatter(x,y)
axes[1].plot(x,y)
axes[2].plot((a[0],b[0],b[0]),(a[1],a[1],b[1]))
pylab.show()