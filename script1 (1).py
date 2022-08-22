
#script2
lower =int(input("Enter the lower limit or Number: "))
upper =int(input("Enter the upper limit or Number: "))


for num in range(lower, upper + 1):
    if num > 1:
        #this for loop check if the num value is prime or not
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
