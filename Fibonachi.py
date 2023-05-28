from math import sqrt
from function import f

def FibonaciMethod(arr,n):
    print("-" * 100)
    print(f"Виконання методу Фібоначі")
    print("-" * 100)


    nk = 0
    nf = 1
    a = arr[0]
    b = arr[-1]

    u = a + bineFormula(n) / bineFormula(n + 2) * (b - a)
    v = a+b-u
    fu = f(u)
    nf +=1
    fv = f(v)
    print(f"Крок 1 : Знайти точки u={u},v={v} і обчислити fu={fu}, fv={fv} ")
    nf += 1
    for i in range(n):
        nk += 1
        print("Крок 2 : Якщо fu<=fv, то покласти a=a, b=v, x̄=u, f-=f(u), v=u , fv=fu, знайти "
              "u = a + b - v та обчислити fu=f(u);"
              "інакше покласти a=u, b=b, x̄=v, f-=f(v), u=v , fu=fv, знайти "
              "v = a + b - u та обчислити fv=f(v);")
        if fu<=fv:
            b =v
            v = u
            fv = fu
            u = a+b-v
            fu = f(u)
            nf += 1
        else:
            a = u
            u = v
            fu = fv
            v = a+b-u
            fv=f(v)
            nf += 1
        print("Крок 3 : Якщо u>v, то u:=a+Fn-i+1/Fn-i+3*(b-a); v:=a+b-u; fu:=f(u); fv:=f(v), інакше перейти до виконання кроку 4")
        if u>v:
            u = a + bineFormula(n - i + 1) / bineFormula(n - i + 3) * (b - a)
            v = a+b-u
            fu = f(u)
            nf += 1
            fv = f(v)
            nf += 1
        else :
            pass
        print("Крок 4 : Якщо k = n, то перейти на виконання кроку 5, інакше покласти k= k+1 перейти до виконання кроку 2.")

    print("Крок 5 : Вивести x̄, f-. Кінець алгоритму")
    print("-" * 100)
    return nk,nf,(a+b)/2, f((a+b)/2)



def bineFormula(n):
    phi = (1 + sqrt(5)) / 2
    fib = (phi ** n - (1 - phi) ** n) / sqrt(5)
    return fib

