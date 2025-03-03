# In a tree of zeroes and ones , give the final answer as no.of islands can be formed. 
# It forms an island where ones are connected and surrounded by zeroes.

def createIsland(root):
    dp = {}

    def dfs(node):
        if(not node):
            return 0
        
        if(not node[1] and not node[2]):
            dp[node] = node[0]
            return dp[node]
        
        left_count = dfs(node[1])
        right_count = dfs(node[2])

        if(node[0] == 0):
            dp[node] = left_count + right_count
        else:
            if(node[1] and node[1][0] == 1 and node[2] and node[2][0] == 1):
                dp[node] = left_count + right_count - 1
            elif(node[1] and node[1][0] == 1):
                dp[node] = left_count + right_count
            elif(node[2] and node[2][0] == 1):
                dp[node] = left_count + right_count
            else:
                dp[node] = 1 + left_count + right_count

        return dp[node]

    return dfs(root)
            