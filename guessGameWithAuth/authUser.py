def authUser(userName,UserPassword):
    name=userName
    password=UserPassword
    with open('ex1.txt','r') as file:
        lines = file.read()
        words = lines.split()
        for i in range(len(words)):
            if words[i] == name and words[i+1] == password:
                print("Login successful")
                return True
    print("Login failed")
    exit(1)