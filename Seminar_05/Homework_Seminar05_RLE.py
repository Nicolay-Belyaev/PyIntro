# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# При кодировании (упаковке, сжатии) строка одинаковых символов, составляющих серию, заменяется строкой,
# содержащей сам повторяющийся символ и количество его повторов
# так-то RLE требует минимальной оптимизации, иначе можно получить на выходе строку длиннее строки входа.
# но формулировка задачи этого не требует, а следующий семинар уже завтра =)

# уже не придумал, что делать, если шифровать надо строку, содержащую цифры.
# ну и точно не все крайние вводы обработал. long story short - оно живое, но по-хорошему надо рефакторить.

class rle(object):
    """Предоставляет доступ к функциям кодировки/декодировки строки по неоптимизированному алгоритму RLE"""

    def code(input_path: str, output_path: str):
        """input_path - путь до файла, содержащего строку, которую надо зашифровать. output_path - пусть до файла
        с результатом. Если файла нет, файл создается функцией."""
        with open(f'{input_path}', 'r') as ind:
            incoming_data = ind.read()

        outcoming_data = []
        symbol_counter = 1
        for i in range(len(incoming_data) - 1, -1, -1):
            current_symbol = incoming_data[i]
            if current_symbol == incoming_data[i-1]:
                symbol_counter += 1
            else:
                outcoming_data.append(str(current_symbol)+str(symbol_counter))
                symbol_counter = 1
                current_symbol = incoming_data[i-1]
        # если у нас вся строка состоит из одного и того же символа
        if symbol_counter > 1 and len(outcoming_data) == 0:
            outcoming_data.append(str(current_symbol)+str(symbol_counter - 1))
        outcoming_data.reverse()
        result = ''.join(outcoming_data)

        with open(f'{output_path}', 'w') as ot:
            ot.write(result)

    def decode(input_path: str, output_path: str):
        """input_path - путь до файла, содержащего строку, которую надо расшифровать. output_path - пусть до файла
            с результатом. Если файла нет, файл создается функцией."""
        with open(f'{input_path}', 'r') as ind:
            incoming_data = ind.read()
            list_incoming_data = [i for i in incoming_data]

            outcoming_data = []
            current_literal = incoming_data[0]
            current_number = ''
            for i in range(1, len(list_incoming_data)):
                if list_incoming_data[i].isdigit():
                    current_number += list_incoming_data[i]
                elif list_incoming_data[i].isalpha():
                    outcoming_data.append((current_literal) * int(current_number))
                    current_literal = list_incoming_data[i]
                    current_number = ''
                # чисто костыль. но что бы сделать фишечку с проходом по массиву в обратку как в шифровании,
                # придется попарно развернуть элементы. это больше проблем, чем подпорочку из if поставить.
                # есть у меня подозрения, что я не оптимально RLE реализую, ага.
                if i == len(list_incoming_data) - 1:
                    outcoming_data.append((current_literal) * int(current_number))

            result = "".join(outcoming_data)
        with open(f'{output_path}', 'w') as ot:
            ot.write(result)

# primitive_rle_сode('input.txt', 'coded.txt')
# primitive_rle_decode('coded.txt', 'decoded.txt')


rle.code('input.txt', 'coded.txt')
rle.decode('coded.txt', 'decoded.txt')