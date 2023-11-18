import random
lottery_numbers = set(random.sample(list(range(22)), 6))
# print(lottery_numbers)

players = [
    ('Jiselle', {3, 7, 20, 13, 6, 9} ),
    ('Sam', {20, 2, 7, 1, 13, 15}),
    ('Diegl', {0, 10, 7, 4, 18, 15}),
    ('Arleen', {10, 9, 15, 7, 6, 2})
]
    
num_winnings = []
for name, guess in players:
    winnings = guess.intersection(lottery_numbers)
    len_winnings = len(winnings)
    
    num_winnings.append(len_winnings)

    print(f"{name} won {len_winnings}.")
    
print(num_winnings)

## get the maximum number of winnings
maximum = max(num_winnings)

nms = []
for i in range(len(players)):
    if num_winnings[i] == maximum:
        nms.append( players[i][0] )

print(f"{nms} won the most.")

