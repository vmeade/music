#!/usr/bin/python
import mido
import sys
#msg = mido.Message('note_on', note=60)
#msg.type
#msg.note
#msg.bytes()

try:
   instr =  sys.argv[2] 
except IndexError:
    instr = 1

port = mido.open_output('minilogue xd:minilogue xd MIDI 2 20:1')
mid = mido.MidiFile(str(sys.argv[1]))


for msg in mid.play():
#    msg.channel=0
    if msg.type == 'program_change':
            msg.program=int(instr)-1
    print (msg)
    port.send(msg)

