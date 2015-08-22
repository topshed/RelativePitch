import pianohat
import pygame
import signal

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(16)
NOTES = {0:['Sound1','./mysound.wav'], 
  		 2: ['Sound2', './mysound2.wav']}

def handle_note(channel, pressed):
	if channel == 0 or channel == 2:
                pygame.mixer.Sound(NOTES[channel][1]).play(loops=0)

pianohat.on_note(handle_note)
signal.pause()
