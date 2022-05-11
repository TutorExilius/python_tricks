"""
Added: 2022-05-11
Updated: -
"""

from collections import defaultdict
items = ['a', 'b', 'a', 'c', 'd', 'd', 'd', 'c', 'a', 'b']

counter = defaultdict(int)

for item in items:
    counter[item] += 1

print(counter)



from collections import Counter
items = ['a', 'b', 'a', 'c', 'd', 'd', 'd', 'c', 'a', 'b']

counts = Counter(items)
print(counts)

print(dict(counts)) # as native dict