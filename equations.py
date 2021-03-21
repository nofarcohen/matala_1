# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:03:33 2021

@author: nofar
"""

def pow_x_y(x:float,y:float):
    p=1.0
    while (y>0):
        p=p*x
        y=y-1
    return(p)
    
def atzeret(y:float):
    n=1.0
    while (y>0):
        n=n*y
        y=y-1
    return(n)
    

def exponent(x:float):
    n=1.0
    Exponentiation=1.0
    while(n<100.0):
       ex=pow_x_y(x,n)/atzeret(n)
       Exponentiation=Exponentiation+ex
       n=n+1
       a= float('%0.6f' %Exponentiation)
    return(a)

def Ln (x: float):
    if (x<=0):
        return 0
    y=x-1.0
    y_1=y+2*((x-exponent(y))/(x+exponent(y)))

    while (True): 
        a=y-y_1
        if (a<0):
            a=-a
        if (a>0.001):
            y=y_1
            y_1=y+2*((x-exponent(y))/(x+exponent(y)))
            a=y-y_1
        else:
            return (y_1)

def XtimesY(x: float,y: float):
    if (x<0):
        return 0
    ans=exponent(y*Ln(x))
    return (ans)


def sqrt(x:float,y:float):
    if (y<=0):
        return 0
    return(XtimesY(y,1/x))


def calculate(x:float):
    if (x<0):
        return 0
    answer=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
    return (answer)


 
   
