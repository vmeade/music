#!/usr/bin/python
import mido
import sys
#msg = mido.Message('note_on', note=60)
#msg.type
#msg.note
#msg.bytes()


port = mido.open_output('DigiTech RP500:DigiTech RP500 MIDI 1 20:0')
mid = mido.MidiFile(str(sys.argv[1]))


for msg in mid.play():
    msg.channel=0
    print (msg)
    port.send(msg)

port.close()

