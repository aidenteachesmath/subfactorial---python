import math
from tkinter import *


window=Tk()

def D(n):
   
    if n == 0:
        return 1
    elif n == 1:
        return 0
    else:
        return (n - 1) * (D(n - 1) + D(n - 2))


def i():
    global a,b
    a=int(e1.get())
    if  a >= 0:
        D_result = D(a)
        factorial_result = math.factorial(a)
        b=D_result*100/factorial_result

        label.configure(text=f"D({a})는 {D_result}입니다.\n{a}명이 있을때의 모자가 모두 자기 것이 아닐 확률은 {b}입니다.")
    else:
        label.configure(text="0이상의 수를 입력해주세요.")
