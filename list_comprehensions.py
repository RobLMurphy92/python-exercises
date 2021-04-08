fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)

# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]

# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())


# In[ ]:



# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.


# In[1]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']


# In[82]:


# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [x.upper() for x in fruits]
uppercased_fruits


# In[81]:


uppercased_fruits = [fruit.upper() for fruit in fruits]


# In[5]:


# Exercise 2 - create a variable named capitalized_fruits 
# and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits =[x.title() for x in fruits]
capitalized_fruits


# In[83]:


capitalized_fruits = [fruit.title() for fruit in fruits]


# In[84]:


capitalized_fruits = [fruit.capitalize() for fruit in fruits]


# In[87]:


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.
# have to nest it, treat string like list of characters
fruit1 = 'mango'


# In[89]:


len([letter for letter in fruit1 if letter in 'aeiou'])


# In[91]:


fruits_more_than_two = [fruit for fruit in fruits if len([letter for letter in fruit if letter in 'aeiou']) > 2 ]


# In[117]:


# Exercise 4 - make a variable named fruits_with_only_two_vowels. 
# The result should be ['mango', 'kiwi', 'strawberry']
fruits_more_than_two = [fruit for fruit in fruits if len([letter for letter in fruit if letter in 'aeiou']) > 2 ]


# In[36]:


# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruit_greater_than_5 = []
for fruit in fruits:
    if len(fruit) > 5:
        fruit_greater_than_5.append(fruit)
fruit_greater_than_5


# In[38]:


# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruit_is_5 = []
for fruit in fruits:
    if len(fruit) == 5:
        fruit_is_5.append(fruit)
fruit_is_5

[fruit for fruit in fruits if len(fruit)  == 5]


# In[92]:


# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruit_is_less_5 = []
for fruit in fruits:
    if len(fruit) <= 4:
        fruit_is_less_5.append(fruit)
fruit_is_less_5


# In[71]:


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc...
fruit_char =[len(fruits[0]),len(fruits[1]),len(fruits[2]),len(fruits[3]),len(fruits[4]),len(fruits[5])]
fruit_char


# In[97]:


fruit_char_1 = [len(fruit) for fruit in fruits]


# In[103]:


# Exercise 9 - Make a variable named fruits_with_letter_a that contains
#a list of only the fruits that contain the letter "a"

fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
fruits_with_letter_a


# In[77]:


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
even_numbers =[number for number in numbers if number % 2 == 0]
even_numbers


# In[78]:


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers =[number for number in numbers if number % 2 != 0]
odd_numbers


# In[105]:


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [num for num in numbers if num > 0]
positive_numbers


# In[106]:


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [num for num in numbers if num < 0]
negative_numbers


# In[108]:


[num if num > 0 else num * -1 for num in numbers] 


# In[109]:


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
[num for num in numbers if len(str(abs(num))) > 1]


# In[111]:


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
[num ** 2 for num in numbers]


# In[114]:


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
[num for num in numbers if (num < 0 and num % 2 != 0)]


# In[116]:


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
[num + 5 for num in numbers]


# In[ ]:


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
#*Hint* you may want to make or find a helper function 
# that determines if a given number is prime or not.


# In[132]:


if numbers > 1:
    for i in range(2, num):
        if (numbers % i) == 0:


# In[138]:


[num for num in numbers if num > 1]


# In[152]:


def is_prime(num):
    if type(num) != int:
        return False
    if num <= 0:
        return False
    if num == 1:
        return True
    if num >= 2:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True 


