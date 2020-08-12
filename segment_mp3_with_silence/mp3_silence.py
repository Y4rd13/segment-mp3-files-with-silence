from pydub import AudioSegment
from os import getcwd
import glob

# audios should be in the same folder
cwd = (getcwd()).replace(chr(92), '/')
MP3_FILES = glob.glob(pathname=f'{cwd}/*.mp3', recursive=True)
silence = AudioSegment.silent(duration=15000)
count = 0
for n, mp3_file in enumerate(MP3_FILES):
    mp3_file = mp3_file.replace(chr(92), '/')
    print(n, mp3_file)
    count += 1
    audio1 = AudioSegment.from_mp3(mp3_file)
    res = (audio1 + silence)
    res.export(f'{cwd}/{str(count)}result.mp3', format='mp3')