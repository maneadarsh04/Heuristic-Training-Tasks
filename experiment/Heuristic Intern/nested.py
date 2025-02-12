print("Good Morning!! Welcome to Indala College of Engineering")

Name = str(input("What is your name??\n"))    

print("What would you like to participate??")

print("1. Music & Dance Perfomance")
print("2. Face Painting & Reel Making")
print("3. Sports & Games")

Event= int(input())

if Event==1:
  Age= int(input("What is your age??\n"))
  if Age<=20:
    print(f"Your age is {Age} years.\nGo to Room 01.")
  elif Age>=20:
       print(f"Your age is {Age} years.\nGo to Room 02.")


elif Event==2:
  Age=int(input("What is your age??\n"))
  if Age<=15:
    print(f"Your age is {Age} years.\nGo to Room 03.")
  elif Age>=15:
      print(f"Your age is {Age} years.\n Go to Room 04.")
elif Event==3:
  Age=int(input("What is your age??\n"))
  if Age<=20:
    print(f"Your age is {Age} years.\nGo to Ground 01.")
  elif Age>=20:
    print(f"Your age is {Age} years.\nGo to Ground 02.")
   
else:
    print("You can go to Office Room for Guidance")

print("Thank you for visting!!")
