import cv2
import speech_recognition as sr
import numpy as np
import tempfile
from os import path



# Загружаем видео
##cap = cv2.VideoCapture('02 - Installation.mp4')

# Извлекаем аудиодорожку
##audio_chunks = []
##while True:
##    ret, frame = cap.read()
 ##   if not ret:
##        break
##    audio_chunks.append(frame)

##audio = np.concatenate(audio_chunks, axis=0)

##audio_bytes = audio.tobytes()

# Записываем во временный WAV файл
##tmp_file = path.join(path.dirname(__file__), 'audio.wav')
##with open(tmp_file,"w") as f:
##    f.write(audio_bytes)
##np.save(tmp_file, audio)

# Инициализируем распознавание речи
##r = sr.Recognizer()

# Передаем аудио на распознавание
##with sr.AudioFile(tmp_file) as source:
##    audio_text = r.listen(source)

##try:
##    text = r.recognize_google(audio_text)
##    with open("output.txt", "w") as f:
##        f.write(text)
##except:
##    print("Не удалось распознать речь")