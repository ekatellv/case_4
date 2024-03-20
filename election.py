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

number_voters = int(input(ru.WHO_CAN_VOTE))
number_polling_stations = int(input(ru.AMOUNT_PSTATION))
print(ru.RESULTS_RULES)

for i in range(number_polling_stations):
    s = input()
    results_polling_stations = s.split()
    for j in range(number_candidates + 1):
        voter_turnout += int(results_polling_stations[j])
        number_votes[j] += int(results_polling_stations[j])
        
print(ru.PROCENT_TURNOUT, round(voter_turnout / number_voters * 100, 2), '%')
print (ru.JACKIE_CHAN, round(number_votes[1] / voter_turnout * 100, 2), '%')
print (ru.KOSCHEY, round(number_votes[2] / voter_turnout * 100, 2), '%')
print (ru.KARLSON, round(number_votes[3] / voter_turnout * 100, 2), '%')
print (ru.RAYAN_GOSLING, round(number_votes[4] / voter_turnout * 100, 2), '%')
print (ru.SPOILED_BALLOT, round(number_votes[0] / voter_turnout * 100, 2), '%')

if check_turnout(voter_turnout,number_voters):
    print(ru.NOT_MIN_TURNOUT)
else:
    number_votes[0] = 0
    if number_votes[max_candidate(number_voters)] / voter_turnout < 0.5:
        print(NOT_MIN_VOTES)
        match max_candidate(number_voters):
            case 1:
                print(ru.JACKIE_CHAN)
            case 2:
                print(ru.KOSCHEY)
            case 3:
                print(ru.KARLSON)
            case 4:
                print(ru.RAYAN_GOSLING )
        number_votes[max_candidate(number_voters)] = -1
        match max_candidate(number_voters):
                case 1:
                print(ru.JACKIE_CHAN)
            case 2:
                print(ru.KOSCHEY)
            case 3:
                print(ru.KARLSON)
            case 4:
                print(ru.RAYAN_GOSLING )
    else:
        print(ru.NEXT_PRESIDENT)
        match max_candidate(number_voters):
                 case 1:
                print(ru.JACKIE_CHAN)
            case 2:
                print(ru.KOSCHEY)
            case 3:
                print(ru.KARLSON)
            case 4:
                print(ru.RAYAN_GOSLING )

date_inauguration = ru.DATA if voter_turnout / number_voters > 0.5 and number_votes[max_candidate(number_voters)] / voter_turnout > 0.5 else ru.DATA_1
print(ru.INAUGURATION, date_inauguration)

