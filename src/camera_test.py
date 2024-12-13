
import cv2
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
#gstream

app = FastAPI()

# Инициализация камеры
camera = cv2.VideoCapture(0)  # Используем встроенную веб-камеру
camera.set(cv2.CAP_PROP_FPS, 20)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

templates = Jinja2Templates(directory="templates")  # Убедитесь, что папка 'templates' существует

# Функция для захвата кадров с камеры и их преобразования в поток
def gen_frames():
    while True:
        success, frame = camera.read()  # Читаем кадр с камеры
        if not success:
            break
        else:
            # Преобразуем кадр в формат JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            if not ret:
                print(ret)
            frame = buffer.tobytes()
            # Отправляем кадры как поток
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Маршрут для главной страницы
@app.get('/')
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Маршрут для видеопотока
@app.get('/video_feed')
def video_feed():
    return StreamingResponse(gen_frames(), media_type='multipart/x-mixed-replace; boundary=frame')

# Запуск сервера
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    