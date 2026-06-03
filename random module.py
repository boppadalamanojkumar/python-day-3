## Random Module 
# it is used to generate random numbers and make random selections.
# this are enough to learn random.random() 1.random.random(), 2.random.randint(), 3.random.choice(), 4.random.shuffle()

# all are this 1.random.random(), 2.random.randint(a, b), 3.random.randrange(start, stop, step), 4.random.uniform(a, b), 5.random.choice(sequence), 6.random.shuffle(list), 7.random.sample(sequence, k)



### 1.random.random()
import random
print(random.random( ))


### 2.random.randint(a, b)
import random
print(random.randint(1,10)) #Returns a random integer between **a and b** (inclusive).
#------for practice------ 
import random
dice=random.randint(1,6)
print("dice value:",dice)


### 3.random.randrange(start, stop, step)
import random
print(random.randrange(1, 10, 2))  #Returns a random number from a range


### 4.random.uniform(a, b)
import random
print(random.uniform(1, 10))    #Returns a random floating-point number between a and b.


### 5.random.choice(sequence)
import random
fruits = ["apple", "banana", "mango"]
print(random.choice(fruits))            #Returns a random item from a list, tuple, or string.


### 6.random.shuffle(list)
import random

nums = [1, 2, 3, 4, 5]
random.shuffle(nums)      #Shuffles a list in place.
print(nums)


### 7.random.sample(sequence, k)

import random
nums = [1, 2, 3, 4, 5]
print(random.sample(nums, 2))   #Returns `k` unique random items.


## Interview Definitions

#| Function              | Definition                                     |
#| --------------------- | ---------------------------------------------- |
#| `random.random()`     | Returns a random float between 0.0 and 1.0     |
#| `random.randint(a,b)` | Returns a random integer between a and b       |
#| `random.randrange()`  | Returns a random number from a specified range |
#| `random.uniform(a,b)` | Returns a random float between a and b         |
#| `random.choice()`     | Returns a random element from a sequence       |
#| `random.shuffle()`    | Randomly rearranges the elements of a list     |
#| `random.sample()`     | Returns unique random elements from a sequence |

