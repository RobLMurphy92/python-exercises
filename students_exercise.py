#!/usr/bin/env python
# coding: utf-8

# # 20 Python Data Structure Manipulation Exercises
# 
# The following questions reference the `students` data structure below. Write
# the python code to answer the following questions:
# 
# 1. How many students are there?
# 1. How many students prefer light coffee? For each type of coffee roast?
# 1. How many types of each pet are there?
# 1. How many grades does each student have? Do they all have the same number of
# grades?
# 1. What is each student's grade average?
# 1. How many pets does each student have?
# 1. How many students are in web development? data science?
# 1. What is the average number of pets for students in web development?
# 1. What is the average pet age for students in data science?
# 1. What is most frequent coffee preference for data science students?
# 1. What is the least frequent coffee preference for web development students?
# 1. What is the average grade for students with at least 2 pets?
# 1. How many students have 3 pets?
# 1. What is the average grade for students with 0 pets?
# 1. What is the average grade for web development students? data science
# students?
# 1. What is the average grade range (i.e. highest grade - lowest grade) for
# dark coffee drinkers?
# 1. What is the average number of pets for medium coffee drinkers?
# 1. What is the most common type of pet for web development students?
# 1. What is the average name length?
# 1. What is the highest pet age for light coffee drinkers?

# In[ ]:


#1.) How many students are there? ANSWER IS 14


# In[74]:


# need to find the number of students, can get number of elements in a list using len
number_of_students = len(students)
number_of_students


# In[526]:


student1 = students[0]
student1


# In[342]:


# 2.) #How many students prefer light coffee? For each type of coffee roast?
# need to know # of light cofee
# need to get outcome, answer is 3

coffee_light = sum(value == 'light' for value in student.values())


prefer_coffee_light = [student for student in students if sum(value == 'light' for value in student.values())]
print(len(prefer_coffee_light))


# In[592]:


count = 0
for student in students:
    if student["coffee_preference"] == "light":
        count += 1
    else:
        continue
print(f' There is a total of {count} light coffee drinkers!')


# In[593]:


for student in students:
    if student['coffee_preference'] == 'light':
        light_coffee_drinkers.append(student)
    else:
        continue
print(len(light_coffee_drinkers))


# In[643]:


for student in students:
    print(student)


# In[650]:


pets = student['pets']


# In[647]:


for species in pets:
    print(species)


# In[651]:


pet_species = species['species']
print(pet_species)


# In[700]:


#3.) How many types of each pet are there? Looking at students I know there is 3. Cats, dogs, horse
# I want to find the total number for each species.
# students is a list of dictionaries

horses = []
dogs = []
cats =[]
for student in students:
    pets = student['pets']
    for species in pets:
        pet_species = species['species']
        if pet_species == 'horse':
            horses.append(pet_species)
        if pet_species == 'dog':
            dogs.append(pet_species)
        if pet_species == 'cat':
            cats.append(pet_species)
            
        
print((f'Number of horses: {len(horses)}'))
print((f'Number of dogs: {len(dogs)}'))
print((f'Number of catss: {len(cats)}'))


            


# In[162]:


#.4 ) How many grades does each student have? Do they all have the same number of grade

student1 = students[0]
student1 = student1.get('grades')
student1 = len(student1)
print(student1)

student2 = students[1]
student2 = student2.get('grades')
student2 = len(student2)
print(student2)


student3 = students[2]
student3 = student3.get('grades')
student3 = len(student3)
print(student3)

student4 = students[3]
student4 = student4.get('grades')
student4 = len(student4)
print(student4)

student5 = students[4]
student5 = student5.get('grades')
student5 = len(student5)
print(student5)

student6 = students[5]
student6 = student6.get('grades')
student6 = len(student6)
print(student6)

student7 = students[6]
student7 = student7.get('grades')
student7 = len(student7)
print(student7)

student8 = students[7]
student8 = student8.get('grades')
student8 = len(student8)
print(student8)

student9 = students[8]
student9 = student9.get('grades')
student9 = len(student9)
print(student9)

student10 = students[9]
student10 = student10.get('grades')
student10 = len(student10)
print(student10)

student11 = students[10]
student11 = student11.get('grades')
student11 = len(student11)
print(student11)

student12 = students[11]
student12 = student12.get('grades')
student12 = len(student12)
print(student12)

student13 = students[12]
student13 = student13.get('grades')
student13 = len(student13)
print(student13)

student14 = students[13]
student14 = student14.get('grades')
student14 = len(student14)
print(student14)


# In[642]:


grade = 'grades'


# In[ ]:





# In[ ]:


for student in students:
    if student['coffee_preference'] == 'light':
        light_coffee_drinkers.append(student)
    else:
        continue
print(len(light_coffee_drinkers))


# In[169]:


#5.) What is each student's grade average?

student1 = students[0]
student1 = student1.get('grades')
student1 = sum(student1) / len(student1)
print(student1)

student2 = students[1]
student2 = student2.get('grades')
student2 = sum(student2) / len(student2)
print(student2)


student3 = students[2]
student3 = student3.get('grades')
student3 = sum(student3) / len(student3)
print(student3)

student4 = students[3]
student4 = student4.get('grades')
student4 = sum(student4) / len(student4)
print(student4)

student5 = students[4]
student5 = student5.get('grades')
student5 = sum(student5) / len(student5)
print(student5)

student6 = students[5]
student6 = student6.get('grades')
student6 = sum(student6) / len(student6)
print(student6)

student7 = students[6]
student7 = student7.get('grades')
student7 = sum(student7) /len(student7)
print(student7)

student8 = students[7]
student8 = student8.get('grades')
student8 = sum(student8)/ len(student8)
print(student8)

student9 = students[8]
student9 = student9.get('grades')
student9 = sum(student9)/len(student9)
print(student9)

student10 = students[9]
student10 = student10.get('grades')
student10 = sum(student10)/len(student10)
print(student10)

student11 = students[10]
student11 = student11.get('grades')
student11 = sum(student11)/len(student11)
print(student11)

student12 = students[11]
student12 = student12.get('grades')
student12 = sum(student12)/len(student12)
print(student12)

student13 = students[12]
student13 = student13.get('grades')
student13 = sum(student13) / len(student13)
print(student13)

student14 = students[13]
student14 = student14.get('grades')
student14 = sum(student14)/len(student14)
print(student14)


# In[ ]:


#6.) How many pets does each student have?

student1 = students[0]
student1 = student1.get('grades')
student1 = sum(student1) / len(student1)
print(student1)

student2 = students[1]
student2 = student2.get('grades')
student2 = sum(student2) / len(student2)
print(student2)


student3 = students[2]
student3 = student3.get('grades')
student3 = sum(student3) / len(student3)
print(student3)

student4 = students[3]
student4 = student4.get('grades')
student4 = sum(student4) / len(student4)
print(student4)

student5 = students[4]
student5 = student5.get('grades')
student5 = sum(student5) / len(student5)
print(student5)

student6 = students[5]
student6 = student6.get('grades')
student6 = sum(student6) / len(student6)
print(student6)

student7 = students[6]
student7 = student7.get('grades')
student7 = sum(student7) /len(student7)
print(student7)

student8 = students[7]
student8 = student8.get('grades')
student8 = sum(student8)/ len(student8)
print(student8)

student9 = students[8]
student9 = student9.get('grades')
student9 = sum(student9)/len(student9)
print(student9)

student10 = students[9]
student10 = student10.get('grades')
student10 = sum(student10)/len(student10)
print(student10)

student11 = students[10]
student11 = student11.get('grades')
student11 = sum(student11)/len(student11)
print(student11)

student12 = students[11]
student12 = student12.get('grades')
student12 = sum(student12)/len(student12)
print(student12)

student13 = students[12]
student13 = student13.get('grades')
student13 = sum(student13) / len(student13)
print(student13)

student14 = students[13]
student14 = student14.get('grades')
student14 = sum(student14)/len(student14)
print(student14)


# In[ ]:


# 7.) How many students are in web development? data science?


# In[ ]:


#8.)What is the average number of pets for students in web development?


# In[ ]:


#9.) What is the average pet age for students in data science?


# In[432]:


student1 = students[0]
pets = student1['pets']
species = pets[0]




student2 = students[0]


# In[395]:


students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

