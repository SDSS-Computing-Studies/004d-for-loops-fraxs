#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""
x = int( input("Enter a number: "))
if x > 10:
    print("no")
    exit()
else:
    pass
start = 1
number = "0"
end = 0
for i in range(1, x+1):
    number = str(number)            # number '0'
    number = number + "1"           # number '01'                  # start 1
    number = int(number)            
    result = start * number            
    end = end + result    
print(f"the sum of the series is {end}")

