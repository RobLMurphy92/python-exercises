# 1.) Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    if x == 2 or x == '2':
        return True
    return False
    
# 2.) Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[4]:


vowel = ['a','e','i','o','u','A','E','I','O','U']
def is_vowel(char):
    if char in vowel:
        return True
    return False

is_vowel('r')
is_vowel('y')
    


# In[224]:


def is_vowel(string):
    if type(string) == str:
        return string.lower() in ['a','e','i','o','u']
        return result
    else:
        return False


# 3.)Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[119]:


vowel = ['a','e','i','o','u','A','E','I','O','U']
def is_consonant(letter):
    if letter not in vowel and letter[0].isalpha() and len(letter) <= 1:
        return True
    return False
is_consonant('t')


# In[225]:


def is_consonant(char):
    if type(char) == str:
        is_only_letters = char.isalpha()
        return is_only_letters and not is_vowel(char)
    else:
        return False


# 4.) Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

# In[226]:



vowel = ['a','e','i','o','u','A','E','I','O','U']
def is_start_consonant(letter):
    letter = letter.lower()
    if letter.startswith(tuple(vowel)) and letter.isalpha():
        return letter.capitalize()
    else:
        return ('Not a word which starts with consonant')
is_start_consonant('5apples')


# In[227]:


def capital_starting_cons(char):
    if type(char) != str:
        return False
    
    first_lett = char[0]
    if is_start_consonant(first_letter):
        char = string.capitalize()
        
    return char


# 5.) Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[140]:


tip_precentage = 18/100
def calculate_tip(x):
    x = float(x)
    if x > 0:
        return x * tip_precentage
    
calculate_tip(12)
   


# In[229]:


def calc_tip_percentage(bill, tip_percentage = 0.2):
    if tip_percentage < 0 or tip_percentage >1:
        return 'Tip percentage is between 0 and 1'
    tip_amount = tip_percentage * bill
    return tip_amount


# 6.) Define a function named apply_discount. It should accept a original price, and a discount percentage, and
# #return the price after the discount is applied.
# 
# 
# 

# In[176]:



def apply_discount(start_price):
    if start_price > 0:
        discount = .18
        discount_price = (start_price * discount)
    return (round(discount_price,2))
apply_discount(10000.70)


# 7.) Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[199]:


def handle_commas(x):
       if x != x.isalpha():
           x = x.replace(',', '')
           return float(x)
handle_commas('1000,')     


# In[230]:


def handle_com(string):
    if type(string) != str:
        return 'Input must be a str'

    return float(string.replace(",", ""))


# 8.)Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[213]:


def get_letter_grade(x):
    if x < 60:
        return 'F'
    if x < 70:
        return 'D'
    elif x < 80:
        return 'C'
    elif x < 90:
        return 'B'
    elif x < 100:
        return 'A'
    
get_letter_grade(78)


# In[236]:


def letter_grade(x):
    if type(x) == int or type(x) == float:
        if x < 60:
            return 'F'
        elif x < 70:
            return 'D'
        elif x < 80:
            return 'C'
        elif x < 90:
            return 'B'
        elif x < 100:
            return 'A'


# 9.) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[12]:


# return words with vowels removed

vowel = ['a','e','i','o','u','A','E','I','O','U']

def remove_vowels(char):
    if type(char) != str:
        return False
    no_vowel = " "
    for letter in char:
        if not is_vowel(letter):
            no_vowel += letter
    return no_vowel


remove_vowels('hello')
            
    


# 10.) Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

# In[ ]:


# not python identifier, remove it
# remover whitespaces
#everything lowercase
# spaces become underscores


# In[48]:


def normalize_name(string):
    if type(string) != str:
        return False
    
    
    string = string.lower()
    
    
    output = " "
    output = output.strip()
    
    
    for char in string:
        if char.isidentifier() or char == " ":
            output += char
    output = output.replace(" ", "_")
    return output

normalize_name('%_not Completed')
    


# In[22]:




def string_test(char):
    if type(char) != str:
        return False
string_test('hello')
string_test(345) 


# In[42]:


old = ('Hello there')

new_string = old.replace(" ", "_")
new_string


# In[41]:


new_low = old.lower()
new_low


# In[35]:


#filter out white spaces
def no_white(x):
    for char in x:
        x.replace(" ","_")
        return x
no_white("hello there")


# 11.) Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[20]:


def cumulative_sum(x):
    new_x = list(x)
    for n in range(1, len(new_x)):
        new_x[n] += new_x[n-1]
    return new_x
cumulative_sum([1,2,5,7])