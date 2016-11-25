import os
from os.path import join, getsize

def obj_into_lists(file_path):
    roots = []
    names = []
    sizes = []
    for root, dirs, files in os.walk(file_path):
        for file in files:
            roots.append(root)
            names.append(file)
            sizes.append(getsize(join(root, file)))
    return roots, names, sizes

def are_files_duplicates(roots, names, sizes):
    overlooked = []
    duplicates = []
    for i in range(len(names)):
        for j in range(len(names)):
            if (i != j) and (overlooked.count(i) == 0) and (overlooked.count(j) == 0) and (names[i] == names[j]) and (sizes[i] == sizes[j]):
                overlooked.append(j)
                overlooked.append(i)
                duplicates.append([j, i])
    return duplicates

def print_duplicates(items):
    for item in items:
        print('Файл с именем %s, размером %dкб, находящийся в директории %s' % (names[item[0]], sizes[item[0]], join(roots[item[0]], names[item[0]])))
        print('является дубликатом файла с именем %s, размером %dкб, находящимся в директории %s' % (names[item[1]], sizes[item[1]], join(roots[item[1]], names[item[1]])))
        print('----------------------------------------------------------------------------------------------')

if __name__ == '__main__':
    file_path = input('Введите путь до директории, чтобы найти там дубликаты: ')
    lists = obj_into_lists(file_path)
    roots = lists[0]
    names = lists[1]
    sizes = lists[2]
    duplicates = are_files_duplicates(roots, names, sizes)
    print_duplicates(duplicates)
