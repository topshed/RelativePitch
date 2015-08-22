import pianohat # import libraries we need
import pygame
import time, random

pygame.mixer.pre_init(44100, -16, 1, 512) #Configure pygame sound
pygame.mixer.init() #Initialise pygame mixer
pygame.mixer.set_num_channels(16)
pianohat.auto_leds(True) # LEDs light whne keys pressed
# A dictionary mapping sounds and notes onto keys
NOTES = {'0':['C','./sounds/piano/39172__jobro__piano-ff-025.wav'], # C
  '1': ['C Sharp', './sounds/piano/39173__jobro__piano-ff-026.wav'], # C sharp
  '2':['D','./sounds/piano/39174__jobro__piano-ff-027.wav'], # D
  '3':['D Sharp','./sounds/piano/39175__jobro__piano-ff-028.wav'], # D sharp
  '4':['E','./sounds/piano/39176__jobro__piano-ff-029.wav'], # E
  '5':['F','./sounds/piano/39177__jobro__piano-ff-030.wav'], # F
  '6':['F Sharp','./sounds/piano/39178__jobro__piano-ff-031.wav'], # F sharp
  '7':['G','./sounds/piano/39179__jobro__piano-ff-032.wav'], # G
  '8':['G Sharp','./sounds/piano/39180__jobro__piano-ff-033.wav'], # G sharp
  '9':['A','./sounds/piano/39181__jobro__piano-ff-034.wav'], # A
  '10':['A Sharp','./sounds/piano/39182__jobro__piano-ff-035.wav'], # A sharp
  '11':['B','./sounds/piano/39183__jobro__piano-ff-036.wav'], # B
  '12':['C','./sounds/piano/39184__jobro__piano-ff-037.wav'] # C
}

def handle_note(channel, pressed): # handler for key presses
    global note
    global correct
    if channel < 13 and pressed: # Only for note keys
        if str(channel) == note: # Did the player get it right?
          print('correct, it was a ' + str(NOTES[note][0]) )
          pianohat.auto_leds(False)
          for x in range(16): # Flash all the lights to celebrate
            pianohat.set_led(x, True)
          time.sleep(0.05)
          for x in range(16): # Them turn them off
            pianohat.set_led(x,False)
          pianohat.auto_leds(True)
          correct = True
        else:
        	print('wrong, try again')

def play(note): # Play a note from the dictionary
	pygame.mixer.Sound(NOTES[note][1]).play(loops=0)
	time.sleep(1)

pianohat.on_note(handle_note) # Set keys to use our handler

while True:
  print('Here comes a C')
  time.sleep(1)
  play('0') # Play a C
  time.sleep(2)
  correct = False
  print('Now identify this note')
  time.sleep(2)
  note = random.choice(list(NOTES)) # Pick a random note
  play(note)
  print('press the key for the note you heard')
  count = 6 # Set countdown timer
  while count > 0 and correct == False:
    time.sleep(1)
    print(str(count) + ' Seconds remaining')
    count -=1
  if not correct: # If they didn't get it right, tell them the answer
    print("time's up, it was a " + str(NOTES[note][0]))
