def greedy(coins):
    p1 = 0
    p2 = 0
    turn = 1  # Player 1 starts first

    while coins:
        if coins[0] >= coins[-1]:
            cur_coin = coins.pop(0)  # Take the first coin
        else:
            cur_coin = coins.pop(-1)  # Take the last coin

        if turn == 1:
            p1 += cur_coin
            turn = 2  # Switch to player 2
        else:
            p2 += cur_coin
            turn = 1  # Switch back to player 1

    return p1

def main():
    n = int(input().strip())
    coins = [int(input().strip()) for _ in range(n)]

    # Player 1 uses the greedy algorithm
    score_p1 = greedy(coins[:])

    # Output the result
    print(f"Player 1's total score using greedy strategy: {score_p1}")

if __name__ == "__main__":
    main()
