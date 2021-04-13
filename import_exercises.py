#1.) Import and test 3 of the functions from your functions exercise file. Import each function in a different way:

# a.) Run an interactive python session and import the module. Call the is_vowel function using the . syntax.

#In [1]: import function_exercises

#In [2]: function_exercises.is_vowel('b')
#Out[2]: False

#In [3]: 

# B.) Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
# from function_exercises import calculate_tip

#In [5]: calculate_tip(100)
#Out[5]: 18.0


#c.)Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.
#from function_exercises import calculate_tip

#In [5]: calculate_tip(100)
#Out[5]: 18.0

#2.) Read about and use the itertools module from the python standard library to help you solve the following problems:

# 2.a)How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
alpha = ['a', 'b', 'c']
numb = [1,2,3]


def combine_lt_numb(alpha, numb):
    return len(list(itertools.product(alpha, numb)))


    
        
  
combine_lt_numb(alpha, numb)
print(list(itertools.product(alpha, numb)),len(list(itertools.product(alpha, numb))) )


# 2.b) How many different combinations are there of 2 letters from "abcd"?
alpha = ['a', 'b', 'c','d']

combo = list(itertools.combinations(alpha, 2))

combo
# How many different permutations are there of 2 letters from "abcd"?
alpha = ['a', 'b', 'c','d']

permu = list(itertools.permutations(alpha, 2))

permu