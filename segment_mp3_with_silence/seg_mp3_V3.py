from pydub import AudioSegment
import glob
import os

# PATH
cwd = (os.getcwd()).replace(chr(92), '/')
export_path = f'{cwd}/result.mp3'

MP3_FILES = sorted(glob.glob(f'{os.getcwd()}/*.mp3'),
                   key=lambda x: int(os.path.basename(x).split(' ')[0]))

# Audio variables
silence = AudioSegment.silent(duration=15000)
result = AudioSegment.empty()

# Main
for n, mp3_file in enumerate(MP3_FILES):
    mp3_file = mp3_file.replace(chr(92), '/')
    print(f'\t{n + 1} | {mp3_file}')
    audio = AudioSegment.from_mp3(mp3_file)
    result += audio + silence
    print(f'Merging {n + 1}')

result.export(export_path, format='mp3')
print('\ndone!')
