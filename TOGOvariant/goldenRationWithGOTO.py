import math

def goto(label):
    global current_label
    current_label = label

def label(label_name):
    pass
def myGoldenRation(f,a,b,epsilon):
    u = a+(3-math.sqrt(5))/2*(b-a)
    v = a+b-u
    fu=f(u)
    fv=f(v)
    label('a')
    if(fu<=fv):
        b=v
        v=u
        fv=fu
        u=a+b-v
        fu=f(u)
    else:
        a = u
        u = v
        fu = fv
        v = a + b - u
        fv = f(v)
    if(u>v):
        u = a + (3 - math.sqrt(5)) / 2 * (b - a)
        v = a + b - u
        fu = f(u)
        fv = f(v)
    else:
        pass

    if b-a<epsilon:
        xStar = (a+b)/2
        fStar = f(xStar)
    else:
        goto('a')

    return xStar,fStar
