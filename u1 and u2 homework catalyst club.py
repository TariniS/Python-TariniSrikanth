"""
Ask for the first and last names
Ask for age
If they are in the age group, tell them they are a teen..., as if they did not know th
 -------------------------------------------
"""
fname=input("What is your first name ")
lname=input("How about your Last name ")
print(" Hello " , fname,lname, "nice to meet you")
age = input( " How old are you ")


if ( int(age) <= 12 ):
    print( " Wow!,your young" )
else:
    print ("You are older than me")
