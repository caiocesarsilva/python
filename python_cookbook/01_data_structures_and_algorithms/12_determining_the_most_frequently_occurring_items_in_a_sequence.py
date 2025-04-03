words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
          'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
          'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
          'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

#######################################################################

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

word_counts.update(morewords)

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)

#Combine counts
c = a + b
print(c)

#Subtract counts
d = a - b
print(d)
