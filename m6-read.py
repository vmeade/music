#!/usr/bin/python
import mido
import sys

port = mido.open_output('Midi Through:Midi Through Port-0 14:0')
mid = mido.MidiFile(str(sys.argv[1]))

#
#for msg in mid.play():
   # msg.channel=0
   # if msg.type == 'control_change':
   #     continue
#    print (msg)
#    port.send(msg)

for msg in mid.play():
    #if msg.type == 'control_change':
    #    print ("no control change")
    #else:
    print(msg)
    port.send(msg)

port.close()
