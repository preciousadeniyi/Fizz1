# Fizz1
for x in range(1,101):# thats for loop that part of that code create a sequence of numbers from 1-100
    i = ""  #i use that to create an empty string it will be use later to create space between the words in the output 
  
    if x % 3 == 0: is to check if the the number is evenly divisible by zero
        i = 'fizz' it create variable "i" and set to string fizz
    if x % 3 == 0: this is ternary operation to write conditional statement in short form  
        i += 'buzz'
        #continue 
    print(x if not i else i)   its used to print either x or i
