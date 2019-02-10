import collections
import math

print("Hello World")


counter = collections.Counter()

for i in range(0, 100000):
    counter[math.sqrt(i) // 25] += 1

for key, count in counter.most_common(5):
    print('Count for %s: %d' % (key, count))
