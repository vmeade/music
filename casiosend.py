#!/usr/bin/python
import mido
import sys
#msg = mido.Message('note_on', note=60)
#msg.type
#msg.note
#msg.bytes()


mid= MidiFile()
track = MidiTrack()
mid.tracks.append(track)



with mid.open_input('CASIO USB-MIDI:CASIO USB-MIDI MIDI 1 20:0') as input:
    for msg in input:
        if sys.stdin.read() == 'q':
            break
        track.append(msg)

mid.save('new_track.mid')
port.close()

