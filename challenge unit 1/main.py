def factorial(n):
  #base case:factorial of 0 is 1
  if n == 0:
      return 1
  # Recursive case:factorial of n is n times factorial of (n-1)
  else:
     return n * factorial(n - 1)
number = int(input("Enter number:"))
result=factorial(number)
print(f"The factorial of{number}is{result}")
