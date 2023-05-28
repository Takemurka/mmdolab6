from math import log
from function import f


def Mylocalization_search(x0, h, epsilon):
    print("-" * 100)
    print(f"Виконання методу пошуку відрізка локалізації точки мінімуму при eps = {epsilon}")
    print("-" * 100)
    nk = 0
    nf = 1
    f1 = f(x0)
    nf += 1
    nk += 1
    h /= 2
    x2 = x0 + h
    f2 = f(x2)
    nf += 1
    print(f"Крок 1 : Покласти x = x0 | x = {x0} та обчислити f(x) = {f1}")
    while True:
        if not (f1 > f2 or abs(h) < epsilon):
            nk += 1
            h /= 2
            x2 = x0 + h
            f2 = f(x2)
            print(f"Крок 2 : Обрахування h = h/2 | h ={h}, x2 = x0+h | x2= {x2}, f(x2) = {f2}")
            nf += 1
            print(f"Крок 3 : Якщо f1 <= f2, то : \n"
                  f"h = -h, x2=x0+h, f2=f(x2), інакше перейти до кроку 4")
            if f1 <= f2:
                h = -h
                x2 = x0 + h
                f2 = f(x2)
                nf += 1
            print(f"Крок 4 : Якщо f1>f2 чи |h|<ε, то : \n"
                  f"перейти до кроку 5\n"
                  f"інакше перейти до кроку 2")
        else:
            break
    print(f"Крок 5 :  |h|>ε, то : \n"
          f"x1=x2,f1=f2,x2=x1+h,f2=f(x2) та перейти до кроку 6\n"
          f"інакше вивести x*=x0; f*=f(x*), вивести дані та алгоритм завершено")

    if abs(h) > epsilon:

        x1 = x2
        f1 = f2
        x2 = x1 + h
        f2 = f(x2)
        nf += 1
        while True:
            if not (f1 < f2):
                nk+=1
                x1 = x2
                f1 = f2
                x2 = x1 + h
                f2 = f(x2)
                nf += 1
            else:
                break
        print(f"Крок 6 : Якщо h>0, то : \n"
              f"a=x1-h, b=x2\n"
              f"інакше : a=x2, b=x1-h\n"
              f"перейти до кроку 7")
        if h > 0:
            a = x1 - h
            b = x2
        else:
            a = x2
            b = x1 - h
        print(f"Крок 7 : вивести дані та алгоритм завершено")
        return nk, nf, a, b
    else:
        nf += 1
        print(f"Крок 7 : вивести дані та алгоритм завершено")
        print("-" * 100)
        return nk, nf, x0, f(x0)




