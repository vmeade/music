#!/usr/bin/python
import mido
import sys
#msg = mido.Message('note_on', note=60)
#msg.type
#msg.note
#msg.bytes()


mid = mido.MidiFile(str(sys.argv[1]))
try:
   instr =  sys.argv[2] 
except IndexError:
    instr = 1
port = mido.open_output('CASIO USB-MIDI:CASIO USB-MIDI MIDI 1 20:0')
port2 = mido.open_output('minilogue xd:minilogue xd MIDI 2 24:1')

for msg in mid.play():
    msg.channel=0
    if msg.type == 'program_change':
            msg.program=int(instr)-1
    if msg.type == 'control_change':
        continue
    print (msg)
    port.send(msg)
    port2.send(msg)

port.close()

