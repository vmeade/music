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

xd = mido.open_output('minilogue xd:minilogue xd MIDI 2 20:1')
port = mido.open_output('CASIO USB-MIDI:CASIO USB-MIDI MIDI 1 24:0')
mid = mido.MidiFile(str(sys.argv[1]))
#xd.program=int(instr)-1

for msg in mid.play():
   # msg.channel=0
    if msg.type == 'control_change':
        continue
    print (msg)
    if msg.channel %2 ==1:
        port.send(msg)
    else:
        msg.channel=0
        if msg.type == 'program_change':
            xd.program=int(instr)-1
        xd.send(msg)

port.close()
xd.close()
