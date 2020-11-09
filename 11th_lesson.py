import datetime
start = datetime.datetime.now()
my_list = [f"{x} - something" for x in range(1_000_000)]
end = datetime.datetime.now()
print(start, end)
print(end-start)

import random
random.seed(42)
numbers = [random.randint(1,6) for n in range(100)]
floats = [random.random() for _ in range(10)]
#if I do not use the inner variable convention is to use _
print(max(numbers))
print(numbers[:5], floats[:5])

import 11th_les_my_mod