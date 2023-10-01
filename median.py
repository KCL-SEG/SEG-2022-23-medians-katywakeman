"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
         n = len(numbers)
    for i in range(n):
      for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
          temp = numbers[j]
          numbers[j] = numbers[j + 1]
          numbers[j + 1] = temp
    if (len(numbers) % 2) == 0:
        median = (numbers[int(n/2)] + numbers[int(n/2 - 1)]) / 2
    else:
      x = n / 2 + 0.5
      median = numbers[int(x) - 1]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
print(median)
