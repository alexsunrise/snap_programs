# -*- coding: utf-8 -*-

# 题目：一瓶啤酒2块钱，两个空瓶可换一瓶啤酒，四个瓶盖可换一瓶啤酒
# 问：10元钱最多可以喝多少瓶啤酒

# exchange beer by bottles
def getBeerByBottle(b):
    return b/2, b%2

# exchange beer by caps
def getBeerByCap(c):
    return c/4, c%4

# exchange beer by money
def getBeerByMoney(m):
    if m % 2 != 0:
        print "money is not an even number, check it again please."
        exit(0)
    return m/2, m%2

# borrow one bottle of beer
def borrow(bottle, cap, beer, balance):
    return bottle+1, cap+1, beer+1, balance-1

# main function to count how many bottles of beer can be drink
def getBeer(m):
    beer = 0
    bottle = 0
    cap = 0
    money = m
    balance = 0
    round = 0

    while( bottle > 0 or cap > 0 or money > 0):
        round += 1
        # exchange beer by money
        if money > 2:
            b, money = getBeerByMoney(money)
            beer += b
            bottle += b
            cap += b
        # exchange beer by bottles
        if bottle >=2:
            # if borrowed from saler
            if balance < 0:
                balance += 1
                bottle -= 2
                continue
            b, _b = getBeerByBottle(bottle)
            beer += b
            bottle = b + _b
            cap += b
        # exchange beer by caps
        if cap >=4:
            # if borrowed from saler
            if balance < 0:
                balance += 1
                cap -= 4
                continue
            c, _c = getBeerByCap(cap)
            beer += c
            bottle += c
            cap = c + _c
        # if have not enough bottles and caps to exchange
        if bottle < 2 and cap < 4:
            # break condition which has nothing to exchange.
            if bottle == 0 and cap == 0 and balance == 0:
                break
            bottle, cap, beer, balance = borrow(bottle, cap, beer, balance)

        print "===================="
        print "round :", round
        print "beer =", beer
        print "bottle =", bottle
        print "cap =", cap
        print "balance =", balance
    print "total beer to drink =" , beer

getBeer(10)
