from MODELS.houseData import json_string
import json

# data = json.loads(json_string)
# players_list = data['players']
# print(players_list)


def sort_alpha_players(players_list):

    def return_first_name(player):
        return player['firstName']

    players_list.sort(key=return_first_name)
    sorted_list =  players_list
    return sorted_list




def convert_to_json(sorted_list):

    # Data to be written
    dictionary = sorted_list

    with open("list-players-alpha-sorted.json", "w") as outfile:
        json.dump(dictionary, outfile)

    print('json file created')

    # # python object to be appended
    # # y = {"pin":110096}

    # # parsing JSON string:
    # z = json.loads(dictionary)

    # # appending the data
    # z.update(y)

    # # the result is a JSON string:
    # print(json.dumps(z))

