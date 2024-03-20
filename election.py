# Part of a case-study #4: election
# Developers: Loseva Ekaterina, Shcherbina Ekaterina, Nesterova Alexandra
#

import ru_local as ru

def check_turnout(voter_turnout, number_voters):
    return voter_turnout / number_voters < 0.5

def max_candidate(number_voters):
    max_value = max(number_votes)
    return number_votes.index(max_value)

voter_turnout = 0
number_votes = [0, 0, 0, 0, 0]

number_voters = int(input(ru.who_can_vote))
number_polling_stations = int(input(ru.amount_pstations))
print(ru.results_rules)

for i in range(number_polling_stations):
    s = input()
    results_polling_stations = s.split()
    for j in range(number_candidates + 1):
        voter_turnout += int(results_polling_stations[j])
        number_votes[j] += int(results_polling_stations[j])
        
print(ru.procent_turnout, round(voter_turnout / number_voters * 100, 2), '%')
print (, round(number_votes[1] / voter_turnout * 100, 2), '%')
print ('Кощей Бессмертный набрал', round(number_votes[2] / voter_turnout * 100, 2), '%')
print ('Карлсон набрал', round(number_votes[3] / voter_turnout * 100, 2), '%')
print ('Райан Гослинг набрал', round(number_votes[4] / voter_turnout * 100, 2), '%')
print ('Испорченные бюллетени', round(number_votes[0] / voter_turnout * 100, 2), '%')

if check_turnout(voter_turnout,number_voters):
    print('Не набран минимальный порог явки, выборы недействительны')
else:
    number_votes[0] = 0
    if number_votes[max_candidate(number_voters)] / voter_turnout < 0.5:
        print('Ни один кандидат не набрал более 50% голосов, необходимо провести второй тур выборов. Участники второго тура: ')
        match max_candidate(number_voters):
            case 1:
                print("Джеки Чан")
            case 2:
                print("Кощей Бессмертный")
            case 3:
                print("Карлсон")
            case 4:
                print("Райан Гослинг")
        number_votes[max_candidate(number_voters)] = -1
        match max_candidate(number_voters):
            case 1:
                print("Джеки Чан")
            case 2:
                print("Кощей Бессмертный")
            case 3:
                print("Карлсон")
            case 4:
                print("Райан Гослинг")
    else:
        print('По итогам выборов следующий президент:')
        match max_candidate(number_voters):
            case 1:
                print("Джеки Чан")
            case 2:
                print("Кощей Бессмертный")
            case 3:
                print("Карлсон")
            case 4:
                print("Райан Гослинг")

date_inauguration = '25 октября' if voter_turnout / number_voters > 0.5 and number_votes[max_candidate(number_voters)] / voter_turnout > 0.5 else '15 ноября'
print('Инаугурация состоится', date_inauguration)

