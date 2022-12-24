import random

result_ans = []
for i in range(1000):
    a = random.randint(0,20)
    b = random.randint(0,30000)
    result = (a**b)%10
    result_ans.append({
        "a":a,
        "b":b,
        "result":result
    })

import json
json.dump()