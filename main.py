start = int(input("Enter your number"))
end = int(input("Enter your number"))
for i in range(start,end + 1):
    if i%7 ==0:
        print(i)
        
start = int(input("Enter your number"))
end = int(input("Enter your number"))
print("All numbers")
for i in range(start,end,+ 1):
     print(i)
print("All numbers descending order")    
for i in range(end,start,- 1):
      print(i)
                    
print("all number %7")                
for i in range(start,end): 
          if i%7 ==0:
              print(i)
print("Numbers 5")
for i in range(start,end):
       if i%5 ==0:
             print(i)                      

a = int(input("Enter your number"))
b = int(input("Enter your number"))
for i in range(a,b):
    if i%3 == 0 and i%5 ==0:
        print("Fizz Buzz")
    elif i%3 ==0:
        print("Fizz")   
    elif i%5 ==0:
        print("Buzz")
    elif i%3 !=0 and i%5 !=0:
       print(i)    