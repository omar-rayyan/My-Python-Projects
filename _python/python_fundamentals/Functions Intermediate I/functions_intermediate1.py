import random

def randInt(min=0, max=100):
    if min > max & max < 0:
        return None
    
    if max is not None and min is None:
        return round(random.random() * max)
    
    elif min is not None and max is None:
        return round(random.random() * (100 - min) + min)
    
    elif min is not None and max is not None:
        return round(random.random() * (max - min) + min)
    
    else:
        return round(random.random() * 100)

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))