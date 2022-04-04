# number 1

def sum_to(n):
  numbers = range(1, n+1)
  print(sum(numbers))

sum_to(6)

# number 2

def largest(list):
  print(max(list))

largest([1, 20, 3, 4, 0])

# number 3

def occurences(str1, str2):
  print(str1.count(str2))

occurences('apple', 'p')


# number 4

def product(*args):
  product = 1
  for arg in args:
    product *= arg
  print(product)

product(4, 0.5, 5)