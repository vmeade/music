#!/usr/bin/python
import mido
import sys
#msg = mido.Message('note_on', note=60)
#msg.type
#msg.note
#msg.bytes()
port = mido.open_output('minilogue xd:minilogue xd MIDI 2 16:1')
mid = mido.MidiFile(str(sys.argv[1]))


for msg in mid.play():
    msg.channel=0
    if msg.type == 'program_change':
            msg.program=int(sys.argv[2])-1
    print (msg)
    port.send(msg)

