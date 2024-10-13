def count_votes_from_file(filename: str) -> dict:
    """
    Функція для підрахунку голосів з файлу.
    :param filename: Ім'я файлу, який містить результати голосування.
    :return:Словник, де ключами є імена кандидатів, а значеннями — сумарна кількість голосів, які вони отримали.
    """
    votes_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            name, votes = line.strip().split()
            votes_dict[name] = votes_dict.get(name, 0) + int(votes)
    return votes_dict


def determine_winner(votes_dict: dict) -> str:
    """
    Функція для визначення переможця на основі підрахованих голосів.

    :param votes_dict: Словник з іменами кандидатів як ключами і сумарними голосами як значеннями.
    :return: Кортеж, що містить словник голосів та ім'я переможця або повідомлення "3-тий тур голосування."
    """
    max_votes = max(votes_dict.values())
    winners = []

    for name, votes in votes_dict.items():
        if votes == max_votes:
            winners.append(name)

    if len(winners) > 1:
        return "3-тий тур голосування."
    else:
        return f"Переможець: {winners[0]}"


filename = 'File.txt'
votes = count_votes_from_file(filename)
print(votes)
print(determine_winner(votes))



