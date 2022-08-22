#script1
num=int(input("Enter a number="))
for num in range(2, num + 1):
    if num > 1:
        #this for loop check if the num value is prime or not
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
  
