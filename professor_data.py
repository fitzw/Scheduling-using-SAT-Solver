
# coding: utf-8

# In[1]:

# import csv


# with open('professor_data', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(mylist)


# In[27]:

import random as rd
import csv
Course_number = 50


# In[21]:

P = {'A':[0,3,[],(1,30),'Building A','Tue'],
    'B':[1,3,[],(2,30),'Building A','Tue'],
     'C':[2,1,[],(1,30),'Building A','Fri'],
     'D':[3,2,[],(1,30),'Building B','Mon'],
     'E':[4,1,[],(1,30),'Building A','WED'],
     'F':[5,2,[],(1,30),'Building C','Tue'],
     'G':[6,3,[],(1,30),'Building B','Thu'],
     'H':[7,1,[],(1,30),'Building C','Thu'],
     'I':[8,2,[],(1,30),'Building A','Tue'],
     'J':[9,1,[],(1,30),'Building C','Fri'],
    }


# In[24]:

for k in P:
    iter_n = P[k][1]
    P[k][2] = []
    for i in range(iter_n):
        P[k][2].append(rd.randint(1,Course_number))


# In[25]:

P


# In[32]:

# with open('Prof_data.csv', 'w') as f:  # Just use 'w' mode in 3.x
#     w = csv.DictWriter(f, P.keys())
#     w.writeheader()
#     w.writerows(P)
       
with open('Prof_data.csv','w') as f:
    w = csv.writer(f)
    w.writerows(P.items())    

