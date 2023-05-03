import pygame
import pygame.midi

#instrument = 0

pygame.init()
pygame.midi.init()

#port = 2
#midiOutput = pygame.midi.Output(port, 0)
#imidiOutput.set_instrument(instrument)
file = "music.mid"
pygame.mixer.music.load(file)
pygame.mixer.music.play()

