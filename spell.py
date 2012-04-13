import sys
import pygame
from random import shuffle
from random import random

FREQ = 44100    # same as audio CD
BITSIZE = -16   # unsigned 16 bit
CHANNELS = 2    # 1 == mono, 2 == stereo
BUFFER = 1024   # audio buffer size in no. of samples
FRAMERATE = 30
HH = 3

def playsound(soundfile):
    """Play sound through default mixer channel in blocking manner.
    
    This will load the whole sound into memory before playback
    """
    
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        clock.tick(FRAMERATE)

def main(args):

    try:
        pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
    except pygame.error, exc:
        print >>sys.stderr, "Could not initialize sound system: %s" % exc
        return 1
    
    wordfile = open("2012bee.txt")

    wordfilelist = wordfile.readlines()
    shuffle(wordfilelist, random)
    
    # print wordfilelist    
    i = 0
    for sfiles in wordfilelist:
        i += 1
        print "\n\n\nword %d out of %d" % (i, len(wordfilelist))
        while True:
            correct, this, that = sfiles.partition('.')
            soundfile, this, that = sfiles.partition('\n')
            # print "correct is %s" % correct
            # print soundfile
            # print locals()
            
            try:
                # playsound("pleasespell.ogg")
                playsound(soundfile)
                # playsound("chute.ogg")
            except pygame.error, exc:
                print >>sys.stderr, "Could not play sound file"
                print exc
                # continue
            
            print "\ntype: 'repeat', 'show', 'exit', or the word"
            answer = raw_input("type the word here> ")
            
            if answer == correct:
                print "Correct!"
                break
            elif answer == "repeat":
                print "does this repeat?"
            elif answer == "show":
                print "here's how to spell it: %s" % correct
                break
            elif answer == "exit":
                exit()
            else:
                print "Wrong!  Here's how to spell it: %s" % correct

        
    return 0
    
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
    
       

