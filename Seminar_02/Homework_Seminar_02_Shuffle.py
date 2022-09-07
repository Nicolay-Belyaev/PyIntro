# Реализуйте алгоритм перемешивания списка.
import random
import time

# start_time = time.time()

in_array = []
result_array = []
for i in range(0, 10):
    # in_array.append(random.randint(0, 10000))
    in_array.append(i)
print(in_array)

len_of_in_array = len(in_array)

while len(result_array) != len_of_in_array:
    rnd_elem = in_array.pop(random.randint(0, len(in_array)-1))
    result_array.append(rnd_elem)

# print("--- %s seconds ---" % (time.time() - start_time))
print(result_array)

# uniques
# len 10         - 0.00000 sec
# len 100        - 0.00000 sec
# len 1000       - 0.00000 sec
# len 10000      - 0.00199 sec
# len 10.000     - 0.02098 sec
# len 100.000    - 0.08685 sec
# len 500.000    - 19.6325 sec
# len 1.000.000  - 90.8550 sec

# non-uniqes, random(0, 10000)
# len 10         - 0.00000 sec
# len 100        - 0.00100 sec
# len 1000       - 0.00298 sec
# len 10000      - 0.03198 sec
# len 10.000     - 0.02098 sec
# len 100.000    - 0.98244 sec
# len 500.000    - 20.4036 sec
# len 1.000.000  - 93.5962 sec