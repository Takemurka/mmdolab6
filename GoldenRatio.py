
from math import sqrt
from function import f

def golden_ratio_method(arr, epsilon):
    print("-" * 100)
    print(f"Виконання методу Золотого Перерізу при eps = {epsilon}")
    print("-" * 100)
    nk = 0
    nf = 1
    ratio = (sqrt(5) - 1) / 2
    a = arr[0]
    b = arr[1]
    print(f"Знайти точки")
    x1 = a + (1 - ratio) * (b - a)
    x2 = a + ratio * (b - a)
    f1 = f(x1)
    nf+=1
    f2 = f(x2)
    nf+=1

    while abs(b - a) >= epsilon:
        nk += 1
        print(
            "Крок 2 : fu<=fv, то покласти а=а,b=v, x̄=u, f-=f(u), v=u , fv=fu, знайти u= a + b - v і обчислити fu=f(u); "
            "інакше (fu > fv) покласти a= u , b=b , x̄=v , f-=f(v) , u=v , fu=fv, знайти"
            "v= a + b - u і обчислити fv = f(v).")

        if f1 <= f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + (1 - ratio) * (b - a)
            f1 = f(x1)
            nf += 1
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + ratio * (b - a)
            f2 = f(x2)
            nf += 1
        print(
            "Крок 3 : Якщо b-a<ε, то перейти на виконання кроку 4, інакше перейти до виконання кроку 2")
    print("Крок 4 : Вивести : x̄, f-. Кінець алгоритму")
    print("-" * 100)
    return  nk, nf,(a + b) / 2, f( (a + b) / 2)

