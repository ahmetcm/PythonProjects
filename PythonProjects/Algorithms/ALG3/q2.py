def game(coins):
    n = len(coins)
    # Create a table to store solutions to subproblems
    dp = [[0] * n for _ in range(n)]

    # Fill the table for subproblems of size 1 (diagonal)
    for i in range(n):
        dp[i][i] = coins[i]

    # Solve for larger subproblems
    for lng in range(2, n + 1):  # lng is the size of the current subproblem
        for i in range(n - lng + 1):
            j = i + lng - 1  # Ending index of the subproblem
            # Player chooses the first coin or the last coin
            first = coins[i] + min(dp[i + 2][j] if i + 2 <= j else 0,
                                        dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
            last = coins[j] + min(dp[i][j - 2] if i <= j - 2 else 0,
                                       dp[i + 1][j - 1] if i + 1 <= j - 1 else 0)
            dp[i][j] = max(first, last)

    return dp[0][n - 1]  # Maximum value for the whole range

def main():
    n = int(input().strip())  # Number of coins
    coins = [int(input().strip()) for _ in range(n)]  # Coin values

    # Player 1 uses the dynamic programming approach
    player1_score = game(coins)

    # Output the result
    print(f"Maximum amount of Player 1: {player1_score}")

if __name__ == "__main__":
    main()

# Time Complexity:
# The algorithm uses a 2D table dp of size n x n, where each cell is computed once.
# Overall time complexity is O(n^2).
# Space Complexity: O(n^2) due to the dp table.