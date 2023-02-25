# 1. Write a program that will simulate user score in a computer game. Create a list with 5 player’s names. After that simulate 
# 10 games for each player (use random). As a result of the game create a list with player’s name and his score (0-100 range). 
# And save it to a CSV file. File should looks like this:
# Player name, Score
# Josh, 56
# Luke, 78
# Kate, 90
# Mark, 12
# Mary, 87
# Josh, 64

from unittest.util import sorted_list_difference
import numpy
import csv

def save_data_to_file(data: list, filename: str) -> bool:
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=csv_columns)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
            return True
    except IOError:
        print('I/O error')
        return False


players = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']

games_result = []
rounds = 1

csv_columns = ['Player name', 'Score']
while rounds <= 10:
    for player_name in players:
        round_result = {}
        round_result['Player name'] = player_name
        round_result['Score'] = int(numpy.random.uniform(0, 100))
        games_result.append(round_result)
    rounds += 1

save_data_to_file(games_result, 'players_score.csv')


# 2. Write a script that reads the data from previous CSV file and creates a new file called high_scores.csv where each row contains the player
#  name and their highest score. Final score should sorted by descending of highest score . The output CSV file should look like this:
# Player name, Highest score
# Kate, 90
# Mary, 87
# Luke, 78
# Josh, 64
# Mark, 12



def get_file_data(filename: str) -> list:
    file = open(filename, "r")
    games_result = list(csv.DictReader(file, delimiter=","))
    file.close()
    return games_result


def find_highest_score(games_result: list) -> list:
    highest_result = {}
    for player_result in games_result:
        player_name = player_result['Player name']
        score = int(player_result['Score'])
        if player_name not in highest_result:
            highest_result[player_name] = score
        else:
            if score > highest_result[player_name]:
                highest_result[player_name] = score
        
    highest_result_list = []
    for result in highest_result.items():
        highest_result_list.append({'Player name':result[0], 'Score':result[1]})

    return highest_result_list

def sort_highest_result(highest_result_list: list) -> list:
    sorted_highest_result_list = sorted(highest_result_list, key=lambda d: d['Score'], reverse=True) 

    return sorted_highest_result_list


results = get_file_data('players_score.csv')

highest_result_list = find_highest_score(results)

sorted_highest_result = sort_highest_result(highest_result_list)

save_data_to_file(sorted_highest_result, 'high_scores.csv')