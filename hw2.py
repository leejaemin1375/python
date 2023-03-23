#!/usr/bin/env python
# coding: utf-8

# In[4]:


def get_integer(prompt) :
    res = int(input(prompt))
    return res;

def exchange(res) :
    n500 = res//500
    n100 = (res-(500*n500))//100
    n50 = (res-(500*n500)-(100*n100))//50
    n10 = (res-(500*n500)-(100*n100)-(50*n50))//10
    print('500원 동전의 개수 : ', n500)
    print('100원 동전의 개수 : ', n100)
    print('50원 동전의 개수 : ', n50)
    print('10원 동전의 개수 : ', n10)
    
res = get_integer('동전으로 교환하고자 하는 금액은?')
exchange(res)


# In[ ]:





# In[ ]:




