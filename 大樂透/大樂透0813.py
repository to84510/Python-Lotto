# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:06:54 2019

@author: 信諺
"""
number=[]
one49=[]
lot=[]
money=int(0)
import random

# 新增1-49號碼至空串列one49
for i in range(1,50):
    one49.append(i)

# 請客人輸入號碼，且防呆
def _number(number):
    for i in range(6):
        num=int(input("請輸入第%s個號碼(1-49):"% (i+1)))
        number.append(num)
        if(num<1 or num>49):
            print("輸入錯誤，請重新填單!")
            break
        if (number.count(num)>1):
            print("重複輸入，請重新填單!")
            break
    number.sort()
    print("您的號碼為:%s" % (number))
    return number

# 先將one49串列蕤隨機打散，再從one49串列裡取前六個為開獎號碼
def _one49(one49,lot):
    random.shuffle(one49)
    for i in range(6):
        lot.append(one49[i])
    lot.sort()
    print("本次開獎號碼為: % s" % lot)
    return one49,lot

#判斷中了幾個號碼，且公布獎金
def _lot(money,number,lot):
    for i in range(len(number)):
        for j in range(len(lot)):
            if (number[i] == lot[j]):
                money += 1
                break
    if (money < 3):
        print("很可惜您只中了%d個號碼，沒有獎金!"%money)
    elif (money==3):
        print("恭喜您中了3個號碼，獎金400元!")
    elif (money==4):
        print("恭喜您中了4個號碼，獎金4000元!")
    elif (money==5):
        print("恭喜您中了5個號碼，獎金五十萬元!")
    elif (money==6):
        print("恭喜您中了3個號碼，獎金一千萬元!")
    return money

_number(number)
_one49(one49,lot)
_lot(money,number,lot)
    
