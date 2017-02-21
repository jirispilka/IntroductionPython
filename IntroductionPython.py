
# coding: utf-8

# Scientific Programming in Python
# ================================
# 
# Created by:
# 
# * Ian Stokes-Rees [ijstokes@continuum.io]
#  
# Original version github:
#  [https://github.com/ijstokes/python-sci-3h.git](https://github.com/ijstokes/python-sci-3h.git)
#  
# Shortened by Jiri Spilka

# Basics
# ======

# In[1]:

"""
Exercise 1. Introduction to python
"""

import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt


# In[2]:

#  ------ bool
bb = True
print bb


# In[3]:

a = 3
b = 7
print 'Results is = ', a


# In[4]:

x = 10
y = 10.


# In[5]:

print x, y
print type(x), type(y)


# In[6]:

d = 7E4
print d


# In[7]:

# ------- complex numbers

d2 = 3 + 2j
print d2, type(d2)


# Tuples
# -------

# In[8]:

#  ------ tuples
person = ('Arnost', 'Cech', 20)

print person
print type(person)


# In[9]:

print person[0]


# In[10]:

# assigment is not supported for tuple
# person[0] = 'petr jan'


# In[11]:

print 'Size of person: ', sys.getsizeof(person)


# Dictionaries
# --------------
# 

# In[12]:

d = dict()
d['karel'] = 50
d['petr'] = 30
print d

# alternatively
dd = {'key1': 5, 'key2': 3}
print dd


# Lists
# ------

# In[13]:

l = list([10, 20, 50, 100])
l.append(50)
l.pop()


# In[14]:

print 'Count {0}'.format(len(l))


# In[15]:

# list slicing, striding
# this is list not an array
nums = [3, 7, 2, 8, 5, 12, -5, 4]
# len(nums)
nums[7]
nums[-1]
nums[-2]
nums[0]
nums[3:6]  # half open interval: end index is NOT included
nums[5]
nums[1:7:2]
nums
nums[7:0:-2]


# In[16]:

# power operations with power operator
a


# In[17]:

b


# In[18]:

b**a   


# In[19]:

nums


# In[20]:

pow(b, a)


# In[21]:

sum(nums)


# In[22]:

max(nums)


# In[23]:

min(nums)


# In[24]:

range(5)


# In[25]:

range(4, 12)


# In[26]:

# simple functions: params, defaults, return values, scoping
def f(x):
    ' a simple polynomial function '
    return 3*x**2 + 8


# In[27]:

help(f)


# In[28]:

f(1.5)


# In[29]:

f(3.7)


# In[30]:

def f_o(x, offset=8):
    ''' a simple polynomial function with a configurable offset
        offset default's to 8
    '''
    return 3*x**2 + offset


# In[31]:

f_o(1.5)


# In[32]:

f_o(1.5, offset=10)


# In[33]:

f_o(1.5, 10)


# In[34]:

pfunkce = f_o


# In[35]:

print pfunkce(20)


# In[36]:

# PEP 731 - use of lambda expressions is not recommended
# g = lambda x: 7*x**3 + 2
# print g(2)

def g(x): return 7*x**3 + 2
print g(2)


# In[37]:

with open('bostonarea.dat') as fh:
    for line in fh:
        parts = line.split()  # will remove leading and trailing whitespace
        print "found parts:", parts


# In[49]:

# ----- matplotlib a numpy

plt.hold()
t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.01)


# In[50]:

# note that plot returns a list of lines.  The "l1, = plot" usage
# extracts the first element of the list into l1 using tuple
# unpacking.  So l1 is a Line2D instance, not a sequence of lines
l1, = plt.plot(t2, np.exp(-t2))
l2, l3 = plt.plot(t2, np.sin(2 * np.pi * t2), '--go', t1, np.log(1 + t1), '.')
l4, = plt.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 'rs-.')

plt.legend( (l2, l4), ('oscillatory', 'damped'), loc='upper right', shadow=True)
plt.xlabel('time')
plt.ylabel('volts')
plt.title('Damped oscillation')
plt.show()


# In[48]:

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
type(x)


# In[41]:

x.shape


# In[42]:

x.size


# In[43]:

x.dtype


# In[44]:

nums = np.arange(3, 12, 2)
nums.dtype


# In[46]:

# random noise
An = 0.1
noise = An * np.random.randn(x.size)
y = np.sin(x)

OFFSET = 0.001
signal = y + noise + OFFSET

plt.figure()
plt.plot(x, signal, '.')
plt.show()

