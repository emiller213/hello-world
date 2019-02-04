def collectinfo():
    global FirstName
    global LastName
    global age
    FirstName = input("Enter your First Name: ")
    LastName = input("Enter your Last Name: ")
      
    
def printresponse():
    print("Hello, " + FirstName + " " + LastName + "!")
    print("You are " + age + " years old!")



collectinfo()
printresponse()
