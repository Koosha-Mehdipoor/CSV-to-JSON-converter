import json
#defining a list for being able to add the dictionaries
json_list = []
#opening the csv file
csv_file = open('/Users/koosha.mehdipoor@igenius.ai/Desktop/CODE/First_Milestone/CSV to Json Converter/csv_file.txt', 'r')

# iterate over the file and remove the "," and "\n" by strip function
for line in csv_file.readlines():
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
csv_file.close()

json_file = open('/Users/koosha.mehdipoor@igenius.ai/Desktop/CODE/First_Milestone/CSV to Json Converter/json_export.json','w')
json.dump(json_list, json_file)
json_file.close()

