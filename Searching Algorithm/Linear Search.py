#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Instruction: By clicking 'E' or 'e' , user input taking will be completed.")

print("Press 'Enter' to continue")


# In[2]:


lst = []


# In[3]:


while True:
    
    i = input()
    
    if i == 'E' or i == 'e':
        
        break
        
    else:
        
        i = int(i)
        lst = lst + [i]
        
print("Input taking completed!")

print(lst)


# In[4]:


print('Enter whatever you want to search....')

find = int(input())


# In[5]:


position = 0

flag = 0

track_position = []

for element in lst:
    
    position = position + 1
    
    if element == find:
        
        flag = flag + 1
        
        track_position = track_position + [position]
        
print('Position: ', track_position)

if flag == 0 :
        
    print('Oops!!! What you have searched is not in the list!')
    

