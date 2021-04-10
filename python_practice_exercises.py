#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.) Write the code that takes a single string containing make and model of vehicle
#example:
#truck = "toyota tacoma"
#the frist part of the string is the make last part is the model.
# strings will only have one space assume the string is lower case


# In[12]:


make = 'cheverolet'
model = 'silverado 1500'

make_and_model = f'{make.lower()}' + ' ' + f'{model.lower()}'
print(make_and_model)


# In[106]:


# 2.) write the code to take a string and produce a dictionary out of that string
#such that the output is the following 
#need a way to get the first part of the string and a way to get your hands on the second part of the string free to make new variable/data types "in between the string and output odictionary"
##input:
#truck = 'tacoma'
#output:
#truck = {
#"make": "toyota",
#"model": "tacoma"

make = 'cheverolet'
model = 'silverado'

make_and_model = f'{make.lower()}' + ' ' + f'{model.lower()}'



make_and_model_s = make_and_model.split()

make_s = make_and_model_s[0]
model_s = make_and_model_s[1]

vehicle = {
    'make': make_s,
    'model': model_s}

print(vehicle)


# In[109]:


#2.) write the code that takes a dictionary 
#containing make/modelb for a vehicle and capaitalizes the first character of the make and the model:
# title function
make = 'cheverolet'
model = 'silverado'

make_and_model = f'{make.lower()}' + ' ' + f'{model.lower()}'



make_and_model_s = make_and_model.split()

make_s = make_and_model_s[0]
model_s = make_and_model_s[1]

vehicle = {
    'make': make_s.capitalize(),
    'model': model_s.capitalize()}

print(vehicle)


# In[129]:


# create a list of three dictionaries where each dictionary represents a vehicle as above 
# write the code that operates on that list of dictionairies in order to uppercase the entire make and model values
# truck = {
#truck = {
#"make": "toyota",
#"model": "tacoma"}#
#then returns this in all caps, use yell
# making three dictionaries
# makes everything uppercase

# TO DO: make three dictionaries /
# create a list which contains those three/
# upper case the make and model values
trucks = [{'make': 'ford',
           'model':'f150'
         },
          {'make': 'toyota',
           'model':'tacoma'
          },
          {'make': 'chevrolet',
           'model':'silverado'
          }]


truck = trucks[0]
truck2 = trucks[1]
truck3 = trucks[2]

truck['model'] = truck['model'].upper()
truck['make'] = truck['make'].upper()

for truck in trucks:
    truck['make'] = truck['make'].upper()
    truck['model'] = truck['model'].upper()
    
print(trucks)



# In[ ]:


# wierd trick to solve loop porblems, blow off the loop.

