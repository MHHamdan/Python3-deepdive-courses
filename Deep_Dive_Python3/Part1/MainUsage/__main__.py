# runTime.py

import timing

code = '[x**3 for x in range(1_100)]'
print(code)



result = timing.timeit(code, 10000)

print(result)