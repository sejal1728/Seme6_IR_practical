def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j  # Insert all characters of s2
            elif j == 0:
                dp[i][j] = i  # Remove all characters of s1
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match, no cost
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # Deletion
                    dp[i][j - 1],    # Insertion
                    dp[i - 1][j - 1] # Substitution
                )
    return dp[m][n]

# Example usage:
s1 = "kitten"
s2 = "sitting"
print("Edit Distance:", edit_distance(s1, s2))
