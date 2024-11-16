# An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps steps, 
# for every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level, 
# and each step up or down represents a 1 unit change in altitude. We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

# Example

# steps = 8 path = [D, D, U, U, U, U, D, D]

# The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain  units high. Finally, the hiker returns to sea level and ends the hike.

def countingValleys(steps, path):
    total_val = 0
    ups = 0
    downs = 0
    
    for i in range(steps):
        if(path[i] == 'U'):
            ups += 1
            if(ups == downs):
                total_val += 1
        else:
            downs += 1
            
    print(total_val)
    
countingValleys(12, ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U', 'D', 'D', 'U', 'U'])
# output will be 2