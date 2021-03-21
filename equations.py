def exponent(x):
    i=1
    numerator=1
    assembly = 1
    answer = 1
    while i < 100:
        numerator= numerator*x
        assembly= assembly*i
        answer= answer*(numerator/assembly)
        i=i+1
        return answer
    
def ln(x):
    i=1
    y=1
    while i < 100:
        y=y+(2*((x-exponent(y))/(x+exponent(y))))
        i=i+1
    return y

def xtimesty(x,y):
    if x>0:
        sum_= exponent(y*ln(x))
        return sum_
    else:
        x=(-1)*x
        sum_= exponent(y*ln(x))
    return (-1)*sum_

def sqr(x,y):
    sqr_= xtimesty(x,(1/y))
    return sqr_()

def calculate(x):
    sum_num = (xtimesty(2.71828182846, x)*xtimesty(2, x)*xtimesty(x, 1))
    return float('%0.6f' % sum_num)

try:
    x=float(input('plz enetr number:'))
    print(calculate(x))
except:
    print(int(0))



    
    