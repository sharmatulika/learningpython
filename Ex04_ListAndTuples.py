print("Exercise for list and tuples")
months=('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
dob=input("please enter your birthday in dd-mm-yyyy format")
print(dob)
print(dob[3:5])
index=int(dob[3:5])-1
bdmonth=months[index]
print(" you were born in ",bdmonth)

name=input("enter your name")
names=["john","scott","marty"]
names.append(name)
print(names)


