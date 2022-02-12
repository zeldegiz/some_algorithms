def factorial(x,y):
    m = y-x
    if(m==0):
        return x
    elif(m==1):
        return x*(x+1)
    elif(m==2):
        return x*(x+1)*(x+2)
    elif(m==3):
        return x*(x+1)*(x+2)*(x+3)
    elif(m==4):
        return x*(x+1)*(x+2)*(x+3)*(x+4)
    else:
        k = int(m/5)
        return factorial(x,x+k)*factorial(x+k+1,x+2*k)*factorial(x+2*k+1,x+3*k)*factorial(x+3*k+1,x+4*k)*factorial(x+4*k+1,y)

