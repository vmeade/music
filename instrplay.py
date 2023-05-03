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

port = mido.open_input('Midi Through:Midi Through Port-0 14:0')
mid = mido.MidiFile(str(sys.argv[1]))

for msg in mid.play():
    msg.program=int(instr)
    print (msg)
    port.send(msg)

port.close()
