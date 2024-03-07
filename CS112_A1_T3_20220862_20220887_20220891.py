#Program: Task 3 Assignment
#Author 1: Richard Remo Emmanuel soleved problem 1 and 4
#Author 2: Ajal Gai Deng Gai solved problem 2 and 5 
#Author 3: Sunday Pul Nyok solved problem 3 and 6
#version : 0.1 // it 0.1 coz it the collective of our rough work this is the upgrate of all problem in one file
#Date: 26/feb/2024


#Head section
print("welcom to the problem solver Program")
print("Date: 26/feb/2024")
print("Authors:", "Richard Remo", "Ajal Gai Deng Gai", "Sunday Pul Nyok")
print("IDS:", '20220862', '20220887', '20220891')
print("Solvers:", 'Richard Remo', 'Ajal Gai Deng Gai', 'Sunday Pul Nyok')


#menu loop
while True:
    print("\nMenu:")
    print("1. Problem.find your grade 1")
    print("2. Problem.check amstrong number 2")
    print("3. Problem.mathematical opration of pi 3")
    print("4. Problem.cesar cipher to convert and encrypt message 4")
    print("5. Problem.program function to check if  two list have same element 5")
    print("6. Problem.program to find factor pf positive integer 0 f 12 6")
    print("7. Exit ")

    choice = input("Entr your choice: ")

    if choice == '1':
        #solve first problem
        # Program to check you grade 

        mark = float(input("Enter the marks: "))

        if mark >= 90:
           print("grade: A+")
        elif mark  >= 85 :
           print("grade: A")
        elif mark >= 80:
           print("grade: B+")
        elif mark >= 75:
           print("grade: B")
        elif mark >= 65:
            print("grade: C+")
        elif mark >= 60:
            print("grade: C")
        elif mark >= 55:
            print("grade: D+")
        elif mark >= 50:
            print("grade: D")       
        else:
            print("grade: F")      

        print("Problem 1 is being solved by Richard Remo Emmanuel")
    elif choice == '2':
        #solve second problem
        #program to check if a given number is for Armtrong or not
        def arm_strong(num):
            num = str(num)
            sum = 0 
            for i in range(len(num)):
                cal = 1
                for j in range(len(num)):
                    cal *= int(num[i])
                sum += cal
            if str(sum) == num:
                return True
            else:
                return False
        while True:
            num = int(input("Enter the number here >>"))
            if num == 0:
                break
            else:
                print(arm_strong(num))           
        print("Problem 2 is solved by Ajal Gai Deng Gai")
    elif choice == '3':
        #solve third problem
        def calculate_pi(n):
            S = 0
            for i in range(n):
                S = S + 1 /((-1) ** i) / (2 * i + 1)
            pi = 4 * S
            return pi

        # Test the program for n = 10
        n = 10
        approx_pi = calculate_pi(n)
        print ( f"Approximation of pi for n = {n}: {approx_pi}")
        print("Problem 3 is solved by Sunday Pul Nyok") 
    elif choice == '4':
        #solve fourth problem
        #program that use Cesar cipher to convert and encrypt message
        def caesar_cipher(text, shift):
            encryted_text = ""
            for char in text:
                if (char.isalpha()): 
                    shifted = ord(char) + shift
                    if char.islower():
                       if shifted > ord('z'):
                           shifted -= 26
                       elif shifted < ord('a'):
                           shifted += 26
                    elif char.isupper():
                     if shifted > ord('Z'):  
                         shifted -= 26
                     elif shifted < ord('A'):
                           shifted += 26
                    encryted_text += chr(shifted)
                else:
                    encryted_text += char
            return encryted_text

        #input message from the user
        message = input("Enter a message to encrypt: ")
        #shift valu for caeer cipher
        shift_value = 1                                    
        #Encrypt message using caeser cipher
        encrypted_message = caesar_cipher(message, shift_value)
        print("Encrypted message: ", encrypted_message)
        print("Problem 4 is solved by Richard Remo Emmanuel")           
    elif choice == '5':
        #solve fifth problem
        #function to check two list if have same element
        def same_list(list1, list2):
            new_list1 =sorted(list1)
            new_list2 =sorted(list2)

            len_list1 = len(new_list1)
            len_list2 = len(new_list2)

            if len_list1 != len_list2:
                return False
            new_size = 0
            for i in range (0, len_list1):
                if new_list1[i] == new_list2[i]:
                    new_size += 1
                else:
                    pass
            if len_list1 != new_size:
                return False
            else:
                return True
        #initial of the two list integer    
        list1 = [4,5,6,7,8,1,9,0]
        list2 = [5,4,1,7,6,8,9,0]
        same = same_list(list1, list2)
        print(same)            
        print("Problem 5 is solved by Ajal Gai Deng Gai")
    elif choice == '6':
        #solve sixth problem
        #program to find all the factors of +ve integer of 12
        import math
        x = 12
        print (" factors of ", x , " is ")
        for  i in range(1, x+1):
            if x % i == 0:
                print (i)
        print("Problem 6 is solved by Sunday Pul Nyok")          
    elif choice == '7':
        #exting the progam
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option")    