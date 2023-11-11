Jin_friends = {'Jack', 'Tom', 'Mary'}
Mark_friends = {'Lily', 'Tom', 'Jack', 'Jeff'}

# --- common friends
# common_friends = Jin_friends & Mark_friends
common_friends = Jin_friends.intersection(Mark_friends)
print(f"Common friends are {common_friends}.")

# ---  students who are jin's friends, but not Mark's
# Jin_not_Mark = Jin_friends - Mark_friends
Jin_not_Mark = Jin_friends.difference(Mark_friends)
print(f"Jin_not_Mark are {Jin_not_Mark}")

# students who are Mark's friends, but not Jin's
# Mark_not_Jin = Mark_friends - Jin_friends
Mark_not_Jin = Mark_friends.difference(Jin_friends)
print(f"Mark_not_Jin are {Mark_not_Jin}.")

# ---  uncommon friends
# uncommon =  Jin_not_Mark.union(Mark_not_Jin)
# print(uncommon)

all = Jin_friends.union(Mark_friends)
uncommon = all - common_friends

print(uncommon)