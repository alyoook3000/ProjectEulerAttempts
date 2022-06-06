def fibsEvenSum(t, a=1, b=2):
  while a < t:
    yield a
    a, b = b, a + b

fibs = fibsEvenSum(4000000)
fibssum = sum(n for n in fibs if n % 2 == 0)
print(fibssum)





