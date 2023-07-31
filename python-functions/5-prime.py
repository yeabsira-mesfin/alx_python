def is_prime(number):
    if abs(number) %2 == 0:
      return  True
    else:
     return   False
print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(0))