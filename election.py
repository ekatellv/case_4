# Part of a case-study #4: election
# Developers: Loseva Ekaterina, Shcherbina Ekaterina, Nesterova Alexandra
#

import ru_local as ru

voter_turnout = 0
number_votes = [0]

number_voters = int(input('Введите количество избирателей в стране: '))
number_candidates = int(input('Введите количество кандидатов, участвующих в выборах: '))
number_polling_stations = int(input('Введите количество избирательных участков в стране: '))
print('Введите результаты на избирательных участках. Вводите через пробел, первое число – кол-во испорченных бюллетеней, далее данные о кандидатах по списку')

for i in range(number_candidates):
    number_votes.append(0)

for i in range(number_polling_stations):
    s = input()
    results_polling_stations = s.split()
    for j in range(number_candidates + 1):
        voter_turnout += int(results_polling_stations[j])
        number_votes[j] += int(results_polling_stations[j])

print(voter_turnout)
print(number_votes)

