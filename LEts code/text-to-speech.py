from gtts import gTTS
from playsound import playsound

language = 'de'
tts = gTTS(text='Jetzt der Ultimative Test. Ich werde es zu Hause mit meiner Stimme versuchen.',
           lang=language,
           slow=False)

tts.save('../../Desktop/tests/Audios/test.mp3')
playsound('../Audios/test.mp3')