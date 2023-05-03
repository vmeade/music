#!/usr/bin/python3
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
#'TR-6S:TR-6S MIDI 1 20:0', 'TR-6S:TR-6S MIDI 2 20:1'
drums = mido.open_output('TR-6S:TR-6S MIDI 2 24:1')
keys = mido.open_output('minilogue xd:minilogue xd MIDI 2 20:1')
mid = mido.MidiFile(str(sys.argv[1]))

for msg in mid.play():
	if msg.type == 'program_change':
		continue
	if msg.type == 'control_change':
		continue

	print (msg)
	
	if msg.channel == 9:
		drums.send(msg)
	keys.send(msg)

drums.close()
keys.close()
