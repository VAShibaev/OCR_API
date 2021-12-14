from fastapi import (FastAPI, UploadFile, File)

from OCR import text_recognition

app = FastAPI()


@app.post('/text-recognition')
async def predict_image(file: UploadFile=File(...)):
    try:
        # Получение изображения от клиента
        image = await file.read()
    except Exception:
        # Если в ходе передачи изображения возникла ошибка, уведомляем клиента
        return {
            'Error': 1,
            'description': 'Error during getting image'
        }
    
    # Распознание текста
    text = text_recognition(image)
    if text is not None:
        return {'recognized_text': text}
    else:
        # Если в ходе распознания текста возникла ошибка, уведомляем клиента
        return {
            'Error': 2,
            'description': 'Error during OCR'
        }
