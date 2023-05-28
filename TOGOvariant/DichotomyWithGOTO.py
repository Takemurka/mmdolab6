def goto(label):
    global current_label
    current_label = label

def label(label_name):
    pass


def MyDichotomyMethod(f,a,b,epsilon):
    error = epsilon/3
    label('a')
    x1 = (a+b-error)/2
    x2 = (a+b+error)/2
    f1 = f(x1)
    f2 = f(x2)
    if(f1<=f2):
        b=x2
    else:
        a =x1
    if(b-a<epsilon):
        xStar = (a+b)/2
        fStar = f(xStar)
        return xStar,fStar
    else:
        goto('a')
