from GoldenRatio import golden_ratio_method as gr
from SegOLocaizationOfminPoint import Mylocalization_search as SLOMP
from Dichotomy import MyDichotomyMethod as dich
from Fibonachi import FibonaciMethod as fib
from Parabola import ParabolaMethod as pm
from prettytable import PrettyTable
from time import perf_counter as tm
import matplotlib.pyplot as plt
import  numpy as np
from function  import f as f
from scipy.optimize import minimize_scalar as mn
arr = [-1.99,2]

def actionPerformer(arr,eps):
    res = []
    timeList = []
    dichTimeS = tm()
    res.append(dich(arr,eps))
    dichTimeE = tm()
    timeList.append(dichTimeE - dichTimeS)
    grTimeS = tm()
    res.append(gr(arr,eps))
    grTimeE = tm()
    timeList.append(grTimeE - grTimeS)
    fibTimeS = tm()
    res.append(fib(arr, 100))
    fibTimeE = tm()
    timeList.append(fibTimeE - fibTimeS)
    pmTimeS = tm()
    res.append(pm(arr, eps))
    pmTimeE = tm()
    timeList.append(pmTimeE - pmTimeS)
    slompTimeS = tm()
    res.append(SLOMP(arr[0],0.01,eps))
    slompTimeE = tm()
    timeList.append(slompTimeE - slompTimeS)
    return res,timeList
def drawOutput():
    test = tm()
    epsEq2,timeEq2 = actionPerformer(arr,eps = 0.01)
    epsEq4,timeEq4 = actionPerformer(arr, eps=0.0001)
    epsEq8,timeEq8 = actionPerformer(arr, eps=1e-8)
    expl = ['Nk,Nf,x*,f*']
    myTable = PrettyTable()
    myTable.field_names = ["№","Назва методу","esp = 10^-2","esp = 10^-4","esp = 10^-8 ","#","Назва_методу","Час виконання при esp = 10^-2","Час виконання при esp = 10^-4","Час виконання при esp = 10^-8 "]
    myTable.add_row([0, "", expl, expl, expl,'',"","",'',''])
    myTable.add_row([1,"Дихотимії",epsEq2[0],epsEq4[0],epsEq8[0],1,"Дихотимії",timeEq2[0],timeEq4[0],timeEq8[0]])
    myTable.add_row([2, "Золотого перерізу", epsEq2[1], epsEq4[1], epsEq8[1],2, "Золотого перерізу",timeEq2[1],timeEq4[1],timeEq8[1]])
    myTable.add_row([3, "Фібоначі", epsEq2[2], epsEq4[2], epsEq8[2],3, "Фібоначі",timeEq2[2],timeEq4[2],timeEq8[2]])
    myTable.add_row([4, "Парабол", epsEq2[3], epsEq4[3], epsEq8[3],4, "Парабол",timeEq2[3],timeEq4[3],timeEq8[3]])
    myTable.add_row([5, "Пошуку відрізка локалізації точки мінімуму", epsEq2[4], epsEq4[4], epsEq8[4],5, "Пошуку відрізка локалізації точки мінімуму",timeEq2[4],timeEq4[4],timeEq8[4]])
    print(myTable)
    testend = tm()
    print(f"Час виконання усіє програми : {testend-test}")

def drawGraph():
    xk = np.linspace(arr[0], arr[-1], num=100)
    plt.plot(xk, f(xk), label='Графік функції', linestyle='solid')
    min = mn(f)
    plt.plot(min.x,min.fun,'ro',label='Точка мінімуму')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    return

if __name__ == '__main__':
   drawOutput()
   drawGraph()
