def caesar():
    def greeting():
        print('                **    **  ********  **        **            **      ')
        print("               **    **  ********  **        **         **     **   ")
        print("              ********  **        **        **         **      **  ")
        print("             ********  ********  **        **         **      **  ")
        print("            **    **  **        **        **         **      **  ")
        print("           **    **  ********  ********  ********    **    **   ")
        print("          **    **  ********  ********  ********       **      ")
        print("Приветствую вас в шифраторе и дешифраторе алгоритма Цезаря")
        questions()

    def right_ru(shift, text, letters, letters_up):
        for i in range(len(text)):
            if text[i] in letters_up:
                num = letters_up.find(text[i]) + shift
                if num > len(letters_up) - 1:
                    num = 0 + (shift - (len(letters_up) - letters_up.find(text[i])))
                if i != len(text) - 1:
                    text = text[:i] + letters_up[num] + text[i + 1:]
                    continue
                else:
                    text = text[:i] + letters_up[num] + text[i + 1:]
                    continue
            elif text[i] in letters:
                num = letters.find(text[i]) + shift
                if num > len(letters) - 1:
                    num = 0 + (shift - (len(letters) - letters.find(text[i])))
                if i != len(text) - 1:
                    text = text[:i] + letters[num] + text[i + 1:]
                    continue
                else:
                    text = text[:i] + letters[num]
                    continue
        return text

    def right_eng(shift, text):
        for i in range(len(text)):
            num = ord(text[i]) + shift
            if text[i].isupper() and text[i].isalpha():
                if num > 90:
                    num = 65 + (shift - (91 - ord(text[i])))
                if i != len(text) - 1:
                    text = text[:i] + chr(num) + text[i + 1:]
                    continue
                else:
                    text = text[:i] + chr(num)
                    continue
            elif text[i].islower() and text[i].isalpha():
                if num > 122:
                    num = 97 + (shift - (123 - ord(text[i])))
                if i != len(text) - 1:
                    text = text[:i] + chr(num) + text[i + 1:]
                    continue
                else:
                    text = text[:i] + chr(num)
                    continue
        return text

    def left_ru(shift, text, letters, letters_up):
        for i in range(len(text)):
            if text[i] in letters_up:
                num = letters_up.find(text[i]) - shift
                if num > len(letters_up) - 1:
                    num = len(letters_up) - (shift - (letters_up.index(text[i]) - 0))
                if i != len(text) - 1:
                    text = text[:i] + letters_up[num] + text[i + 1:]
                    continue
                else:
                    text = text[:i] + letters_up[num]
                    continue
            elif text[i] in letters:
                num = letters.find(text[i]) - shift
                if num > len(letters) - 1:
                    num = len(letters) - (shift - (letters.index(text[i]) - 0))
                if i != len(text) - 1:
                    text = text[:i] + letters[num] + text[i + 1:]
                    continue
                else:
                    text = text[:i] + letters[num]
                    continue
        return text

    def left_eng(shift, text):
        for i in range(len(text)):
            num = ord(text[i]) - shift
            if text[i].isupper() and text[i].isalpha():
                if num < 65:
                    num = 91 - (shift - (ord(text[i]) - 65))
                if i != len(text) - 1:
                    text = text[:i] + chr(num) + text[i + 1:]
                    continue
                else:
                    text = text[:i] + chr(num)
                    continue
            elif text[i].islower() and text[i].isalpha():
                if num < 97:
                    num = 123 - (shift - (ord(text[i]) - 97))
                if i != len(text) - 1:
                    text = text[:i] + chr(num) + text[i + 1:]
                    continue
                else:
                    text = text[:i] + chr(num)
                    continue
        return text

    def correct_word_ru(word):
        import pymorphy2
        morph = pymorphy2.MorphAnalyzer()
        if len(morph.parse(word)) > 0:
            return True
        else:
            return False

    def correct_word_eng(word):
        import enchant
        if enchant.Dict("en_US").check(word):
            return True
        else:
            return False

    def is_valid_(s):
        if str(s).isdigit():
            return True
        return False

    def questions():
        global letters, letters_up
        while True:
            choiсe = input('Вы хотите шифровать или расшифровать послание? Введите "шифр" или "расшифр" ').strip().lower()
            if choiсe == 'шифр':
                while True:
                    choice_direct = input('Шифруем со сдвигом вправо или влево? Введите "вправо" или "влево" ').strip().lower()
                    if choice_direct == 'вправо':
                        while True:
                            lan = input('На каком языке? Введите "ru" или "eng" ').strip().lower()
                            if lan.lower() == 'ru':
                                while True:
                                    choice = input('Будем учитывать букву Ё ? Введите "да" или "нет" ').strip().lower()
                                    if choice == 'да':
                                        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                        letters_up = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                                        shift = input('Введите шаг сдвига от 1 до 33 ').strip()
                                        while True:
                                            if is_valid_(shift) and int(shift) < 33:
                                                shift = int(shift)
                                                break
                                            else:
                                                print('А может быть все-таки введём целое число? ')
                                                continue
                                        break
                                    elif choice == 'нет':
                                        letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
                                        letters_up = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                                        shift = input('Введите шаг сдвига от 1 до 32 ').strip()
                                        while True:
                                            if is_valid_(shift) and int(shift) < 32:
                                                shift = int(shift)
                                                break
                                            else:
                                                print('А может быть все-таки введём целое число? ')
                                                continue
                                        break
                                    else:
                                        print('Я не понимаю ')
                                        continue
                                while True:
                                    text = input('Введите текст для шифровки ').strip()
                                    if is_valid_(shift):
                                        break
                                    else:
                                        print('А может быть все-таки введем текст для шифровки? ')
                                        continue
                                print(right_ru(shift, text, letters, letters_up))
                                break
                            elif lan.lower() == 'eng':
                                while True:
                                    shift = input('Введите шаг сдвига от 1 до 26 ').strip()
                                    if is_valid_(shift) and int(shift) < 26:
                                        shift = int(shift)
                                        break
                                    else:
                                        print('А может быть все-таки введём целое число? ')
                                        continue
                                while True:
                                    text = input('Введите текст для шифровки ').strip()
                                    if is_valid_(shift):
                                        break
                                    else:
                                        print('А может быть все-таки введем текст для шифровки? ')
                                        continue
                                print(right_eng(shift, text))
                                break
                            else:
                                print('Я не понимаю  ')
                                continue
                        break
                    elif choice_direct == 'влево':
                        while True:
                            lan = input('На каком языке? Введите "ru" или "eng" ').strip().lower()
                            if lan.lower() == 'ru':
                                while True:
                                    choice = input('Будем учитывать букву Ё ? Введите "да" или "нет" ').strip().lower()
                                    if choice == 'да':
                                        letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                        letters_up = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                                        shift = input('Введите шаг сдвига от 1 до 33 ').strip()
                                        while True:
                                            if is_valid_(shift) and int(shift) < 33:
                                                shift = int(shift)
                                                break
                                            else:
                                                print('А может быть все-таки введём целое число? ')
                                                continue
                                        break
                                    elif choice == 'нет':
                                        letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
                                        letters_up = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                                        shift = input('Введите шаг сдвига от 1 до 32 ').strip()
                                        while True:
                                            if is_valid_(shift) and int(shift) < 32:
                                                shift = int(shift)
                                                break
                                            else:
                                                print('А может быть все-таки введём целое число? ')
                                                continue
                                        break
                                    else:
                                        print('Я не понимаю ')
                                        continue
                                while True:
                                    text = input('Введите текст для шифровки ').strip()
                                    if is_valid_(shift):
                                        break
                                    else:
                                        print('А может быть все-таки введем текст для шифровки? ')
                                        continue
                                print(left_ru(shift, text, letters, letters_up))
                                continue_code()
                                break
                            elif lan.lower() == 'eng':
                                while True:
                                    shift = input('Введите шаг сдвига от 1 до 26 ').strip()
                                    if is_valid_(shift) and int(shift) < 26:
                                        shift = int(shift)
                                        break
                                    else:
                                        print('А может быть все-таки введём целое число? ')
                                        continue
                                while True:
                                    text = input('Введите текст для шифровки ').strip()
                                    if is_valid_(shift):
                                        break
                                    else:
                                        print('А может быть все-таки введем текст для шифровки? ')
                                        continue
                                print(left_eng(shift, text))
                                break
                            else:
                                print('Я не понимаю  ')
                                continue
                        break
                    else:
                        print('Я не понимаю ')
                        continue
                break
            elif choiсe == 'расшифр':
                A = []
                while True:
                    lan = input('На каком языке? Введите "ru" или "eng" ').strip().lower()
                    if lan.lower() == 'ru':
                        print('К сожалению я не могу расшифровать текст на русском языке ')
                        '''while True:
                            choice = input('Будем учитывать букву Ё ? Введите "да" или "нет" ').strip().lower()
                            if choice == 'да':
                                letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
                                letters_up = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                                break
                            elif choice == 'нет':
                                letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
                                letters_up = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                                break
                            else:
                                print('Я не понимаю ')
                                continue
                        while True:
                            text = input('Введите текст для шифровки ').strip()
                            if text == '':
                                print('Я не понимаю ')
                                continue
                            else:
                                break
                        for i in range(1, 33):
                            A.append(right_ru(i, text, letters, letters_up).split())
                            A.append(left_ru(i, text, letters, letters_up).split())
                        print(A)
                        decoding = 'Это послание бессмысленно '
                        for i in range(len(A)):
                            cnt = 0
                            for j in A[i]:
                                i_ = j
                                for q in A[i]:
                                    if not q.isalpha():
                                        i_ = i_.replace(q, '')
                                if i_ == '' or correct_word_ru(i_):
                                    cnt += 1
                            if cnt == len(A[i]):
                                decoding = ' '.join(A[i])
                                break
                        print(decoding)
                        break'''
                    elif lan.lower() == 'eng':
                        while True:
                            text = input('Введите текст для шифровки ').strip()
                            if text == '':
                                print('Я не понимаю ')
                                continue
                            else:
                                break
                        for i in range(1, 26):
                            A.append(right_eng(i, text).split())
                            A.append(left_eng(i, text).split())
                        decoding = 'Это послание бессмысленно '
                        for i in range(len(A)):
                            cnt = 0
                            for j in A[i]:
                                i_ = j
                                for q in j:
                                    if not q.isalpha():
                                        i_ = i_.replace(q, '')
                                if i_ == '' or correct_word_eng(i_):
                                    cnt += 1
                            if cnt == len(A[i]):
                                decoding = ' '.join(A[i])
                                break
                        print(decoding)
                        break
                    else:
                        print('Я не понимаю  ')
                        continue
            else:
                print('Я не понимаю ')
                continue
            continue_code()
            break

    def continue_code():
        while True:
            restart = input('Хотите ещё раз воспользоваться нашей программой? (Введите "да" или "нет"): ')
            if restart.strip().lower() == 'да':
                questions()
            elif restart.strip().lower() == 'нет':
                print('Возвращайся если ещё понадобится что-нибудь зашифровать или расшифровать!')
                print('Пока!')
                break
            else:
                print('Я не понимаю ')
                continue

    greeting()


caesar()
