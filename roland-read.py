#!/usr/bin/python
import mido
import sys
#msg = mido.Message('note_on', note=60)
#msg.type
#msg.note
#msg.bytes()

#try:
#   instr =  sys.argv[2] 
#except IndexError:
#    instr = 1


# mido.open_output('TR-6S:TRS-6S MIDI 1 20:0')
# TR-6S:TR-6S MIDI 1 20:0', 'TR-6S:TR-6S MIDI 2 20:1'
with mido.open_input('TR-6S:TR-6S MIDI 1 20:0') as inport:
    for msg in inport:
            print (msg)

#for msg in mid.play():
#    msg.channel=0
#    if msg.type == 'program_change':
#            msg.program=int(instr)-1
#    if msg.type == 'control_change':
#        continue
#    print (msg)
#    port.send(msg)

