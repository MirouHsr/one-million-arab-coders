# lesson 5: variables & strings

#we can use variable to define something like an int number or string or array 
#syntax: var_name = expression ..
age = 23
days_of_year = 365.25
hours_of_sleep = 7
age_in_days = age * days_of_year
sleep_hours_in_life = age_in_days * hours_of_sleep
awake_hours_in_life = (age_in_days * 24) - sleep_hours_in_life
print  age_in_days
print  sleep_hours_in_life / 24
print  awake_hours_in_life / 24

# name of variable can't be separated by spaces like (age in day)..
# a string is a type of variable ==> it means a series of Character ..
last_name = 'Hasrane '  # between '...' 
# OR
first_name = "Amir "    # between "..." 
# both are right 
print "Hello " + first_name + last_name + '!' * 3
# as you see we can add to strings by the plus operator (+).. and we call that "String concatenation" ....
# We can even multiply a string by a integer number for avoiding repeatation....

# This code shows the difference between the string "4" and the number 4.
# Remove the four comment characters (#) on the lines below to see what happens.
print 4
print "4"
print 4 + 4
print "4" + "4"

# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.

s = 'audacityda'
# answer is :
print 'U' + s[2:]

# This segment is just a chance for you to play around with 
# finding strings within strings. Read through the code and 
# press Test Run to see what it does. Is there anything 
# interesting or unexpected?

print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string