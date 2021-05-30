import json
import re


class Parser():
    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file

    def get_all_mnemonics(self) -> list:
        with open('mnemonics.json') as file:
            data = file.read()
            mnemonics = json.loads(data)
            list_of_mnemonics = list()
            for element in mnemonics:
                list_of_mnemonics.append(element["name"].lower())
        return list_of_mnemonics

    def find_labels(self) -> dict:
        labels_dict = dict()
        with open(self.path_to_file, 'r+') as file_to_parse:
            data = file_to_parse.readlines()
            for line in data:
                try:
                    result_label = re.search('.(.*):', line)
                    labels_dict[result_label.group(1)] = ' '
                except AttributeError:
                    pass
        return labels_dict

    def find_code_under_labels(self, labels_dict: dict) -> dict:
        with open(self.path_to_file, 'r+') as file_to_parse:
            data = file_to_parse.read()
            for key in labels_dict.keys():
                try:
                    next_key = list(labels_dict)[list(labels_dict.keys()).index(key) + 1]
                    start = data.find('.' + key + ':') + len(key) + 2
                    stop = data.find('.' + next_key + ':')
                    labels_dict[key] = data[start:stop]
                except IndexError:
                    start = data.find('.' + key + ':') + len(key) + 2
                    labels_dict[key] = data[start:]
                except AttributeError:
                    pass
        labels_with_code_dict = labels_dict.copy()
        return labels_with_code_dict


if __name__ == '__main__':
    pass