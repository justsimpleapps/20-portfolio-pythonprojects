# this code checks wether the email entered is valid or not using string functions
# the smallest email is g@g.in i.e. 6 chars
# here we have used multiple nested if-else statements so that we can check in which parameter did the email was not valid


email = input("Enter your email: ")
k,j ,d = 0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") or (email[-3] == "."):
                for i in email:
                    if i==" ":
                        k=1
                    elif i==i.isalpha():
                        if i == i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i== "@":
                        continue
                    else:
                        #d=1
                        continue
                if k == 1:
                    print("Wrong Email! 5")
                elif j==1:
                    print("Wrong Email! 6")
                elif d ==1:
                    print("Wrong Email! 7")
                else:
                    print("Right Email!")
            else:
                print("Wrong Email! 4")
        else:
            print("Wrong Email! 3")
    else:
        print("Wrong Email! 2")
else:
    print("Wrong Email! 1")    