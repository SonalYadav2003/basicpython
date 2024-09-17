# print("sonal yadav")
# #to print your name using input
# name=input("enter your name")
# print(name)
# #find current age
# bornyear=input("enter your born year")
# currentyear=input("enter current year")
# ageinyear=int(currentyear)-int(bornyear)
# print(ageinyear)

# #wap for currency convertor
# print("convert rupee into dollars")
# rupeesAmount=int(input("enter the amount in rs"))
# rsintodollar=(rupeesAmount /84)
# print(rupeesAmount,"convert into dollar",rsintodollar)

#wap for currency convertor
# print("convert dollar into rupee")
# dollarAmount=int(input("enter the amount in dollar"))
# dollarintors=(dollarAmount * 84)
# print(rupeesAmount,"convert into dollar",dollarintors)

# #wap to check the user eligible for job
# #if gender is female and age is greater than 17
# #if gender is male  then they can apply for private job
# userage=int(input("enter the user age"))
# usergender=(input("enter your gender"))

# if (userage> 17 and usergender == "female"):
#     print("you are eligible for goverment job")
# elif( userage>17 and usergender == "male"):
#     print("you are eligible for private job")
# else:
#     print("you are not eligible for any job")

# #wap to check the greatest no
#  a=int(input("enter the value for a"))
#  b=int(input("enter the vale for b"))
#  c=int(input("enter the value for c"))
#  if(a > b  and a > c):
#      print("A is greatest")
#  elif(b > c and b > a):
#      print("B is greatst")
#  else:
#     print("C is greatest")

# #switch condition is the replacement of multiple if else block
# friendname=["walt","mehak","mike"]
# #to add the new friend name in list 
# friendname.append("sonal")
# #print after adding name
# print("After",friendname) 
# #to add the name in specific position
# friendname.insert(0,"harsh")
# #print after adding name at 0 index 
# print ("add name at index 0",friendname)
# #to remove the name from the list
# friendname.remove("harsh")
# #print after removing the name in the list 
# print(friendname)

# friendname.pop(1)
# print (friendname)

# #to sort the list
# friendname.sort()
# print (friendname)

#to print element in the list
#for name in friendname:
   # print(name)
# to print the number 1to 10

for no in range(1,12):
    print (no)

#to print the even no from 1 to 10 
for even in range(2,21,2):
    print (even)

for even in range(1,11):
 if even %2==0:
    print (even)

#tuple used to store the data and data is changeable
sets ={"pawan","ivan","anshu","ivan"  }
sets.add("harsh")
sets.remove("harsh")
print(sets) 
print (type (sets))

# friend={"sonal", "anika","sneha","deepika","honey"}
# print(friend)
# friend.sort()
# print (friend)

import datetime 
x= datetime.datetime.now()
print(x.month) 

import datetime 
x= datetime.datetime.now()
print(x) 



