#!/usr/bin/python
import mido
import sys

while True:
    try:
        #with mido.open_input('minilogue xd:minilogue xd MIDI 2 20:1') as inport:
        with mido.open_input('minilogue xd:minilogue xd minilogue xd _ SOU 20:1') as inport:
            for msg in inport:
                if msg.type != "clock":
                    print(msg)
                    print(msg.type)
    except KeyboardInterrupt:
        inport.close()
        sys.exit()

