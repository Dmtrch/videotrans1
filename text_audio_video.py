import moviepy.editor as mp
from gtts import gTTS

file_aud_out = "audio-ru.mp3"
# Читаем текст из текстового файла
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Генерируем аудио из текста с помощью gTTS
tts = gTTS(text=text, lang='ru')

tts.save(file_aud_out)

# Загружаем видео
video = mp.VideoFileClip('02 - Installation.mp4')

# Загружаем сгенерированный аудиофайл
audio = mp.AudioFileClip(file_aud_out)

# Заменяем аудио в видео на наш аудиофайл
final = video.set_audio(audio)

# Сохраняем результат
final.write_videofile('output.mp4')