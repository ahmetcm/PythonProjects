def cross(times):
    times.sort()
    n = len(times)

    # Eğer sadece bir kişi varsa
    if n == 1:
        return times[0]

    timeTotal = 0

    while len(times) > 3:
        # 1. İlk önce en hızlı iki kişi geçsin, en hızlı geri dönsün.
        # 2. En yavaş iki kişi geçsin, ikinci en hızlı geri dönsün.
        # İki stratejiyi karşılaştırıyoruz.
        option1 = 2 * times[1] + times[0] + times[-1]
        option2 = 2 * times[0] + times[-2] + times[-1]

        timeTotal += min(option1, option2)

        # Geçen en yavaş iki kişiyi listeden çıkarma
        times = times[:-2]

    # Son üç veya daha az kişi
    if len(times) == 3:
        timeTotal += times[0] + times[1] + times[2]
    elif len(times) == 2:
        timeTotal += times[1]

    return timeTotal

if __name__ == "__main__":
    userInput = input()
    times = list(map(int, userInput.split()))
    result = cross(times)
    print("Minimum total time required:", result)
