import whisper

model = whisper.load_model("medium")
res = model.transcribe("C:/Users/YANNI/OneDrive - Schulen Stadt St. Gallen/Desktop/tests/Audios/Aufzeichnung.m4a")

print(res["text"])