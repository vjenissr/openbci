#name of a file with words in format: every column for one group
RAW_WORDS_FILE='raw_words.csv'

#to-be-created-every-time file with experiment words with rows:
#group, word, fixation time
WORDS_FILE='words.csv'
#if true then it is assumed that there is word.csv file and itll be used
USE_EXISTING_WORDS_FILE = False

#how many repetitions of the experiment in a one session?
#used to generate WORDS_FILE file
REPS = 2
#dummy word for the experiment
#used to generate WORDS_FILE file
DUMMY_WORD='Drewno'
#after every target word there will be N dummy wordse
#where N is a random between 1 and DUMMY_WORD_MULT
#used to generate WORDS_FILE file
DUMMY_WORD_MULT= 6
#fixation min and max time (to be randomised)
#used to generate WORDS_FILE file
FIX_MIN = 0.5
FIX_MAX = 1.5

#every BLINK words blink instruction will occur
BLINK_MIN = 10
BLINK_MAX = 15




#true if send trigger
USE_SERIAL = False
#a value to be send to trigger on init
SERIAL_INIT_VALUE = 1
#serial port name
PORT_NAME = "COM1"




#internal ************************
NUM_OF_VALS = 3
START_ST = 100
START_DUR = 1000

s_st = [0.0, 1.0, 1.0]
s_dur = [1.0, 1.0, 2.0]