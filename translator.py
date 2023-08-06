from googletrans import Translator


filename = "02 - Installation.txt"
with open(filename, 'r') as f:
    text = f.read()

translator = Translator()
translated = translator.translate(text, src='en', dest='ru')

new_filename = filename.split('.')[0] + '_ru.' + filename.split('.')[1]
with open(new_filename, 'w') as f:
    f.write(translated)

## print(f'Переведенный текст сохранен в файл {new_filename}')