import time
def intuitiveFib(n):
    if n==0 or n==1:
        #print(1)
        return 1
    else:
        fib = intuitiveFib(n-1)+intuitiveFib(n-2)
        #print(fib)
        return fib

print('start 0:'+ time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(intuitiveFib(30))
print('end 0:'+ time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
def fastFid(n,memory={}):
    if n == 0 or n==1:
        return 1
    else:
        try:
            return memory[n]
        except:
            memory[n] = fastFid(n-1,memory)+fastFid(n-2,memory)
            return memory[n]
print('start 1:'+ time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(fastFid(30))
print('end 1:'+ time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
