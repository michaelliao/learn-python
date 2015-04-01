#!/usr/bin/env python3
# -*- coding: utf-8 -*-

g = (x * x for x in range(10))
print(g)
for x in g:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)
