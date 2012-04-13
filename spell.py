# pygame help from http://code.activestate.com/recipes/521884-play-sound-files-with-pygame-in-a-cross-platform-m/ (for playing sounds)
# shuffle help from http://stackoverflow.com/a/976921/868718

import sys
import pygame               # This library required for playing audio files
from random import shuffle  # These two functions for shuffling the word list
from random import random

FREQ = 44100    # same as audio CD
BITSIZE = -16   # unsigned 16 bit
CHANNELS = 2    # 1 == mono, 2 == stereo
BUFFER = 1024   # audio buffer size in no. of samples
FRAMERATE = 30  # This has something to do with how often to check if sound is done?

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
    """For starters, I just hacked the main function from the above pygame sound tutorial.  I know this should be split into functions, but for now it works. I also don't understand the error checking and I don't think it works
    """
    
    try:
        pygame.mixer.init(FREQ, BITSIZE, CHANNELS, BUFFER)
    except pygame.error, exc:
        print >>sys.stderr, "Could not initialize sound system: %s" % exc
        return 1
    
    wordfile = open("2012bee.txt") # for now this file is hard-coded.  Should be sent in as an argument

    wordfilelist = wordfile.readlines()
    shuffle(wordfilelist, random)
    
    # print wordfilelist    
    i = 0
    for sfiles in wordfilelist:
        i += 1
        print "\n\n\nword %d out of %d" % (i, len(wordfilelist))
        while True:
            correct, this, that = sfiles.partition('.') # I am using this and that to store the parts of strings i don't want
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
# this is from the pygame sound tutorial. I don't really know what it does.    
if __name__ == '__main__':         
    sys.exit(main(sys.argv[1:]))
    
       

