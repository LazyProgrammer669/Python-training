from collections import Counter

def sumowanie(dict1, dict2):
    return dict(Counter(dict1) + Counter(dict2))

dict1 = {1: 1, 2: 1, 3: 1, 4: 1}
dict2 = {3: 1, 4: 1, 5: 1, 6: 1}

print(sumowanie (dict1, dict2))