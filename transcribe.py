import whisper
import sys
import os

# Загружаем модель
model = whisper.load_model("base", device="cuda")

# Получаем путь к файлу
file_path = sys.argv[1] if len(sys.argv) > 1 else "audio.m4a"

# Распознаем
result = model.transcribe(file_path, language="ru")

# Формируем имя текстового файла
base_name = os.path.splitext(os.path.basename(file_path))[0]
output_path = f"{base_name}.txt"

# Сохраняем результат
with open(output_path, "w", encoding="utf-8") as f:
    f.write(result["text"])

print(f"\n✅ Готово! Текст сохранён в файл: {output_path}")