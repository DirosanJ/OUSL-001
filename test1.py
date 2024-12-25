Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Function Fibonacci(n):
...     If n is less than 0:
...         Return "Invalid Input"
...     Else If n == 0:
...         Return 0
...     Else If n == 1:
...         Return 1
...     Else:
...         Initialize first = 0
...         Initialize second = 1
...         For i from 2 to n:
...             temp = first + second
...             first = second
...             second = temp
...         End For
...         Return second
