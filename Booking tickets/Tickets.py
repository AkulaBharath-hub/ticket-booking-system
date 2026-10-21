def Famliy(Gender):
  
    select=int(input("Select Your Seats: "))
    print("Your Seats Numbers Are: ")
    for i in range(1,select+1):
        print(i)
    print("HAPPY JOURNEY!!!!!!!!!!")

        


def Individual1(Gender):
   
         select=int(input("Select Your Seats: "))
         print("Your Seats Numbers Are: ")
         for i in range(21,21+select):
                print(i)
         print("HAPPY JOURNEY!!!!!!!!!!")

def Individual2(Gender):
    
         select=int(input("Select Your Seats: "))
         print("Your Seats Numbers Are: ")
         for i in range(41,41+select):
                print(i)
         print("HAPPY JOURNEY!!!!!!!!!!")

         

while True:
    Name=input("Enter Your Name: ")
    Age=int(input("Enter Your Age: "))
    print("!________________________Welcome To My Tickets________________________!")
    print("______________________________________________________________________")
    print("")
    print("1.Family Booking")
    print("")
    print("2.Individual Booking")
    print("______________________________________________________________________")

    choice=int(input("Enter Your Choice: "))

    if choice==1:
        Famliy(Gender=input("Enter Your Gender: "))
        break
    elif choice==2:
         Gender=input("Enter Your Gender: ")
         if Gender.lower()=="male":
              Individual1(Gender)
              break
         elif Gender.lower()=="female":
              Individual2(Gender)
         else:
              print("Wrong Selection")
    

       

    else:
         print("Wrong Choice")

