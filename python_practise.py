#!/usr/bin/env python
# coding: utf-8

# Priniting all students name from a list

# In[2]:


students_f_name_list = ["ram", "Hari","Shyam","Gita"]


# In[3]:


students_last_name_list = ['Sharma',"Kadel","Oli","Nepal"]


# List Concatenation

# In[4]:


students_fname_lname_list = students_f_name_list + students_last_name_list


# In[5]:


students_fname_lname_list


# Combine lists by element wise

# In[22]:


students = zip(students_f_name_list,students_last_name_list)


# In[23]:


type(students)


# In[24]:


new_list = []
for i,j in students:
    new_list.append(i + str(" ") + j)


# In[25]:


new_list


# In[ ]:




