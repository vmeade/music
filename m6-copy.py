#!/usr/bin/python
import mido
from mido import Message, MidiFile, MidiTrack
import sys

mid = mido.MidiFile(str(sys.argv[1]))

mid2 = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

mid.track.append(msg)
