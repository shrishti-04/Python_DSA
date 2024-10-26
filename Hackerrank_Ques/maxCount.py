# Birthday Cake Candles

# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# Example
# candles = [4, 4, 1, 3]

# The maximum height candles are 4 units high. There are 2 of them, so return 2.

candles = [3, 7, 5, 3, 7, 6, 7]
count = 0
mx = 0

for i in candles:
    if(i > mx):
        mx = i
        count = 0
        
    if(i == mx):
        count += 1
        
print(count)