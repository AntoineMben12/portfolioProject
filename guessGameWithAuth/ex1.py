import random
import authUser

print("1)-Start")
print("2)-Exit")                                                                           #guessing-games-py-program
points=int(100)
att=int(0)


choose = input("Enter a choice :")
if( choose == "1"):
    print("1)-Login")
    print("2)-Registration:) if you don't have an account")
    choice=input("Enter a choice: ")
    if( choice=="1"):
        userName = input("Enter your name: ")
        UserPassword = input("Enter your password: ")
        authUser.authUser(userName,UserPassword)
        rand = int(random.random()*100)
        val = int(input("Guess the entered value : "))
        while(val != rand):
            att=att+1
            val = int(input("Guess the entered value : "))
            if( val < rand):
                print("The value is greater.")
            elif( val > rand):
                print("The value is smaller.")
            elif( val == " "):
                val = int(input("Guess the entered value : "))
            else:
                print("Congratulation you won")
                score=points-(att*5)
                print(f"score: {score}/100")
                print(f"attempts: {att}")
                text1 = f"Game1: \n score: {score}\n attempts: {att} \n\n"
                with open('ex1.txt','a') as file:
                    file.write(text1)
    else:
        userName = input("Enter your name: ")
        UserPassword = input("Enter your password: ")
        text2 = f"{userName}\n{UserPassword}\n\n"
        safe_name = userName.replace(" ", "_")
        filename = f"user_{safe_name}.txt"
        with open(filename,'w') as file:
            file.write(text2)
        print("Registration successful")
else:
    exit(1)