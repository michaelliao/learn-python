#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, math

def rnd(count):
    while count > 0:
        count = count - 1
        r = random.randint(0, 100)
        print('-- random number --')
        # 返回随机数r:
        yield r
        # 代理返回tri(r)的yield，可能有很多次:
        ok = yield from tri(r)
        # 相当于:
        # for x in tri(r):
        #     yield x
        print('-- %s --' % ok)
    return 'done'

def tri(r):
    yield r * r
    yield r * r * r
    # 相当于: raise StopIteration('ok')
    return 'ok'

def main():
    for x in rnd(3):
        print(x)

main()
