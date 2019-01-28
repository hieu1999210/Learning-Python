print("Hello")

# def fib(n):
#     """Assumes int n >= 0
#     Return Fibonacci of n"""
#     global numFibCalls
#     numFibCalls +=1
#     if n == 0 or n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# def testFib(n):
    
#     for i in range(n):
#         global numFibCalls
#         numFibCalls = 0
#         print("Fib of",i,"=", fib(i))
#         print("Fib called", numFibCalls, "times")
# testFib(5)
# fib()

# def isPalindrome(s):
#     """Assumes s is a string.
#     Return True if letters in s form a palindrome.
#     False otherwise.
#     Non-letter and capitalization are ignored."""

#     def toChar(s):
#         s = s.lower()
#         letters = ""
#         for c in s:
#             if c in "abcdefghiklmnopqrstuvwxyz":
#                 letters = letters + c
#         return letters

#     def isPar(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPar(s[1:-1])
#     return isPar(toChar(s))

# def testIsPalindrome():
#     print("'abcdef' is Palindrome: ", str(isPalindrome("abcdef")))
#     print("'aba' is Palindrome: ", str(isPalindrome("aba")))

# testIsPalindrome()

#------------------------------------

import circle

def testCircle():
    print(circle.PI)
    print(circle.area(3))
    print(circle.circumference(3))
    print(circle.sphereSurface(3))
    print(circle.sphereVolume(3))

testCircle()