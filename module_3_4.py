#Формируем требуемую функцию
def single_root_words(root_word, *other_words):
    same_words = []
    n_root_word = str(root_word).lower()
    for i in other_words:
        if (str(i).lower() in n_root_word) or (n_root_word in str(i).lower()):
            same_words.append(str(i))
    if same_words == []:
        print(f"Слов, содержащих или входящих в '{root_word}', не найдено...")
    else:
        print(f"Слова, содержащие или входящие в '{root_word}':")
    return same_words
#Вызовы функции
print(single_root_words('Disablement', 'Able', 'Mable', 'DiSABle', 'Bagel'))
print(single_root_words('rich', 'riCHiest', 'orichalcum', 'Cheers', 'RiChIeS'))
print(single_root_words('Housekeeping', 'Housekeep', 'KeeP', 'Housekeeper', 'Mousekeep'))
print(single_root_words('Village', 'Nile', 'Ageist', 'WiLL', 'Sauce', 'Century'))