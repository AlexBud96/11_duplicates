import os
from os.path import join, getsize

def obj_into_lists(file_path):
    Roots = []
    Names = []
    Sizes = []
    for root, dirs, files in os.walk(file_path):
        for file in files:
            Roots.append(root)
            Names.append(file)
            Sizes.append(getsize(join(root, file)))
    return Roots, Names, Sizes

def are_files_duplicates(Roots, Names, Sizes):
    overlooked = []
    duplicates = []
    for i in range(len(Names)):
        for j in range(len(Names)):
            if (i != j) and (overlooked.count(i) == 0) and (overlooked.count(j) == 0) and (Names[i] == Names[j]) and (Sizes[i] == Sizes[j]):
                overlooked.append(j)
                overlooked.append(i)
                duplicates.append([j, i])
    return duplicates

def print_duplicates(items):
    for item in items:
        print('Файл с именем %s, размером %dкб, находящийся в директории %s' % (Names[item[0]], Sizes[item[0]], join(Roots[item[0]], Names[item[0]])))
        print('является дубликатом файла с именем %s, размером %dкб, находящимся в директории %s' % (Names[item[1]], Sizes[item[1]], join(Roots[item[1]], Names[item[1]])))
        print('----------------------------------------------------------------------------------------------')

if __name__ == '__main__':
    file_path = input('Введите путь до директории, чтобы найти там дубликаты: ')
    lists = obj_into_lists(file_path)
    Roots = lists[0]
    Names = lists[1]
    Sizes = lists[2]
    duplicates = are_files_duplicates(Roots, Names, Sizes)
    print_duplicates(duplicates)
