# n_winnings may be 0, 1, 2, 3, 4, 5, 6
# probabilities for 0, 1, 2, 3, 4, 5, 6

import random

guess = {1, 3, 4, 6, 9, 10}

# collect number of winnings N times.
N = 1000000
nums = []
for i in range(N):
    lottery_numbers = set(random.sample(list(range(22)), 6))
    n_winnings = len(guess.intersection(lottery_numbers))
    
    nums.append(n_winnings)
# print(nums)

# compute the prob for each number, 0, 1, 2, 3, 4, 5, 6
prob = [nums.count(i)/N for i in range(7)]
print(prob)

# what is mean of the number of winnings?
mean = sum(nums)/len(nums)
print(mean)

# what is expectation of your revenue?
earnings = [0, 5, 5, 10, 100, 100, 100000]
mean = 0
for i in range(len(prob)):
    m = prob[i] * earnings[i]
    mean += m
print(mean)    
