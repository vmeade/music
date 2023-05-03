#!/usr/bin/python
import mido
import sys

while True:
    try:
        with mido.open_input('DigiTech RP500:DigiTech RP500 MIDI 1 20:0') as inport:
            for msg in inport:
                print(msg)
    except KeyboardInterrupt:
        inport.close()
        sys.exit()

