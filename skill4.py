# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 21:35:26 2021

@author: quentin
"""

def q1():
    print("A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists.")
    print("The differences between tuples and lists are,the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets")

def q2():
    import matplotlib.pyplot as pp
    n, x, y = 121, [], []
    for i in range(0,n+1):
        if i%2 ==0:
            x.append(i)
            y.append(i*i-2*i)
    pp.plot(x,y, label= "f(x) = x² - 2x")
    pp.title('question 2 - skill 4')
    pp.xlabel('x')
    pp.ylabel('f(x)')
    pp.legend()
    pp.show()

def q3():
    print('the statement c) d = {89:"adam", 95:"brenda"}\
          is creating a dictionary')

def mySum(lastNumber):
    i, S = 0, 0
    while i <= lastNumber:
        S = S + i
        i+=1
    return S
    

print("\n>> question 1 :\n")
q1()
print("\n>> question 2 : (see graph)\n")
q2()
print("\n>> question 3 :\n")
q3()
print("\n>> question 4 :\n",mySum(3))