file = None
#here we create a empty var called file

try:
    user = int(input("enter a number: "))
    result = 100 / user
    file = open("log.txt", "w")
    file.write(str(result))

    # in this block we get the user input as int 
    # then we use the pre defiend file var and create a log.text text file and open it in write mode 
    # and we use file.write to write the output(result) as str in the file("log.txt")


except ValueError:
    print("enter a valid number")
except ZeroDivisionError:
    print("number cannot be zero")
except FileNotFoundError:
    print("file error")

       #here we handled some error
       # i didnt use Exception here because it hides what had went wrong 

       
else:
       
    print("done!")
    #and here we printed done(this only happens when the try block was succesful)

finally:
    if file:
        file.close()
    print("the program is finished")
    #this part we close the file and print the message above(this part runs anyway) 