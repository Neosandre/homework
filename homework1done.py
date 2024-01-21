#!/usr/bin/env python
# coding: utf-8

# To complete the homework simply fill in your answers in this jupyter notebook!
# 
# Remember that there are many ways in which markup cells can be used and you can add useful things such as references and images to better explain your answers.
# 
# It is perfectly fine if you copy your answer from somewhere else in the internet as long as you understand the code you copied and cite the source. However, refrain from asking help for your colleagues (unless you're really struggling) as the ability to find information online is crucial for any tech role you might want to have in the future.
# 
# <h1> Question 1: Multiple prints</h1>
# Create 3 different variables of different types and print their values using a single print statement.

# In[3]:


Name="Student"
age= 70
height = 6.4

print(Name +" "+ str(age)+" " + str(height))


# <h1> Question 2: Data structures</h1>
# Create two variables containing each a nested list and a nested dictionary and demonstrate how to access specific items of it.

# In[74]:


fruitList=["mango","apple","banana"]

colorsValue = {"Black":1, "yellow":2, "white":3}

print(fruitList[0])
print(fruitList[-1])
print(colorsValue["Black"])
print(colorsValue.values())
for key,value in colorsValue.items():
     print(value)


# Now consider the following list,

# 1 - slice this list (by index) to contain only the numbers smaller than 5; <br>
# 2 - make a loop to create a new list containing only the EVEN numbers of this list (bonus point if you use a list comprehension!!);<br>
# 3 - make a loop to create a new list containing only the numbers that are multiples of 3;<br>
# Bonus - make a loop that will print every item on the list inside a sentence using a f-string.

# In[72]:


a_list = [1,2,3,4,5,6,7,8,9]


# In[75]:


#1 - slice this list (by index) to contain only the numbers smaller than 5;
print(a_list[0:5])


# In[116]:


#2 - make a loop to create a new list containing only the EVEN numbers of this list (bonus point if you use a list comprehension!!);
even_numbers=[]
for i in a_list:
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)


## BONUS list comprehension##
new_list=[i for i in a_list if i % 2==0 ]
print(new_list)


# In[118]:


#3 - make a loop to create a new list containing only the numbers that are multiples of 3;
new_list =[i for i in a_list if i %3==0]


print(new_list)


# <h1>Question 3: Creating functions</h1>
# 
# Create a function that takes a list of numbers and convert them into strings. (bonus point if you use a list comprehension!!)

# In[126]:


the_list=[1,2,3,4,5,6,7,8,9]
def numberToString(the_list):
    another_list = []
    
    """this function converts numbers to String"""
    
    for item in the_list:    
        converted_item = str(item)
        another_list.append(converted_item)
        
    return(another_list)
numberToString(the_list)


# In[123]:


my_list = [1,2,3,4,5]

numberToString(the_list=my_list)


# In[124]:


new_list = [str(number) for number in my_list]
new_list


# In[125]:


new_list = [str(number) for number in range(10)]
new_list


# Create a small calculator. The function should pick two numbers and perform one of four mathematical operations with it (sum/subtraction, division, multiplication, exponents). The desired operation should be an option (hint: what IF the user wants to do a sum?)
# 
# Bonus: Make a function that can pick ANY number of numbers.

# In[46]:


num1=int(input("enter num 1: "))
operator=str(input("enter operator: "))
num2=int(input("enter num 2: "))

def calculator (num1,operator, num2):
    
    """this function calculates two numbers based on the operator input"""
    
        if operator == "+":
            print(num1 + num2)
        elif operator == "-":
            print(num1 - num2)
        elif operator == "*":
            print(num1 * num2)
        elif operator == "/":
            print(num1 / num2)
        elif operator == "**":
            print(num1 ** num2)
        
         

calculator(num1,operator,num2)


# Create a function that check if a number is within a list of numbers.

# In[131]:


checklist = [1,2,3,4,5]
n=int(input("enter number: "))

def checknum (n):
    
    """check if input number exist in list"""
    
    if n in checklist:
            print("number is in the list")
    else:
            print("number is NOT in the list")
checknum(n)


# Bonus: similar to the item above, create a function that checks if a string contains a given substring, e.g. 'I have a cat' contains the string sequence 'cat' or 'ave'.

# In[132]:


sentence="I am leaning python"
input_string=str(input("enter string: "))

def check_string(input_string,sentence):
    """check input exists in string"""
    if input_string in sentence:
        print("true")
    else:
        print("false")

check_string(input_string,sentence)


# Bonus: create a function that given the initial speed of a projectile that is thrown at 90 degrees will calculate how much time the projectile will take to get back to the initial altitude. (yes you're expected to disregard air resistence)

# In[ ]:





# <h1>solve these questions...or ELSE</h1>
# 
# Why the nested if statement below doesn't only produce the first print? Can you modify it so it produces the desired output?

# In[133]:


food = 'Pizza'
drinks = 'Beer'

if food == 'Pizza' and drinks == 'Beer':
    print('Yeeeey!')
elif food == 'Pizza' and drinks != 'Beer':
    print('Yey.')
elif food != 'Pizza' and drinks == 'Beer':
    print('Yey!')
else:
    print('.....???')


# <h1> Debugging </h1>
# None of the blocks of code below work. Your task is to make them work (if possible!) and add markup cells (or comments) explaining why they don't work.

# print("Is this working?")

# In[138]:


#this is a cooment so it will be ignore and it won print
print("does this work?")


# In[137]:


#you cannot use double and single quotes together
print("about now?")


# In[136]:


#you have to convert int to string and add the + sign to concatinate both variables

text_variable = "Today on a scale from 1 to 10 I am feeling..."
my_mood = 10
print(text_variable + str(my_mood))


# In[139]:


#convert int var to string before concatinate with a str var
text_variable = "Today on a scale from 1 to 10 I am feeling..."
my_mood = 10
print(text_variable+str(my_mood)) #Yep there are ways to make it work with a + operator too!


# In[141]:


#both keys and values have to be inside quotes as a str
a_dictionary = {"item1": 'Value 1',
                "item2": 'value 2',}


# In[142]:


# use double equal sign for comparison 
1 == 1 # Should return True


# In[144]:


# Why isn't the outcome 'Clap your hands?'
#comparisons are case sensitive so use capital H
mood = 'Happy'
if mood == 'Happy':
    print('Clap your hands')
else:
    print('...do I look like I have this one figured out?')


# In[146]:


#identation print has to be inside function
def printerfunction(x,y):
    print(x,y)

printerfunction("a word", "another word")


# In[150]:


# bonus/annoying round, why is this crashing?
#comparisons are case sensitive so use capital H & Identataion so print have to be inside if statement
mood = 'Happy'
if mood == 'Happy':s
    print('Clap your hands')
else:
    print('...do I look like I have this one figured out?')

