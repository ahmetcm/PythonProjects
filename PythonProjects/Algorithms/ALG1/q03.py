def average_distance(villages, post_office_location):
    total_distance = 0
    n = len(villages)

    for village in villages:
        total_distance += abs(village - post_office_location)

    return total_distance / n


def find_best_post_office(villages):
    min_average_distance = float('inf')
    best_location = None

    for village in villages:
        avg_distance = average_distance(villages, village)
        print(f'Testing post office location at {village}: average distance = {avg_distance}')  # Durumu yazdır

        if avg_distance < min_average_distance:
            min_average_distance = avg_distance
            best_location = village

    return best_location


villages = [1, 5, 7, 9, 12, 17, 20]
best_location = find_best_post_office(villages)
print(f'The best location for the post office is at: {best_location}')




