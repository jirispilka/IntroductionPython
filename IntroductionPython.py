
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

# In[40]:


"""
Exercise 1. Introduction to python
"""

import sys
import os.path
import numpy as np
import matplotlib.pyplot as plt


# In[41]:


#  ------ bool
bb = True
print(bb)


# In[42]:


a = 3
b = 7
print('Results is = ', a)


# In[43]:


x = 10
y = 10.


# In[44]:


print(x, y)
print(type(x), type(y))


# In[45]:


d = 7E4
print(d)


# In[46]:


# ------- complex numbers

d2 = 3 + 2j
print(d2, type(d2))


# Tuples
# -------

# In[47]:


#  ------ tuples
person = ('Arnost', 'Cech', 20)

print(person)
print(type(person))


# In[48]:


print(person[0])


# In[49]:


# assigment is not supported for tuple
# person[0] = 'petr jan'


# In[50]:


print()'Size of person: ', sys.getsizeof(person))


# Dictionaries
# --------------
# 

# In[ ]:


d = dict()
d['karel'] = 50
d['petr'] = 30
print d

# alternatively
dd = {'key1': 5, 'key2': 3}
print(dd)


# Lists
# ------

# In[ ]:


l = list([10, 20, 50, 100])
l.append(50)
l.pop()


# In[ ]:


print('Count {0}'.format(len(l)))


# In[ ]:


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


# In[ ]:


# power operations with power operator
a


# In[ ]:


b


# In[ ]:


b**a   


# In[ ]:


nums


# In[ ]:


pow(b, a)


# In[ ]:


sum(nums)


# In[ ]:


max(nums)


# In[ ]:


min(nums)


# In[ ]:


range(5)


# In[ ]:


range(4, 12)


# In[ ]:


# simple functions: params, defaults, return values, scoping
def f(x):
    ' a simple polynomial function '
    return 3*x**2 + 8


# In[ ]:


help(f)


# In[ ]:


f(1.5)


# In[ ]:


f(3.7)


# In[ ]:


def f_o(x, offset=8):
    ''' a simple polynomial function with a configurable offset
        offset default's to 8
    '''
    return 3*x**2 + offset


# In[ ]:


f_o(1.5)


# In[ ]:


f_o(1.5, offset=10)


# In[ ]:


f_o(1.5, 10)


# In[ ]:


pfunkce = f_o


# In[ ]:


print(pfunkce(20))


# In[ ]:


# PEP 731 - use of lambda expressions is not recommended
# g = lambda x: 7*x**3 + 2
# print g(2)

def g(x): return 7*x**3 + 2
print(g(2))


# In[ ]:


with open('bostonarea.dat') as fh:
    for line in fh:
        parts = line.split()  # will remove leading and trailing whitespace
        print("found parts:", parts)


# In[ ]:


# ----- matplotlib a numpy

plt.hold()
t1 = np.arange(0.0, 2.0, 0.1)
t2 = np.arange(0.0, 2.0, 0.01)


# In[ ]:


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


# In[ ]:


x = np.arange(-2*np.pi, 2*np.pi, 0.01)
type(x)


# In[ ]:


x.shape


# In[ ]:


x.size


# In[ ]:


x.dtype


# In[ ]:


nums = np.arange(3, 12, 2)
nums.dtype


# In[ ]:


# random noise
An = 0.1
noise = An * np.random.randn(x.size)
y = np.sin(x)

OFFSET = 0.001
signal = y + noise + OFFSET

plt.figure()
plt.plot(x, signal, '.')
plt.show()

