#!/usr/bin/python
import mido
import sys
import os
#msg = mido.Message('note_on', note=60)
#msg.type
#msg.note
#msg.bytes()

#try:
#   instr =  sys.argv[2] 
#except IndexError:
#    instr = 1
kick = "~/wvin/software/apc/musicradar-drum-samples/Drum\ Kits/Kit\ 4\ -\ Electro/CYCdh_ElecK01-Kick01.wav"
snare = "~/wvin/software/apc/musicradar-drum-samples/Drum\ Kits/Kit\ 4\ -\ Electro/CYCdh_ElecK01-Snr01.wav"
with mido.open_input('Akai APC40:Akai APC40 MIDI 1 20:0') as inport:
	for msg in inport:
		if msg.note == 53 and msg.type == 'note_on' and msg.channel == 0:
			os.system("aplay " + kick)
			print(msg)
			
		if msg.note == 53 and msg.type == 'note_on' and msg.channel ==1:
			os.system("aplay " + snare)
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

