#!/usr/bin/env python3
import math

class ABC:

    A = int(input("A = "))
    B = int(input("B = "))
    C = int(input("C = "))

    def X1(a, b, c):
        square_root = math.sqrt(b*b + 4*a*c)
        x1 = -b + square_root / 2 * a
        result = x1

        return result

    def X2(a, b, c):
        square_root = math.sqrt(b*b +4*a*c)
        x2 = -b - square_root / 2 * a
        result = x2

        return result

def outputABC():

    xOne = ABC.X1(ABC.A, ABC.B, ABC.C)
    xTwo = ABC.X2(ABC.A, ABC.B, ABC.C)

    print(":: X1 = ", xOne)
    print(":: X2 = ", xTwo)

outputABC()


