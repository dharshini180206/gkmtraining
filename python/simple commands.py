Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=5
x
5
type(x)
<class 'int'>
y=3.65
type(y)
<class 'float'>
m=567.8765432047873664
type(m)
<class 'float'>
a=true
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
a=true
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
a=True
type(a)
<class 'bool'>
b='Hi'
b
'Hi'
x
5
type(b)
<class 'str'>
c="Hello"
c
'Hello'
b="""hi
hello
how
are
you
"""
d
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
b
'hi\nhello\nhow\nare\nyou\n'
str1='hello'
str1
'hello'
str1.upper()
'HELLO'
str1.lower()
'hello'
str1.count('l')
2
str1.endswith('o')
True
str1.edswith('y')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    str1.edswith('y')
AttributeError: 'str' object has no attribute 'edswith'. Did you mean: 'endswith'?
str1.endswith('y')
False
str1.find('o')
4
str1.find('b')
-1
str1.index('e')
1
str1.index('b')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    str1.index('b')
ValueError: substring not found
str1.isnumeric()
False
str1.isalpha()
True
str1.isdecimal()
False
str1.replace('l','1')
'he11o'
str1.replace('o','0')
'hell0'
str1.replace('l','r')
'herro'
str1.replace('h','z')
'zello'
str1.swapcase()
'HELLO'
str2="India is my country"
str2
'India is my country'
str1
'hello'
len(str1)
5
len(str2)
19
str2.split(' ')
['India', 'is', 'my', 'country']
str2.('$')
SyntaxError: invalid syntax
>>> str2.split('$')
['India is my country']
>>> str2.split('-')
['India is my country']
>>> str2="India is$my-country"
>>> str2
'India is$my-country'
>>> str2.split('$')
['India is', 'my-country']
>>> str2.split('-')
['India is$my', 'country']
>>> str2="India is     my       country"
>>> str2
'India is     my       country'
>>> str2.split(' ')
['India', 'is', '', '', '', '', 'my', '', '', '', '', '', '', 'country']
>>> str1
'hello'
>>> str1[0]
'h'
>>> str1[4]
'o'
>>> str1[5]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    str1[5]
IndexError: string index out of range
>>> str3
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    str3
NameError: name 'str3' is not defined. Did you mean: 'str1'?
>>> x+str1
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    x+str1
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str1+x
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    str1+x
TypeError: can only concatenate str (not "int") to str
>>> str1
'hello'
>>> str1[-1]
'o'
>>> str1[-5]
'h'
>>> str2
'India is     my       country'
>>> str2="India is my country"
>>> str2[0:9]
'India is '
>>> str2[5:]
' is my country'
>>> ' is my country'' is my country'
' is my country is my country'
>>> str2[::3]
'Iiimcny'
