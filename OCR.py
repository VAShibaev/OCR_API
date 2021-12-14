import easyocr

from IOUtils import read_params

# Считывание параметров из json-файла
params = read_params('params.json')

# Создание Reader для дальнейшего распознавания текста на изображениях
reader = easyocr.Reader(lang_list=params['languages'],  # Список языков, которые необходимо распознать на изображении
                        gpu=params['gpu'])              # На каком устройстве считать модель


"""
Распознавание текста на изображении
На выходе - строка со всем тектом, который удалось распознать на переданном изображении
"""
def text_recognition(image: bytes):
    try:
        # Распознание текста
        result = reader.readtext(image,
                                 paragraph=params['paragraph'])  # Нужно ли объединять текст в параграфы
    except:
        return None
    
    result_strings = []
    for box in result:
        result_strings.append(box[1])

    # Объединяем список распознанных фраз в одну строку, используя указанный разделитель
    return params['separator'].join(result_strings)