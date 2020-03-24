"""
装饰器原理：
1.函数本身是一个对象
2.作用域
3.闭包
作用：在不修改原来函数代码的情况下，为其增加新的功能
"""

import time 

#打印另一个函数的执行时间
def timer(func):
    def demo(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time =time.time()
        print(end_time-start_time)
        return result
    return demo

@timer   #语法糖
def add(x,y):
    time.sleep(2)
    return x + y


本质过程

def sub(x,y):
    time.sleep(2)
    return x-y

demo = timer(sub)
sub = demo


------------------------------------
函数闭包:需要两个条件 有个内部函数 有个平级变量   
def foo():
    m = []
    def bar(x):
        m.append(x)
        return m
    return bar 