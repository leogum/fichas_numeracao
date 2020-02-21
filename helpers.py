# refaz a lista para tirar itens que estao repetidos> função futura
def clean_dup_list(list_dup_items):
    unique_list = list()
    for i in range(len(list_dup_items)):
        if list_dup_items[i] not in list_dup_items[i + 1:]:
            unique_list.append(list_dup_items[i])
    return unique_list
