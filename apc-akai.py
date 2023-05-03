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

pitch=0
mid = mido.MidiFile(str(sys.argv[1]))

with mido.open_input('Akai APC40:Akai APC40 MIDI 1 20:0') as inport:
    for msg in inport:
        if msg.channel == 0 and msg.note == 53 and msg.type=='note_on':
            pitch=pitch+1
            print (msg)
            print(pitch)
        if msg.channel == 0 and msg.note == 54 and msg.type=='note_on':
            pitch=pitch-1
            print (msg)
            print(pitch)
    #msg2.note=msg2.note+pitch
for msg2 in mid.play():
    print(msg2.note)

#for msg in mid.play():
#    msg.channel=0
#    if msg.type == 'program_change':
#            msg.program=int(instr)-1
#    if msg.type == 'control_change':
#        continue
#    print (msg)
#    port.send(msg)

