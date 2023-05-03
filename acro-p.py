from mido import Message, MidiFile, MidiTrack
import os.path
from os import path

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(Message('program_change', program=12, time=0))
for x in range(32,64,4):
    t1 = x + x/4 
    t2 = t1 + 1000

    track.append(Message('note_on', note=x, velocity=64, time=int(t1)))
    track.append(Message('note_off', note=x, velocity=64, time=int(t2)))

i = 0
g = 1000
while i < g:
    file = str(i) + "acro-p.mid" 
    if path.exists(file):
        i+=1
    else:
        break

mid.save(file)
