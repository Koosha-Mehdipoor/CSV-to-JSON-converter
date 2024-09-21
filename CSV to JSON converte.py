import json
#defining a list for being able to add the dictionaries
json_list = []
    #opening the csv file with context manager
with open('/Users/koosha.mehdipoor@igenius.ai/Desktop/CODE/First_Milestone/CSV to Json Converter/csv_file.txt', 'r') as file:

# iterate over the file and remove the "," and "\n" by strip function
    for line in file.readlines():
        club , city, country = line.strip().split(',')
        # assigning the values to a dictionary as data and then append it to the json_list, if we don't do the append the data will
        # be overwritten
        data = {
            'club': club,
            'city': city,
            'country': country
        }
        json_list.append(data)
    print(json_list)


with open('/Users/koosha.mehdipoor@igenius.ai/Desktop/CODE/First_Milestone/CSV to Json Converter/json_export.json','w') as file:
    json.dump(json_list, file)

