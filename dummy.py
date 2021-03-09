#!/bin/python

print("hello from the long branch")

a = 'unused variable'

b = None

c = 2

d = c / b

e = a + c  # should trigger rule Operators should be used on compatible types

foo = 1 == "1"  # Noncompliant. Always False.


print("We're done")



