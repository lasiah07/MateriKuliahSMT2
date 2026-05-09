import gtts
from playsound import playsound

# teks yang mau diubah jadi suara
text = "Halo, selamat datang di kelas 2A Informatika"

# ubah teks jadi suara
tts = gtts.gTTS(text=text, lang='id')

# simpan jadi file mp3
tts.save("suara.mp3")

# putar suaranya
playsound("suara.mp3")