#!/usr/bin/python
import time 
import mido
import sys
#msg = mido.Message('note_on', note=60)
#msg.type
#msg.note
#msg.bytes()
time.sleep(5)
port = mido.open_output('minilogue xd:minilogue xd MIDI 2 20:1')
mid = mido.MidiFile('' + str(sys.argv[1]))
#channel=sys.argv[2]
for msg in mid.play():
    port.send(msg)

