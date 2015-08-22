import pianohat
import pygame
import signal

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

def handle_note(channel, pressed):
	if channel == 2:
		pygame.mixer.Sound('./mysound.wav').play(loops=0)

pianohat.on_note(handle_note)
signal.pause()
