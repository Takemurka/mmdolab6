def goto(label):
    global current_label
    current_label = label

def label(label_name):
    pass

def Mylocalization_search(f, x0, h, epsilon):
    f1 = f(x0)
    label('first')
    h=h/2
    x2 = x0+h
    f2 = f(x2)
    if(f1<=f2):
        h = -h
        x2 = x0+h
        f2 = f(x2)
    else:
        pass
    if(f1>f2 or abs(h)<epsilon):
        if(abs(h)>epsilon):
            label('a')
            x1 = x2
            f1=f2
            x2 = x1+h
            f2 = f(x2)
            if(f1<f2):
                if(h>0):
                    a = x1-h
                    b=x2
                    return a,b
                else:
                    a = x2
                    b = x1-h
                    return a,b
            else:
                goto('a')
        else:
            xStar = x0
            fStar = f(xStar)
            return xStar, fStar
    else:
        goto('first')




