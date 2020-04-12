import json

filename = "population_data.json"
with open(filename) as read:
    popInfo = json.load(read)

    for pop2010 in popInfo:
        if pop2010['Year'] == '2010':
            country_name = pop2010['Country Name']
            population = pop2010["Value"]
            print(country_name+" has "+population+" people in 2010")