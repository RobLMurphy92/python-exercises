### Exercise 1

### Identify the data type of the following values:

#99.9,Float


#"False",string


#False,boolean


#'0',string


#0, int


#True,boolean


#'True',string


#[{}],list


#{'a': []} dict


### Exercise 2

### What data type would best represent:


A term or phrase typed into a search box? string


If a user is logged in? boolean


A discount amount to apply to a user's shopping cart? float


Whether or not a coupon code is valid? boolean


An email address typed into a registration form? dictionary


The price of a product? float


A Matrix? int 


The email addresses collected from a registration form? list of strings, 


Information about applicants to Codeup's data science program? 
dictionaries

### Exercise 3


For each of the following code blocks, read the expression and predict what the result of evaluating it would be, then execute the expression in your Python REPL.


'1' + 2 error


6 % 4 remainder of 2


type(6 % 4) int


type(type(6 % 4)) type


'3 + 4 is ' + 3 + 4 error

0 < 0 false

'False' == False false

True == 'True' false

5 >= -5 true


True or "42" true


6 % 5 remainder 1


5 < 4 and 1 == 1 false


'codeup' == 'codeup' and 'codeup' == 'Codeup' false


4 >= 0 and 1 !== '1' error


6 % 3 == 0 true 


5 % 2 != 0 true 


[1] + 2 error


[1] + [2]     [1,2]


[1] * 2 [1,1]


[1] * [2] error cant mutiply sequence by non int.


[] + [] == [] true


{} + {}     unsupported operation


### Exercise data_types_and_variables

Create a Python script file named data_types_and_variables.py. Inside it, write some Python code, that is, variables and operators, to describe the following scenarios. Do not worry about the real operations to get the values, the goal of these exercises is to understand how real world conditions can be represented with code.

You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?


Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.


A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.


A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.

# 1.
#You have rented some movies for your kids: 
#The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and 
#Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, 
#how much will you have to pay?

price = 3.00
movie_1 = {
    "movie": "little mermaid",
    "rental_time": 3} # days
movie_2 = {
    "movie": "brother bear",
    "rental_time": 5} # days
movie_3 = {
    "movie": "hercules",
    "rental_time": 1} # days
payment = movie_1["rental_time"]* price + movie_2["rental_time"] * price + movie_3["rental_time"] * price

'${:,.2f}'.format(payment)



little_mermaid = 3
brother_bear = 5 
hercules = 1
price_per_day = 3

total_price = price_per_day * (little_mermaid + brother_bear+hercules)
total_price


#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
#they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
#How much will you receive in payment for this week? 
#You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.




google = {
    "pay": 400.00,
    "hours":6}
google_pay = google["pay"] * google["hours"]

facebook = {
    "pay": 350.00,
    "hours":10}
facebook_pay = facebook["pay"] * facebook["hours"]

amazon = {
    "pay": 380.00,
    "hours":4}
amazon_pay = amazon["pay"] * amazon["hours"]

total_compensation = amazon_pay + facebook_pay + google_pay

'${:,.2f}'.format(total_compensation)

#A student can be enrolled to a class 
#only if the class is not full and the class schedule #
#does not conflict with her current schedule.
# class cannot be full
# schedule cannot conflict    

class_is_full = False
schedule_conflict = False

enrollable_status = not(class_is_full or schedule_conflict)
enrollable_status

#A product offer can be applied only if people buys more than 2 items, 
#and the offer has not expired. 
#Premium members do not need to buy a specific amount of products.

more_than_two_items = True
offer_not_expired = True 
premium_membership = False
discount_elig = offer_not_expired and (more_than_two_items or premium_membership)
discount_elig

Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'


Create a variable that holds a boolean value for each of the following conditions:

the password must be at least 5 characters

the username must be no more than 20 characters

the password must not be the same as the username

bonus neither the username or password can start or end with whitespace

username = 'codeup' 
password = 'notastrongpassword'
pw_len_stuff = len(password) >= 5
user_char = len(username) < 21
not_match = username != password
user_no_whitespace = not username.startswith(' ') or username[-1]
pass_no_whitespace = not password.startswith(' ') or password[-1]

user_pw_valid = pw_len_stuff and user_char and not_match
user_pw_valid

fake_user = " hire this is  kfahdjgkhfgkihfgijhfdihdiuvh"

fake_user[-1] == " "
username.startswith('code')