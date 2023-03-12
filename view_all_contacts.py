import json
import contriller


path_to_db = 'db.json'


def view_all_contacts():

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    contriller.user_choice()