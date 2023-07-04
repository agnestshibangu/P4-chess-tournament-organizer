import json

def add_tour_to_tournament_json(tour):

    tourName = tour._name
   
    dictionary = {
    "tour": tourName 
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)

    