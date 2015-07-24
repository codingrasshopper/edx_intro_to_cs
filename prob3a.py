def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)



def radiationExposure(start, stop, step):

    area = 0
    number = ((stop-start) +1)/step
    for i in range(number-1):
        height = f(start) 
        width = step
        area += (height * width)
        start = start + step
        
    return area


def main():
    print radiationExposure(5,11,1)
    
    
if __name__ =="__main__":
    main()    