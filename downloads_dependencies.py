"""
Предварительное скачивание библиотекой easyocr
всех необходимых моделей при сборке docker-образа
"""
import easyocr

from IOUtils import read_params

# Считывание параметров из json-файла
params = read_params('params.json')

# Создание Reader для дальнейшего распознавания текста на изображениях
reader = easyocr.Reader(lang_list=params['languages'],    # Список языков, которые необходимо распознать на изображении
                        gpu=params['gpu'])                # На каком устройстве считать модель
