from function import f

def ParabolaMethod(arr,eps):
    print(f"Виконання методу Парабол при eps = {eps}")
    nk = 0
    nf = 0
    a = arr[0]
    b = arr[-1]

    x0,x1,x2=find_good_triple(a,b)
    f0,f1,f2 = f(x0),f(x1),f(x2)
    print(f"Крок 0 : На відрізку [a,b] | [{a,b}] визначити першу вдалу трійку x0={x0}, x1={x1}, x2={x2} і обчислити f(x0)={f0}, f(x1)={f1}, f(x2) = {f2}")
    nf+=3
    flag = False

    while(flag ==False):
        nk+=1

        xStar=(x0+x1)/2+(f1-f0)*(x2-x0)*(x2-x1)/(2*((f1-f0)*(x2-x0)-(f2-f0)*(x1-x0)))
        fStar = f(xStar)
        print(f"Крок 1 : Знайти точку x̄={xStar} і обчислити f(x̄) ={fStar}\n")
        nf+=1
        print(f"Крок 2 : Якщо |x̄-x1|<ε, то покласти x*=x̄, f*=f(x̄) і перейти до кроку 4,\n"
              f"інакше якщо x̄>x1, то покласти x0=x1, x1=x1,x3=x2,x2=x̄,\n"
              f"інакше покласти : x0=x0,x3=x2,x2=x1,x1=x̄\n")
        if abs(x1-xStar)>=eps and abs(x2-xStar)>=eps:
            flag = False
            if xStar<x1:
                x3 = x2
                x2 = x1
                x1 = xStar
                f3 = f2
                f2 = f1
                f1 = fStar
            else :
                if xStar>x1:
                    x3 = x2, x2 = xStar
                    f3 = f2, f2 = fStar

                else :
                    pass
            print("Крок 3 : Якщо f1 > f2, то : \n"
                  "x0=x1; f0=f1; x1=x2; f1=f2; x2=x3; f2=f3")
            if(f1>f2):
                x0 = x1,x1=x2,x2=x3
                f0 = f1,f1=f2,f2=f3
            else :
                pass
        else :
            flag = True
    print("Крок 4 : Алгоритм закінчено")
    print("-" * 100)
    return nk,nf,xStar,fStar

def find_good_triple(a, b):
    fa = f(a)
    fb = f(b)
    c = (a + b) / 2
    while True:
        fc = f(c)

        if fc < fa and fc < fb:
            return a, c, b
        elif fa < fb:
            b = c
            fb = fc
        else:
            a = c
            fa = fc


        c = (a + b) / 2
