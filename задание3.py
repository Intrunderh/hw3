def scrabble(word):
    eng_1 = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
    eng_2 = dict.fromkeys(['D', 'G'], 2)
    eng_3 = dict.fromkeys(['B', 'C', 'M', 'P'], 3)
    eng_4 = dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4)
    eng_5 = dict.fromkeys(['K'], 5)
    eng_8 = dict.fromkeys(['J', 'X'], 8)
    eng_10 = dict.fromkeys(['Q', 'Z'], 10)
    dict_eng = eng_1 | eng_2 | eng_3 | eng_4 | eng_5 | eng_8 | eng_10

    rus_1 = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
    rus_2 = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
    rus_3 = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
    rus_4 = dict.fromkeys(['Й', 'Ы'], 4)
    rus_5 = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
    rus_8 = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
    rus_10 = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)
    dict_rus = rus_1 | rus_2 | rus_3 | rus_4 | rus_5 | rus_8 | rus_10

    list_scr = list(word.upper())
    score = 0
    if list_scr[0] in list(dict_rus):
        for item in list_scr:
            score += int(dict_rus.get(item))
        return score
    for item in list_scr:
            score += int(dict_eng.get(item))
    return score

scrabble_word = input('Введите слово для игры: ')
print(scrabble(scrabble_word))