import json


"""
Generates a CSV Item deck using the JSON mapping file to create one
deck for the passed in category of item.
@map_file The JSON file containing item data, and image mapping data.
@category The category of item to generate a deck of.
@output_path The output path of the csv file.
"""
def generate_item_deck(json_path, category, output_path, tag):
    with open(json_path, 'r') as file:
        with open(output_path, 'w') as csv:
            data = json.loads(file.read())
            category_data = data[category]

            for item in category_data:
                line = ""
                line += generate_item_front(item)
                line += generate_item_back(item)
                line += tag

                csv.write(line + '\n')
                

def generate_item_front(item):
    return '<p style="font-weight: 700">Name the item, effects, and abilities:</p><br /><img src="' + item['icon_path']  + '"/>;'

def generate_item_back(item):
    output = '<img src="' + item['infobox_path'] + '" style="padding: 5px"/>'
    if len(item['abilities']) > 0:
        for ability in item['abilities']:
            output += '<img src="' + ability['ability_image_path'] +'" style="padding: 5px"/>'

    output += '<br /><a href="' + item['wiki'] + '" style="font-weight: 700">Wiki Page</a>;'
    return output
