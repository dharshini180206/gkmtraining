Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
x=5
x
5
type(x)
<class 'int'>
id(x)
140737059742968
x=10.09734853
type(x)
<class 'float'>
type(x)
<class 'float'>
id(x)
2794621274800
s1='hi'
id(s1)
140737059788216
s1='hello'
id(s1)
2794619566288
nums=[10,20,30,40,50]
nums
[10, 20, 30, 40, 50]
len(nums)
5
nums[3]
40
nums[7]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    nums[7]
IndexError: list index out of range
nums[1:5]
[20, 30, 40, 50]
nums[2:4]
[30, 40]
nums[:5:2]
[10, 30, 50]
nums[2]=300
nums
[10, 20, 300, 40, 50]
id(nums)
2794581052352
nums.append(60)
nums
[10, 20, 300, 40, 50, 60]
nums.count(40)
1
nums.count(400)
0
nums.index(300)
2
nums.insert(4, 1000)
nums
[10, 20, 300, 40, 1000, 50, 60]
nums.pop()
60
nums.remove(1000)
nums
[10, 20, 300, 40, 50]
nums.reverse()
nums
[50, 40, 300, 20, 10]
nums.sort()
nums
[10, 20, 40, 50, 300]
nums.sort(reverse=True)
nums
[300, 50, 40, 20, 10]
nums2=nums.copy()
nums
[300, 50, 40, 20, 10]
nums2
[300, 50, 40, 20, 10]
id(nums)
2794581052352
id(nums2)
2794620925760
nums3=nums
nums
[300, 50, 40, 20, 10]
nums3
[300, 50, 40, 20, 10]
id(nums3)
2794581052352
nums3.clear()
nums3
[]
del(nums3)
nums3
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    nums3
NameError: name 'nums3' is not defined. Did you mean: 'nums'?
nums=[10,20,30,40,50]
nums.append(10)
nums.append(50)
nums
[10, 20, 30, 40, 50, 10, 50]
nums2
[300, 50, 40, 20, 10]
nums.extend(nums2)
nums
[10, 20, 30, 40, 50, 10, 50, 300, 50, 40, 20, 10]
data=(100,200,300,400)
data
(100, 200, 300, 400)
type(nums)
<class 'list'>
type(data)
<class 'tuple'>
data[3]
400
data[1:3]
(200, 300)
data.count(200)
1
data.index(300)
2
data.index(3000)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    data.index(3000)
ValueError: tuple.index(x): x not in tuple
data=(100,200,300,400)
data
(100, 200, 300, 400)
details={100,200,300,400,200,300}
details
{100, 300, 400, 200}
type(details)
<class 'set'>
details[3]
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    details[3]
TypeError: 'set' object is not subscriptable
id(details)
2794625294720
details.add(10)
details
{100, 200, 10, 300, 400}
id(details)
2794625294720
details.discard(300)
details
{100, 200, 10, 400}
details.pop
<built-in method pop of set object at 0x0000028AACA5E180>
details.pop()
100
details
{200, 10, 400}
details.pop()
200
details.add(100)
details.add(300)
>>> deatails.add(700)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    deatails.add(700)
NameError: name 'deatails' is not defined. Did you mean: 'details'?
>>> details.add(100)
>>> details.add(300)
>>> details.add(700)
>>> details
{100, 10, 300, 400, 700}
>>> len(details)
5
>>> det1={1,2,3,4,5}
>>> det1
{1, 2, 3, 4, 5}
>>> details
{100, 10, 300, 400, 700}
>>> details.union(det1)
{1, 2, 3, 100, 4, 5, 10, 300, 400, 700}
>>> detais.intersection(det1)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    detais.intersection(det1)
NameError: name 'detais' is not defined. Did you mean: 'details'?
>>> details.intersection(det1)
set()
>>> det2
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    det2
NameError: name 'det2' is not defined. Did you mean: 'det1'?
>>> det2={1,3,5,7,9}
>>> det1.intersection(det2)
{1, 3, 5}
>>> det1.difference(det2)
{2, 4}
>>> det2.difference(det1)
{9, 7}
>>> det1.remove(det2)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    det1.remove(det2)
KeyError: {1, 3, 5, 7, 9}
>>> det2.remove(7)
>>> det2
{1, 3, 5, 9}
>>> det1.update(det1)
>>> det1
{1, 2, 3, 4, 5}
>>> det2.update(det1)
>>> det1
{1, 2, 3, 4, 5}
>>> det2.update(det1)
... det2
SyntaxError: multiple statements found while compiling a single statement
>>> student={1: 'A', 2: 'B', 3: 'C'}
>>> stud
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    stud
NameError: name 'stud' is not defined
student
{1: 'A', 2: 'B', 3: 'C'}






type(student)
<class 'dict'>
stud[3]
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    stud[3]
NameError: name 'stud' is not defined
student[3]
'C'
student[4]='D'
student
{1: 'A', 2: 'B', 3: 'C', 4: 'D'}
id(student)
2794625687104
student[5]='E'
student
{1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
id(student)
2794625687104
student={'rno':123, 'name':'AAA'}
student
{'rno': 123, 'name': 'AAA'}
student['name']
'AAA'
student.keys()
dict_keys(['rno', 'name'])
student.values()
dict_values([123, 'AAA'])
student.items()
dict_items([('rno', 123), ('name', 'AAA')])
student.get('rno')
123
student.pop('rno')
123
student
{'name': 'AAA'}
