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

with mido.open_input('Akai APC40:Akai APC40 MIDI 1 20:0') as inport:
	for msg in inport:
		print(msg)
#mid = mido.MidiFile(str(sys.argv[1]))


#for msg in mid.play():
#    msg.channel=0
#    if msg.type == 'program_change':
#            msg.program=int(instr)-1
#    if msg.type == 'control_change':
#        continue
#    print (msg)
#    port.send(msg)

