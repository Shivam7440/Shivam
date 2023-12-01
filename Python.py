#!/usr/bin/env python
# coding: utf-8

# In[2]:


#unit 1 Lesson 8 Inout and Output formatting
a=10
b=20
c="python"
print("a=",a,"b=",b,"c=",c)


# In[ ]:


# format specifier %
get_ipython().run_line_magic('d->integer', '')
get_ipython().run_line_magic('s->string', '')
get_ipython().run_line_magic('f->float', '')
get_ipython().run_line_magic('x', 'or %X->hexadecimal')
get_ipython().run_line_magic('o->octal', '')


# In[3]:


a=10
b=20
c="python"
print("a=%6d,b=%.8f and c=%s" %(a,b,c))


# In[4]:


a=10
b=20
c="python"
#hexadecimal 0-15 0-9 10-a,11-b,12-c,13-d,14-e,15-f
#octal 0-7
print("a=%x,b=%o and c=%s"% (a,b,c))


# In[ ]:


#format()
# {}->string
# {:d}->integer
# {:f}->float
# {:x} or {:X}->hexadecimal
# {:o}->octal


# In[6]:


a=10
b=20
c="python"
print("a={:4d},b={:.3f} and c={}" .format(a,b,c))


# In[7]:


a=10
b=20
c="python"
print("a={:x},b={:o} and c={}" .format(a,b,c))


# In[ ]:




