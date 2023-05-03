#!/usr/bin/python
import mido
from mido import Message, MidiFile, MidiTrack
import sys

mid = mido.MidiFile(str(sys.argv[1]))

track = MidiTrack()
mid.tracks.append(track)

for msg in mid.play():
    track.append(msg)

mid.save('new_avril.mid')
