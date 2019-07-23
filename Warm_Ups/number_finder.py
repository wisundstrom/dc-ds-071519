
def prime_finder(array):
    primelist=[]
    iarray= np.array.astype(int)
    for num in iarray:
        maxnum=int(num/2)
        for i in range(1,maxnum):
            j=num/i
            if j%1!=0 and i%1!=0:
                continue
            else:
                primelist.append(num)
    
        
def fibn(n):
    r5=5**.5
    fib1= ((1+r5)/2)
    fib2= ((1-r5)/2)
    fib= (fib1**n)-(fib2**n)
    return int(fib/r5)

def fibonacci_finder(array):
    arraymax=max(array)
    exptarg=np.log(arraymax)/np.log(1.61803439887)
    n=int(exptarg+3)
    fibs=list(map(fibn, list(range(n))))
    fibaarray= np.array(fibs)
    
    return numpy.intersect1d(array, fibarray)
              
