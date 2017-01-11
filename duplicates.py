import os
from collections import defaultdict


def get_files_count(directory):
    files_same_size = defaultdict(list)
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            if os.path.exists(filepath):
                files_same_size[os.path.basename(filepath) + ' ' + str(os.path.getsize(filepath))].append(filepath)
    return files_same_size

def are_files_duplicates(directory):
    files_dict = get_files_count(directory)
    return [val for val in files_dict.values() if len(val) > 1]


if __name__ == '__main__':
    directory = input("Input directory: ")
    duplicates = are_files_duplicates(directory)
    if duplicates:
        print('This directory contain duplicated files:')
        for pair in duplicates:
            print(pair)
