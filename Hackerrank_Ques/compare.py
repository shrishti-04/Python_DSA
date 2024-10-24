# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.

# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).

# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.

# Given a and b, determine their respective comparison points.

a = [4, 7, 3]
b = [5, 2, 8]

n = len(a)
alice_point = 0
bob_point = 0

for i in range(n):
    if(a[i] == b[i]):
        continue
    elif(a[i] > b[i]):
        alice_point += 1
    else:
        bob_point += 1
        
ans = [alice_point, bob_point]
print(ans)