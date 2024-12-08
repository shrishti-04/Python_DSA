# There is a strange counter. At the first second, it displays the number 3. 
# Each second, the number displayed by decrements by 1 until it reaches 1. 
# In next second, the timer resets to 2 * initial number of prior cycle and continues counting down. 
# The diagram below shows the counter values for each time t in the first three cycles:
    
# for whole question visit: https://www.hackerrank.com/challenges/strange-code/problem?h_r=profile

def strangeCounter(t):
    start = 1
    value = 3

    while(t >= (start + value)):
        start += value
        value *= 2

    return value - (t - start)

result = strangeCounter(13)
print(result)