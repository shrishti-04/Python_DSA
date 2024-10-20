# break example

i = 1
while(i < 5):
    if(i == 3):
        break
    print(i)
    i += 1
    
# continue example
# to get odd numbers

i = 1
while(i <= 10):
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1