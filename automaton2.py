import random

#Marcus Nash
#CSCI-486: Theory of Computing
#Dr. Fatima Boukari
#04/30/2019

def accept_or_reject(string):
   file = open("Results.txt", 'a')
   state = "q1"
   stack = ['$']
   for i in string:
       print("i in string "+i)
       if state == 'q1':
           stack.append(i)
           state = 'q2'
       elif state == 'q2' and i == 'a':
           stack.append(i)
       elif state == 'q2' and i =='b' :
           stack.pop()
       elif state == 'q2' and i =='a':
           print("rejected")
           return "rejected"+"\n"+"=================="+"\n"
           break
       elif (len(stack) == 1) and i =='c':
           stack.append(i)
           state = 'q3'
       elif state == 'q3' and i == 'c':
           stack.append(i)
       elif state == 'q3' and i == 'a':
           print("rejected")
           return "rejected"+"\n"+"=================="+"\n"
           break
       elif state == 'q3' and i == '\n':
           print("Approved")
           return "Approved"+"\n"+"=================="+"\n"
           break
       else:
           print('rejected')
           return "rejected"+"\n"+"=================="+"\n"
           break



def accept_or_reject2(string):
   #file = open("Results.txt",'a')
   str1 = string
   state = "q1"
   stack = ['$']
   #print(" ---------------- i in string "+string)
   #print(string)
   string = string[:-1] 
    
   rString = string[::-1]+"\n"

   #print(" ---------------- i in String "+rString)

   for i in rString:
       #print("i in rString "+i)
       if state == 'q1':
           stack.append(i)
           state = 'q2'
       elif state == 'q2' and i == 'c':
           stack.append(i)
       elif state == 'q2' and i =='b' and len(stack)!=0:
           stack.pop()
       elif state == 'q2' and i =='c':
           print("rejected")
           return "rejected"+"\n"+"=================="+"\n"
           break
        
       elif (len(stack) == 1) and i =='a':
           stack.append(i)
           state = 'q3'
       elif state == 'q3' and i == 'a':
           stack.append(i)
       elif state == 'q3' and i == 'c':
           print("rejected")
           return "rejected"+"\n"+"=================="+"\n"
           break
       elif state == 'q3' and i == '\n':
           print("Approved")
           return "Approved"+"\n"+"=================="+"\n"
           break
       else:
           print('rejected')
           return "rejected"+"\n"+"=================="+"\n"
           break
    





def readfile(filename):
    strings = open(filename, 'r').readlines()

    ijkVar = random.randint(0,10)
    #ijkVar = 2
    #ijkVar = 3
    #Evens used to check when I==J
    #Odds used to check when J==K

    if(ijkVar %2 == 0):
       print("When, I == J")
       for string in strings:
            print("-----------------------------------------")
            print(string)
            file = open("Results.txt",'a')
            file.write("--------------------------------"+"\n")
            file.write("When, I == J"+"\n")
            AccOrRej = accept_or_reject(string)
            if(AccOrRej != None):
                file.write(string + "\n"+AccOrRej)
            else:
                break      
    else:
        print ("When, J == K")
        for string in strings:
            print("-----------------------------------------")
            print(string)
            file = open("Results.txt",'a')
            file.write("--------------------------------"+"\n")
            file.write("When, J == K"+"\n")
            AccOrRej = accept_or_reject2(string)
            if(AccOrRej != None):
                file.write(string + "\n"+AccOrRej)
            else:
                break
    file.close()



readfile("TestStrings.txt")
