# There are a number of people who will be attending ACM-ICPC World Finals. 
# Each of them may be well versed in a number of topics. Given a list of topics known by each attendee, 
# presented as binary strings, determine the maximum number of topics a 2-person team can know. 
# Each subject has a column in the binary string, and a '1' means the subject is known while '0' means it is not. 
# Also determine the number of teams that know the maximum number of topics. Return an integer array with two elements. 
# The first is the maximum number of topics known, and the second is the number of teams that know that number of topics.

# Example
# n = 3
# topics = ['10101', '11110', '00010']

# The attendee data is aligned for clarity below:

# 10101
# 11110
# 00010
# These are all possible teams that can be formed:

# Members Subjects
# (1,2)   [1,2,3,4,5]
# (1,3)   [1,3,4,5]
# (2,3)   [1,2,3,4]
# In this case, the first team will know all 5 subjects. 
# They are the only team that can be created that knows that many subjects, so [5, 1] is returned.

def acmTeam(team):
    team_str = []
    
    for i in range(len(team)-1):
        s1 = team[i]
        
        for j in range(i+1, len(team)):
            s2 = team[j]
            
            count = 0
            for i in range(len(s1)):
                if(s1[i] == '1' or s2[i] == '1'):
                    count += 1
                    
            team_str.append(count)
            
    m = max(team_str)
    
    ans = 0
    for i in range(len(team_str)):
        if(team_str[i] == m):
            ans += 1
            
    return [m, ans]

answer = acmTeam(['10101', '11100', '11010', '00101'])
print(answer)