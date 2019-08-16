# Social and Cultural Dynamics Course 2017-2018
from psychopy import visual, core, data, event, logging, sound, gui
import numpy as np  # whole numpy lib is available, prepend 'np.'
from psychopy.constants import *  # things like STARTED, FINISHED
import pandas as pd
import random
import itertools
from psychopy.iohub import launchHubServer
#at the very beginning to load the server
io = launchHubServer()
keyboard = io.devices.keyboard


################## SETTING UP THE EXPERIMENTS'S CONSTANTS ###############

#number of trials per conditions
TRIALS = 1 # multiplied by number of unique stimulus type
practice_trials= 1 # multiplied by number of unique stimulus type

#list of waiting times from which we will randomly select later
waitingtimes = [0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4]

############## PREPARING THE DATAFRAME ######################

#where we will save the data
columnss = ['Participant', 'Condition', 'Imitative Compatibility', 'Spatial Compatibility', 'Reaction_time', 'Response', 'Correctness', 'Cue', 'Finger','Green']
indexs = np.arange(0)
DATA = pd.DataFrame(columns=columnss, index = indexs) 


################## THE GRAPHICAL INTERFACE ################

# gui requesting participant info
participant_id = gui.Dlg(title="Imitation-Inhibition experiment") 
participant_id.addText('Subject Info')
participant_id.addField('Participant:')
participant_id.addField('Condition:', choices = ['M','G', 'N'])
participant_id.show()

if participant_id.OK:
    Participant = participant_id.data[0]                     #saves data from dialogue box into the variable 'ID'
else:
    core.quite()
                        

#save condition to add to the dataframe
Condition = participant_id.data[1]

############# SETTING UP SOME PSYCHOPY CONSTANTS ###############

#window where we will show everything
win = visual.Window(fullscr=True, color='black', colorSpace='rgb', units = 'pix', allowStencil=True)
#watch we will use to measure RT
stopwatch = core.Clock()

#function to show instruction texts
def msg(txt):
    instructions = visual.TextStim(win, text=txt, color = 'white', height = 20,alignHoriz='center') # create an instruction text
    instructions.draw() # draw the text stimulus in a "hidden screen" so that it is ready to be presented 
    win.flip() # flip the screen to reveal the stimulus

instructions ='''
Welcome to this experiment.\n\nYou will be holding down the Cmd/Windows and Alt keys on the left side of the keyboard with your \
middle and index fingers respectively throughout this task.\n\nWhen the number "1" appears, lift your index finger \
as quickly as possible.\n\nWhen the number "2" appears, lift your middle finger as quickly as possible. \
Regardless of the response, return to holding down both Cmd/Windows and Alt/Option after each lifting movement.\n\nYou will first have a few practice trials. \
Afterwards, the experiment will being.\n\n Position your left index and middle fingers on the left Cmd/Windows and Alt buttons respectively.\n\n When you are ready press \
the spacebar to begin the set of practice trials.
'''

instructionsNumberless ='''
Welcome to this experiment.\n\nYou will be holding down the Cmd/Windows and Alt keys on the left side of the keyboard with your \
middle and index fingers respectively throughout this task.\n\nYou will see short movies off a hand lifting either the index or the middle finger.\n\n When you see the index finger lifting, lift your index finger \
as quickly as possible.\n\nWhen you see the middle finger lifting, lift your middle finger as quickly as possible. \n\n
Regardless of the response, return to holding down both Cmd/Windows and Alt/Option after each lifting movement.\n\nYou will first have a few practice trials. \
Afterwards, the experiment will being.\n\n Position your left index and middle fingers on the left Cmd/Windows and Alt buttons respectively.\n\n When you are ready press \
the spacebar to begin the set of practice trials.
'''


################# LOADING THE CONSTANT PICTURES TO MAKE THE FINGER ANIMATION ###############

#static hand lines for loading normal and mirrored hands
staticHand = visual.ImageStim(win=win, name='staticHand',image='Pictures/StaticHand.jpg')
staticHandR = visual.ImageStim(win=win, name='staticHandR',image='Pictures/StaticHand Reversed.jpg')
#blue blackground
blue = visual.ImageStim(win=win, name='blue',image='Pictures/blue.jpg')


################## CREATING A STIMULUS CLASS THAT HOLDS ALL THE CHARACTERISTICS OF OUR STIMULI AND A FUNCTION TO CREATE A TRIAL

class Stimulus():
    def __init__(self,someList, win):
        
        self.finger = someList[0]
        self.condition = someList[1]
        self.green = someList[2]
        
        #if spatial compatibility or numberless or numberless mirror, sc = 1, otherwise 0
        if self.condition[0:2] == "SC" or self.condition[-1] == "s" or self.condition[-1] == "r":
            self.sc = 1
        
        else:
            self.sc = 0
        
        #If imitation compatibility or numberless, ic = 1, otherwise 0
        if self.condition[2:4] == "IC" or self.condition[-1] == "s":
            self.ic = 1
        else:
            self.ic = 0
        
        #We load all the pictures
        self.pic1 = someList[3]
        self.pic2 = visual.ImageStim(win=win, name='pic2',image='Pictures/'+self.finger+'/'+self.condition+'/'+self.finger+str(2)+self.condition+'.jpg')
        self.pic3 = visual.ImageStim(win=win, name='pic3',image='Pictures/'+self.finger+'/'+self.condition+'/'+self.finger+str(3)+self.condition+'.jpg')
        self.pic4 = visual.ImageStim(win=win, name='pic4',image='Pictures/'+self.finger+'/'+self.condition+'/'+self.finger+str(4)+self.condition+'.jpg')

    def display(self):
        #record time
        trial_start=core.getTime()
        
        #wait some random time and show the hand
        number = random.choice(waitingtimes)
        self.pic1.draw()
        win.flip()
        core.wait(number)
        
        #wait a bit, show the first movement pic
        self.pic2.draw()
        win.flip()
        core.wait(0.34)
        
        #wait a bit, show the next pic
        self.pic3.draw()
        win.flip()
        core.wait(0.34)
        
        #wait a bit show the final pic
        self.pic4.draw()
        win.flip()
        core.wait(0.5)
        
        #what key was releasedafter seeing the stimulus?
        key = keyboard.waitForReleases(keys = ['lcmd','lalt'])
        while str(keyboard.state.keys()) != str(['lalt','lcmd']) and str(keyboard.state.keys()) != str(['lcmd','lalt']):
            core.wait(0.1)
        
        #make the hand disappear, get ready for a new trial
        blue.draw()
        win.flip()
        core.wait(0.5)
        
        #What finger did you move? (dependent on the key released)
        if key[0].key == "lalt":
            self.response = "i"
        else:
            self.response = "m"
        
        #reaction time
        self.RT = key[0].time - number - trial_start
        
        #What finger was the cue pointing at? if IC = 1, it's the same as the finger moving. Otherwise it's the other
        if self.ic == 1:
            self.cue = self.finger
        else :
            if self.finger == "i":
                self.cue = "m"
            else:
                self.cue = "i"
        
        #If your response correspond to the cue, then you are right
        if self.response == self.cue:
            self.correctness = 1
        else:
            self.correctness = 0

#################### SETTING UP THE TRIALS COMBINATION #####################

#We define some variables to create all combinations we want according to the condition
if Condition == 'M':
    conditions = ["SIII","SCII","SIIC","SCIC"]  #SC = Social Compatibility ; #SI = Social Incompatibility ; #IC = Imitation Compatibility #II = Imitation Incompatibility
    fingers = ["i","m"] #i = index, #m = middle
    green = [0] #0 = no green finger, #1 = green finger

elif Condition == 'G':
    function_list = ["SIII", "SCIC"]
    fingers = ["i","m"]
    green = [0,1]

elif Condition == 'N' :
    conditions = ["Numberless", "Numberless-mirror"] #Here task is different, this is about imitating
    fingers = ["i","m"]
    green = [0]

#Make a list of all possible combinations
trialList = list(itertools.product(fingers, conditions, green))

#A combination is a tuple, but we want it to be a list to .append stuff to it
for i in range(len(trialList)):
   trialList[i] = list(trialList[i])

#Adding the baseline picture
for el in trialList:
    if el[1] in ["SIIC","SCII","Numberless-mirror"]:
        el.append(staticHandR)
    else:
        el.append(staticHand)

#loading all stimuli before hand to avoid any kind of latency
stimulist = []
for i in range(len(trialList)):
    stimulist.append(Stimulus(trialList[i],win))


######################## STARTING THE EXPERIMENT #########################

#show instructions till they press space
msg(instructions)
event.waitKeys(keyList = 'space')

#practice loop with practice_trials (defined in the beginning) trials. Each video appears practice_trials times. DATA IS NOT SAVED
for t in range(practice_trials):
    #each time, we randomize the order of the videos, therefore, it is impossible for the same video to appear twice in a row. 
    rounds = np.random.permutation(stimulist)
    
    for stim in rounds:
        #do the function
        stim.display()

msg('You have completed all practice trials.\n\nPlease make sure to have your fingers on the buttons and press SPACE to move on to the experiment')
event.waitKeys(keyList = 'space')

#for loop with TRIALS (defined in the beginning) trials. Each video appears TRIALS times. data is saved
for t in range(TRIALS):#
    key = event.getKeys()
    
    if key=='escape':
        break
    #each time, we randomize the order of the videos, therefore, it is impossible for the same video to appear twice in a  row. 
    rounds = np.random.permutation(stimulist)
    for stim in rounds:
        #load the stimulus and do the function
        stim.display()
        
        #append trial data to pandas
        DATA = DATA.append({
            'Participant': Participant,
            'Condition': Condition,
            'Imitative Compatibility': stim.ic,
            'Spatial Compatibility': stim.sc,
            'Reaction_time':stim.RT,
            'Response': stim.response,
            'Correctness': stim.correctness,
            'Cue':stim.cue,
            'Finger': stim.finger,
            'Green': stim.green
            }, ignore_index=True)
    #Line was here in original script but doesn't seem relevant (kept just in case)
    #DATA.to_csv('data/II_'+Participant+'.csv')
msg('You are now done with the experiment :-) Please press SPACE')
event.waitKeys(keyList = 'space')

#save to csv file - put this in the end of the script 
DATA.to_csv('data/II_'+Participant+'_'+Condition+'.csv')