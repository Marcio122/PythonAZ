#keep taking input from user and print sum of all numbers until
#user give input as 0

num = 1
sum = 0

print("Enter number for sum, Press '0' to exit. ")

while num != 0:
    num = int(input("Enter Number: "))
    sum = num + sum
    print("Current Sum: ", sum)

else:
    print('Loop Completed.')