def thesaurus(name1, name2, name3, name4):
    names_list = [name1, name2, name3, name4]
    names_list.sort()
    dictionary = {}
    for name in names_list:
        if name[:1] in dictionary.keys():
            temp_var = dictionary.pop(name[:1])
            temp_var.append(name)
            dictionary.update({name[:1]: temp_var})
        else:
            dictionary[name[:1]] = [name]
    print(dictionary)


thesaurus("Иван", "Мария", "Петр", "Илья")
