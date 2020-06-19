#!/usr/bin/env python

import random
import json
import os

count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]
#words = [word.strip() for word in open('/usr/share/dict/words').readlines()]
for i in range(count):
    amount = random.uniform(1.0,1000)
    content= {
        'topic': random.choice(words),
        'value': "%.2f" %amount
    }
    with open(f'./new/reciept-{i}.json', 'w') as f:
        json.dump(content, f)
#print(random.uniform(1,5))
