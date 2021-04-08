#!/usr/bin/env python
# coding: utf-8

# ## Conditional Basics

# In[ ]:



#prompt the user for a day of the week, print out whether the day is Monday or not
#prompt the user for a day of the week, print out whether the day is a weekday or a weekend


# In[19]:


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
current_day = ['Monday']
for day in days:
    if day in current_day:
        print('Monday')
    else:
        print('Not Monday')


# In[20]:


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in days:
    if day in week_days:
        print('weekday')
    else:
        print('weekend')


# In[ ]:


#create variables and make up values for
#-- the number of hours worked in one week --
#-- the hourly rate --
#-- how much the week's paycheck will be --
# --write the python code that calculates the weekly paycheck. 
# -- You get paid time and a half if you work more than 40 hours


# In[23]:


number_of_hours = 60
hourly_rate = 33
over_time = number_of_hours > 40

overtime_pay = (hourly_rate/2) + hourly_rate
weekly_paycheck_no_over = number_of_hours * hourly_rate

over_time_pay = over_time * overtime_pay

weekly_pay_with_overtime = weekly_paycheck_no_over + overtime_pay

print('${:,.2f}'.format(over_time_pay), 'overtime')
print('${:,.2f}'.format(weekly_paycheck_no_over), 'weekly no overtime')
print('${:,.2f}'.format(weekly_pay_with_overtime), 'weekly with overtime')
 


# In[ ]:





# # LOOP BASICS

# ## Part a.)

# In[ ]:


#Create an integer variable i with a value of 5.
i = 5


# In[3]:


i = 5
while i <= 15:
    print(i)
    i += 1


# In[4]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2


# In[24]:


for n in range(0,101,2):
    print(n)


# In[2]:


# Alter your loop to count backwards by 5's from 100 to -10.
for n in range(100,-11, -5):
   print(n)


# In[25]:


i = 100
while i >= -10:
    print(i)
    i -= 5
    


# In[27]:


#Create a while loop that starts at 2, and displays the number squared on each 
#line while the number is less than 1,000,000. Output should equal:
#2
#4
#16
#256
#65536

i = 2
while i <= 1000000:
    print(i)
    i **= 2


# In[7]:


#Write a loop that uses print to create the output shown below. 100 to 5 by 5

i=105
while i >= 5:                              
    i += -5
    print(i)


# In[ ]:


#For Loops

#Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

#For example, if the user enters 7, your program should output:


# In[12]:



n = int(input("Input a number: "))

# use for loop to iterate 10 times
for i in range(1,11):
   print(n,'x',i,'=',n*i)


# In[18]:


print(['1']* 1)
print(['2']* 2)


# In[15]:


for i in range(10):
    print(str(i) * i)

#1
#22
#333
#4444
#55555
#666666
#7777777
#88888888
#999999999


# In[ ]:


#2.c)
#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement 
#to continue prompting the user if they enter invalid input. 
#(Hint: use the isdigit method on strings to determine this). 
#Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
#except for the number the user entered.


# In[28]:


while True:
    posited_num = input('Please inser and odd number between 1 and 50: ')
    if posited_num.isdigit():
        if int(posited_num) % 2 == 1 and int(posited_num) <= 50:
            break


# In[ ]:


poisted_num = int(posited_num)
for num in range(1,50,2):
    if num == posited_num:
        print('yikes! Skipping number:', num )
    else:
        print('here is a ', num )   


# In[ ]:


#2.d) The input function can be used to prompt for input and 
#use that input in your python code. Prompt the user to enter a positive number 
#and write a loop that counts from 0 to that number. 
#(Hints: first make sure that the value the user entered is a valid number, 
#also note that the input function returns a string, 
#so you'll need to convert this to a numeric type.)


# In[29]:


while True:
    posited_num = input('Please insert a positive int: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
posited_num = int(posited_num)
for num in range(0, posited_num +1):
    print(num)


# In[33]:


#2.e) Write a program that prompts the user for a positive integer. 
#Next write a loop that prints out the numbers from the number the user
#entered down to 1.

while True:
    posited_num = input('Please insert a positive int: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
posited_num = int(posited_num)
for num in range(posited_num, 0, -1):
    print(num)


# In[ ]:


#3.) Fizzbuzz
#One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

#Write a program that prints the numbers from 1 to 100.
#For multiples of three print "Fizz" instead of the number
#For the multiples of five print "Buzz".
#For numbers which are multiples of both three and five print "FizzBuzz".


# In[36]:


for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif 1 % 5 == 0:
        print('Buzz')
    else:
        print(i)


# In[ ]:


#4.) Display a table of powers.

#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.


# In[ ]:


while True:
    posited_num = input('Please insert a positive int: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break
proceed = input('Do you want to continue and print a table of powers? :')
if proceed.lower().startswith('y'):
    posited_num = int(posited_num)
    print()
    print('number | squared | cubed')
    print('------ | ------- | -----')
    for i in range(1, posited_num, +1):
        i_squared = i ** 2
        i_cubed = i ** 3
        print(f'{i: 6} | {i_squared: 7} | {i_cubed: 5}')


# In[ ]:





# Convert given number grades into letter grades.
# 
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# 
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# 
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.
