def paint(boards, k):
    n = len(boards)

    def calSum(start, end):
        return sum(boards[start:end + 1])

    # Dinamik programlama tablosu
    table = [[0] * (k + 1) for _ in range(n + 1)]

    # 1 boyacı olduğunda toplam süre = tüm tahtaların toplamı
    for i in range(1, n + 1):
        table[i][1] = calSum(0, i - 1)

    # 1 tahtayı boyamak için süre = tahtanın uzunluğu
    for j in range(1, k + 1):
        table[1][j] = boards[0]

    # Dinamik programlama tablosunu doldur
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            best = float('inf')
            for p in range(1, i + 1):
                best = min(best, max(table[p][j - 1], calSum(p, i - 1)))
            table[i][j] = best

    return table[n][k]

if __name__ == "__main__":
    boards = list(map(int, input().split()))
    k = int(input())

    result = paint(boards, k)
    print("Minimum time required:", result)
