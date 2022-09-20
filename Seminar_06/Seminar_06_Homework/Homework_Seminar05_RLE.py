# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# При кодировании (упаковке, сжатии) строка одинаковых символов, составляющих серию, заменяется строкой,
# содержащей сам повторяющийся символ и количество его повторов
# так-то RLE требует минимальной оптимизации, иначе можно получить на выходе строку длиннее строки входа.
# но формулировка задачи этого не требует, а следующий семинар уже завтра =)

# уже не придумал, что делать, если шифровать надо строку, содержащую цифры.
# ну и точно не все крайние вводы обработал. long story short - оно живое, но по-хорошему надо рефакторить.

import re


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
            if i == 0:
                outcoming_data.append(str(current_symbol) + str(symbol_counter))
            current_symbol = incoming_data[i]
            if current_symbol == incoming_data[i - 1]:
                symbol_counter += 1
            else:
                outcoming_data.append(str(current_symbol) + str(symbol_counter))
                symbol_counter = 1
                current_symbol = incoming_data[i - 1]
        # если у нас вся строка состоит из одного и того же символа
        if symbol_counter > 1 and len(outcoming_data) == 0:
            outcoming_data.append(str(current_symbol) + str(symbol_counter - 1))
        outcoming_data.reverse()
        result = ''.join(outcoming_data)

        with open(f'{output_path}', 'w') as ot:
            ot.write(result)

    def decode(input_path: str, output_path: str):
        """input_path - путь до файла, содержащего строку, которую надо расшифровать. output_path - пусть до файла
            с результатом. Если файла нет, файл создается функцией."""
        with open(f'{input_path}', 'r') as ind:
            incoming_data = ind.read()

            literals = list(filter(lambda x: x.isalpha(), incoming_data))
            coefficients = [int(s) for s in re.findall(r'-?\d+\.?\d*', incoming_data)]
            result = ''.join([literals[i] * coefficients[i] for i in range(len(literals))])

        with open(f'{output_path}', 'w') as ot:
            ot.write(result)


rle.code('input.txt', 'coded.txt')
rle.decode('coded.txt', 'decoded.txt')