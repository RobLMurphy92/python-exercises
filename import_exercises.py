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

from function_exercises import get_letter_grade as glg

glg(16)
# F

#In [5]: calculate_tip(100)
#Out[5]: 18.0

#2.) Read about and use the itertools module from the python standard library to help you solve the following problems:
import itertools 
# 2.a)How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
alpha = ['a', 'b', 'c']
numb = [1,2,3]


def combine_lt_numb(alpha, numb):
    return len(list(itertools.product(alpha, numb)))


 len(list(itertools.product('abc', '123')))   
        
  
combine_lt_numb(alpha, numb)
print(list(itertools.product(alpha, numb)),len(list(itertools.product(alpha, numb))) )


# 2.b) How many different combinations are there of 2 letters from "abcd"?
alpha = ['a', 'b', 'c','d']

combo = list(itertools.combinations(alpha, 2))

len(list(itertools.combinations('abcd', 2)))


combo
# How many different permutations are there of 2 letters from "abcd"?
alpha = ['a', 'b', 'c','d']

permu = list(itertools.permutations(alpha, 2))

permu

#3.)Save this file as profiles.json inside of your exercises directory (right click -> save file as...).
#Use the load function from the json module to open this file.
#Use the load function from the json module to open this file.
import json
json.load(open('profiles.json')

#Total number of users
#Number of active users
#Number of inactive users
#Grand total of balances for all users
#Average balance per user
#User with the lowest balance
#User with the highest balance
#Most common favorite fruit
#Least most common favorite fruit
#Total number of unread messages for all users




#total number of users

len(profiles)



# count of users who are active
count = 0
for profile in profiles:
    if profile['isActive'] == True:
        count +=1
print(count)


# Number of inactive users
count = 0
for profile in profiles:
    if profile['isActive'] == False:
        count +=1
print(count)
# madeline method
inactive_users = []
for accnt in profiles:
    if not accnt['isActive']:
        inactive_users.append(accnt)
        
inactive_users

# Grand total of balances for all users
balances = float(profile['balance'].replace(',', '').replace('$', ''))
balances

count = 0
for profile in profiles:
    profile_balance = float(profile['balance'].replace(',', '').replace('$', ''))
    count += profile_balance
print(count)

#madeline method
bal_list = []
for accnt in profiles:
    bal_list.append(float(accnt['balance'][1:].replace(',','')))
sum(bal_list) # with lists we dont have to add all through!!


# Average balance per user
count = 0
for profile in profiles:
    profile_balance = float(profile['balance'].replace(',', '').replace('$', ''))
    count += profile_balance
average = count/len(profiles)
round(average, 2)



#User with the lowest balance
min_user = {}
for accnt in profiles:
    if float(accnt['balance'][1:].replace(',','')) == min(bal_list):
        min_user = accnt
    
        
min_user['name']


# User with the highest balance
max_user = []
for accnt in profiles:
    bal_list_2.append(float(accnt['balance'][1:].replace(',','')))
min(bal_list) # with lists we dont have to add all through!!
print(max(bal_list))

# Most common favorite fruit
fruit_list = [accnt['favoriteFruit'] for accnt in profiles]

fruit_counts = {}
for fruit in fruit_list:
    if fruit not in fruit_counts.keys():
        fruit_counts[fruit] = 1
    else:
        fruit_counts[fruit] += fruit_counts[fruit] + 1
        
fruit_counts


#madeline method
fruitcount_dict = fruit_counts(all_fruits)
fave_fruit = [fruit for fruit in fruitcount_dict \
    if fruitcount_dict[fruit] == max(fruitcount_dict.values())][0]
print(f'Most popular fruit: {fave_fruit}')


# Least most common favorite fruit
fruit_list = [accnt['favoriteFruit'] for accnt in profiles]

fruit_counts = {}
for fruit in fruit_list:
    if fruit not in fruit_counts.keys():
        fruit_counts[fruit] = 1
    else:
        fruit_counts[fruit] += 1

fruit_counts

#madeline method
least_fave_fruit = ''
for k, v in fruitcount_dict.items():
    if v == min(fruitcount_dict.values()):
        print('least favorite fruit: ',k)

#Total number of unread messages for all users
#madeline method
list_comp_all_unreads = sum([int(''.join([val for val in accnt['greeting'] if val.isdigit()])) for accnt in profiles])
# 
# breaking it down:
# 
# single greeting value:
profiles[0]['greeting']
# pulling out the digits from that greeting into a list:
digit_list = []
for letter in profiles[0]['greeting']:
    if letter.isdigit():
        digit_list.append(letter)
# this gives us a digit list that looks like ['4'] or like ['1','9'] -- we want a single int.
# to join the list, we use the join string method
digit_as_string = ''.join(digit_list)
# finally we want to cast it to an integer data type
digit = int(digit_as_string)
# Now, we want to do this for every account in the profile
list_of_unread_messages = []
for accnt in profiles:
    # do everything we just did for every dictionary referenced here as accnt
    digit_list = []
    for letter in accnt['greeting']:
        if letter.isdigit():
            digit_list.append(letter)
    digit_as_string = ''.join(digit_list)
    digit = int(digit_as_string)
