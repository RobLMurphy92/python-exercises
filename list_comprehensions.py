{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unindent does not match any outer indentation level (<tokenize>, line 20)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<tokenize>\"\u001b[0;36m, line \u001b[0;32m20\u001b[0m\n\u001b[0;31m    'KIWI', etc...]\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unindent does not match any outer indentation level\n"
     ]
    }
   ],
   "source": [
    "# 17 list comprehension problems in python\n",
    "\n",
    "fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']\n",
    "\n",
    "numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]\n",
    "\n",
    "# Example for loop solution to add 1 to each number in the list\n",
    "numbers_plus_one = []\n",
    "for number in numbers:\n",
    "    numbers_plus_one.append(number + 1)\n",
    "\n",
    "# Example of using a list comprehension to create a list of the numbers plus one.\n",
    "numbers_plus_one = [number + 1 for number in numbers]\n",
    "numbers_plus_one\n",
    "# Example code that creates a list of all of the list of strings in fruits and uppercases every string\n",
    "output = []\n",
    "for fruit in fruits:\n",
    "    output.append(fruit.upper())\n",
    "    \n",
    " 'KIWI', etc...]\n",
    "\n",
    "\n",
    "\n",
    "# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.\n",
    "\n",
    "# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']\n",
    "\n",
    "# Exercise 5 - make a list that contains each fruit with more than 5 characters\n",
    "\n",
    "# Exercise 6 - make a list that contains each fruit with exactly 5 characters\n",
    "\n",
    "# Exercise 7 - Make a list that contains fruits that have less than 5 characters\n",
    "\n",
    "# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]\n",
    "\n",
    "# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter \"a\"\n",
    "\n",
    "# Exercise 10 - Make a variable named even_numbers that holds only the even numbers \n",
    "\n",
    "# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers\n",
    "\n",
    "# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers\n",
    "\n",
    "# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers\n",
    "\n",
    "# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals\n",
    "\n",
    "# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]\n",
    "\n",
    "# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.\n",
    "\n",
    "# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. \n",
    "\n",
    "# BONUS Make a variable named \"primes\" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['MANGO', 'KIWI', 'STRAWBERRY', 'GUAVA', 'PINEAPPLE', 'MANDARIN ORANGE']"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 1 - rewrite the above example code using list comprehension syntax. \n",
    "# Make a variable named uppercased_fruits to hold the output of the list comprehension. \n",
    "# Output should be ['MANGO', 'KIWI', etc...]\n",
    "\n",
    "fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']\n",
    "\n",
    "uppercased_fruits = [x.upper() for x in fruits] # stated uppercase variable for variable in list.\n",
    "\n",
    "uppercased_fruits\n",
    "  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Mango', 'Kiwi', 'Strawberry', 'Guava', 'Pineapple', 'Mandarin Orange']"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]\n",
    "capitalized_fruits = [x.title() for x in fruits]\n",
    "capitalized_fruits"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 112,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 112,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. \n",
    "# Hint: You'll need a way to check if something is a vowel.\n",
    "vowels = 'a' or 'e' or 'i' or 'o' or 'u'\n",
    "fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']\n",
    "\n",
    "fruits_with_more_than_two_vowels = [x for x in fruits if vowels.count('aeiou') > 2]\n",
    "\n",
    "\n",
    "\n",
    "fruits_with_more_than_two_vowels\n",
    "    \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Exercise 4 - make a variable named fruits_with_only_two_vowels. \n",
    "# The result should be ['mango', 'kiwi', 'strawberry']`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['strawberry', 'pineapple', 'mandarin orange']"
      ]
     },
     "execution_count": 102,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 5 - make a list that contains each fruit with more than 5 characters\n",
    "fruit_greater_5 = []\n",
    "for fruit in fruits:\n",
    "    if len(fruit) > 5:\n",
    "        fruit_greater_5.append(fruit)\n",
    "    \n",
    "fruit_greater_5"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
