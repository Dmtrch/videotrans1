import os
import speech_recognition as sr
from moviepy.editor import *


def extract_audio_from_video(video_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio_path = os.path.splitext(video_path)[0] + ".wav"
    audio.write_audiofile(audio_path)
    return audio_path


def speech_to_text(audio_path):
    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 300
    recognizer.dynamic_energy_threshold = False
    recognizer.dynamic_energy_adjustment_damping = 0.15
    recognizer.dynamic_energy_adjustment_ratio = 1.5
    recognizer.pause_threshold = 0.8

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)  # Поддерживаемый язык - английский ("en")
        return text
    except sr.UnknownValueError:
        return "Не удалось распознать речь"
    except sr.RequestError as e:
        return f"Ошибка сервиса распознавания речи; {e}"


if __name__ == "__main__":
    video_file = "05 - Game Loop and Key Events.mp4"   ## input("Введите путь к видеофайлу: ")

    if not os.path.isfile(video_file):
        print("Указанный файл не существует.")
    elif not video_file.lower().endswith((".mp4", ".avi", ".mov")):
        print("Формат видеофайла не поддерживается.")
    else:
        audio_file = extract_audio_from_video(video_file)
        text_output = speech_to_text(audio_file)

        with open(os.path.splitext(video_file)[0] + ".txt", "w") as file:
            file.write(text_output)

