import math
from function import f

def MyDichotomyMethod(arr, epsilon):
    print("-"*100)
    print(f"Виконання методу Дихотомії при eps = {epsilon}")
    print("-"*100)
    a = arr[0]
    b = arr[-1]
    error = epsilon / 3
    nk = 0
    nf = 1
    while b - a >= epsilon:
        nk += 1

        print(f"Ітерація № {nk}")
        x1 = (a + b - error) / 2
        x2 = (a + b + error) / 2
        print(f"Крок 1 : Знаходження точок : x1={x1}, x2={x2}")
        print(f"x1 = {x1}, x2 = {x2}")
        f1 = f(x1)
        nf+=1
        f2 = f(x2)
        print(f"f1 = {f1}, f2 = {f2}")
        nf+=1
        print(f"Крок 2 : Якщо f1 < f2, то покласти а=а, b=x2,x̄=a,f-=f1, інакше a=x1, b=b,x̄=b,f-=f2")
        if f1 <= f2:
            b = x2
        else:
            a = x1
        print(f"Крок 3 : Якщо,b - a < ε, то покласти Nf=2k і перейти на крок 4, в протилежному випадку покласти k:= k+1 і перейти до виконання кроку 1.")

    print("-" * 100)
    return nk,nf,(a + b) / 2, f((a + b) / 2)

