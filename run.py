#! /usr/bin/env python3

import os
import requests

def get_dictionary_list(result, dir):
    dic_list = []
    jpeg_counter = 1
    for file_from_list in result:
        with open(dir + file_from_list) as file_data:
            dict_return = {
                'name': 'name',
                'weight': 'weight',
                'description': 'description',
                'image_name': 'image_name',
            }
            counter = 0
            for line in file_data:
                if counter == 0:
                    dict_return['name'] = line.replace( '\n' , '' )
                    counter += 1
                elif counter == 1:
                    dict_return['weight'] = line.replace( '\n' , '' )[:-3]
                    counter += 1
                elif counter == 2:
                    dict_return['description'] = line.replace( '\n' , '' )
                    counter += 1

        if jpeg_counter < 10:
            dict_return['image_name'] = '00' + str(jpeg_counter) + '.jpeg'
        else:
            dict_return['image_name'] = '0' + str(jpeg_counter) + '.jpeg'
        jpeg_counter += 1
        
        dic_list.append(dict_return)

    return dic_list

def json_request(json_data):
    response = requests.post('http://34.68.197.211/fruits/', json=json_data)

def main():
    dir = "supplier-data/descriptions/"
    result = os.listdir(dir)

    json_data_list = get_dictionary_list(result, dir)

    for json_data in json_data_list:
        json_request(json_data)
    
if __name__ == "__main__":
    main()
