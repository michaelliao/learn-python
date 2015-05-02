#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def each_ascii(s):
    for ch in s:
        yield ord(ch)
    return '%s chars' % len(s)

def yield_from(g):
    try:
        while True:
            next(g)
    except StopIteration as s:
        return s.value

def main():
    for x in each_ascii('abc'):
        print(x) # => 'a', 'b', 'c'
    it = each_ascii('xyz')
    try:
        while True:
            print(next(it)) # => 'x', 'y', 'z'
    except StopIteration as s:
        print(s.value) # => '3 chars'

    # using yield from in main() will change main() from function to generator:
    # r = yield from each_ascii('hello')

    print(yield_from(each_ascii('hello'))) # => '5 chars'

main()
