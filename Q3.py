from math import factorial
 
# input for the number of rows
n = int(input("Rows:")
for i in range(n):
    for j in range(n-i+1):
        # for left spacing
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    # for new line
    print()
