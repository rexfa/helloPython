import pylab
def clear(n,p,steps):
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-p)**t))
    pylab.plot(numRemaining)
    pylab.xlabel('time')
    pylab.ylabel('Molecules Remaining')
    pylab.title('Clearance of Drug')
    pylab.show()


clear(1000,0.01,1000)