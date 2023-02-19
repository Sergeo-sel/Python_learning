# One day you decide to arrange all your 100 cats in a giant circle. Initially, none of your cats have any hats on. 
# You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time 
# you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
# The first round, you stop at every cat, placing a hat on each one.
# The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat). Write a program 
# that simply outputs which cats have hats at the end.

# First soluyion
cats_list = [False] * 100
round_counts = 0

while round_counts <= len(cats_list):
    rounds = range(round_counts, len(cats_list), round_counts + 1)
    for i in rounds:
        cats_list[i] = not cats_list[i]
    round_counts += 1

print(cats_list)


# Second solution

cats_list = [False] * 100
rounds = []
m_list = range(1, 11)
for el in m_list:
    rounds.append(el * el)

for i in rounds:
    cats_list[i-1] = True

print(cats_list)