#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), November 16, 2016, at 10:54
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'SocialUrn'  # from the Builder filename that created this script
expInfo = {u'participant': u'999'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/' + '%s_%s' %(expInfo['participant'], expInfo['date']) + '_Urn'

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\lab\\Desktop\\Alcohol\\InferenceTask\\InferenceTask_keyboard.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=[1280, 1024], fullscr=False, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "initialise"
initialiseClock = core.Clock()
import random
import csv
import collections
import string
leftJelly=""
rightJelly=""
stopwatch = core.Clock()
counterD = collections.defaultdict(int)
correctResponses = 0
bucketNumber=0

yBucket=1
xBucket= 0
wBucket=.4
hBucket=.5


# Initialize components for Routine "Instruct1"
Instruct1Clock = core.Clock()
instruct1 = visual.TextStim(win=win, ori=0, name='instruct1',
    text="Part 1\n\nFor the following pairs of faces, choose the face that appears to be the most confident. \n\npress 'V' for LEFT   press 'B' for RIGHT",    font='Helvetica',
    pos=[0, 0.2], height=0.05, wrapWidth=1,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)
presskey1 = visual.TextStim(win=win, ori=0, name='presskey1',
    text='press any key to start',    font='Arial',
    pos=[0, -.75], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
imageLeft = visual.ImageStim(win=win, name='imageLeft',
    image='sin', mask=None,
    ori=0, pos=[-0.25, 0], size=[.3,.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
imageRight = visual.ImageStim(win=win, name='imageRight',
    image='sin', mask=None,
    ori=0, pos=[0.25, 0], size=[.3,.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)


# Initialize components for Routine "social_urn_intro"
social_urn_introClock = core.Clock()
#defaults
compplayer = 1 
confi = 'faces/04c.jpg'
unconfi = 'faces/04uc.jpg'
splayer =1
sgrab = 'hands/sgrab_darker.png'
sreach = 'hands/sreach_darker.png'
shand = 'hands/shand_dark.png'
comphand = 'hands/hand_04.png'
compreach = 'hands/reach_04.png'
compgrab = 'hands/grab_04.png'
pronoun = 'his'
pronoun2 = 'he'
computerface = visual.ImageStim(win=win, name='computerface',
    image='cartoon.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.75],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
pt2_intro_txt = visual.TextStim(win=win, ori=0, name='pt2_intro_txt',
    text='Part 2\n\nWelcome to the Jellybean Game!\nWith help from your virtual friend, \nyou are going to label buckets of\njellybeans.\n\nBuckets are either: 65% red or 65% blue\n\nYour job is to label each bucket as mostly red or mostly blue.',    font='Arial',
    pos=[-.3, .5], height=0.05, wrapWidth=1.5,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
blue_bucket_intro = visual.ImageStim(win=win, name='blue_bucket_intro',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[.65, -.3], size=[0.6, 0.75],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
redbucket_intro = visual.ImageStim(win=win, name='redbucket_intro',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0.2, -.3], size=[.6, 0.75],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
press = visual.TextStim(win=win, ori=0, name='press',
    text='press any key to continue.',    font='Arial',
    pos=[0, -.8], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)
labelred = visual.ImageStim(win=win, name='labelred',
    image='red_choice_s.png', mask=None,
    ori=0, pos=[0.2, -.3], size=[0.2, 0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
labelblue = visual.ImageStim(win=win, name='labelblue',
    image='blue_choice_s.png', mask=None,
    ori=0, pos=[0.65, -.3], size=[0.2, 0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)

# Initialize components for Routine "pickplayer"
pickplayerClock = core.Clock()

player1 = visual.ImageStim(win=win, name='player1',
    image='faces/04c.jpg', mask=None,
    ori=0, pos=[-.45, 0.5], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
player2 = visual.ImageStim(win=win, name='player2',
    image='faces/30c.jpg', mask=None,
    ori=0, pos=[-.15, 0.5], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
player3 = visual.ImageStim(win=win, name='player3',
    image='faces/11c.jpg', mask=None,
    ori=0, pos=[0.15, 0.5], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
player4 = visual.ImageStim(win=win, name='player4',
    image='faces/06c.jpg', mask=None,
    ori=0, pos=[.45, 0.5], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
hand1 = visual.ImageStim(win=win, name='hand1',
    image='hands/hand_04.png', mask=None,
    ori=0, pos=[-.45, -.5], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
hand2 = visual.ImageStim(win=win, name='hand2',
    image='hands/hand_19.png', mask=None,
    ori=0, pos=[-.15, -.5], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
hand3 = visual.ImageStim(win=win, name='hand3',
    image='hands/hand_11.png', mask=None,
    ori=0, pos=[0.15, -.5], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
hand4 = visual.ImageStim(win=win, name='hand4',
    image='hands/hand_06.png', mask=None,
    ori=0, pos=[0.45, -.5], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
Pick = visual.TextStim(win=win, ori=0, name='Pick',
    text='Pick your virtual partner for the jellybean game.',    font='Arial',
    pos=[0, 0.83], height=0.1, wrapWidth=100,
    color='black', colorSpace='rgb', opacity=1,
    depth=-10.0)
player1uc = visual.ImageStim(win=win, name='player1uc',
    image='faces/04uc.jpg', mask=None,
    ori=0, pos=[-.45, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
player2uc = visual.ImageStim(win=win, name='player2uc',
    image='faces/30uc.jpg', mask=None,
    ori=0, pos=[-.15, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
player3uc = visual.ImageStim(win=win, name='player3uc',
    image='faces/11uc.jpg', mask=None,
    ori=0, pos=[.15,0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
player4uc = visual.ImageStim(win=win, name='player4uc',
    image='faces/06uc.jpg', mask=None,
    ori=0, pos=[.45, 0], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
choose = visual.TextStim(win=win, ori=0, name='choose',
    text='  V           B           N           M',    font='Arial',
    pos=[0, -.85], height=0.1, wrapWidth=1.5,
    color='black', colorSpace='rgb', opacity=1,
    depth=-15.0)

# Initialize components for Routine "confident"
confidentClock = core.Clock()

confText = visual.TextStim(win=win, ori=0, name='confText',
    text='default text',    font='Arial',
    pos=[-.3, .2], height=0.05, wrapWidth=.5,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
unconfText = visual.TextStim(win=win, ori=0, name='unconfText',
    text='default text',    font='Arial',
    pos=[.3, 0.2], height=0.05, wrapWidth=.5,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
conf = visual.ImageStim(win=win, name='conf',
    image='sin', mask=None,
    ori=0, pos=[-.3, -.2], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
unconf = visual.ImageStim(win=win, name='unconf',
    image='sin', mask=None,
    ori=0, pos=[.3, -.2], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
press_i1 = visual.TextStim(win=win, ori=0, name='press_i1',
    text='press any key to continue',    font='Arial',
    pos=[0, -.9], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "pickhand"
pickhandClock = core.Clock()
darker = visual.ImageStim(win=win, name='darker',
    image='hands/shand_dark.png', mask=None,
    ori=0, pos=[-0.3, 0], size=[0.52, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
lighter = visual.ImageStim(win=win, name='lighter',
    image='hands/shand_light.png', mask=None,
    ori=0, pos=[.3, 0], size=[0.52, 1],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
Pick_hand = visual.TextStim(win=win, ori=0, name='Pick_hand',
    text='Pick your hand.',    font='Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)

text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text='V                         B',    font='Arial',
    pos=[0, -.65], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "Ins_intro"
Ins_introClock = core.Clock()

ins_0 = visual.TextStim(win=win, ori=0, name='ins_0',
    text="\nNow let's go through what happens\nin each situation.",    font='Arial',
    pos=[0, -.2], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
press_0 = visual.TextStim(win=win, ori=0, name='press_0',
    text='press key to continue',    font='Arial',
    pos=[0, -.75], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
chosen_other = visual.ImageStim(win=win, name='chosen_other',
    image='sin', mask=None,
    ori=0, pos=[0, 0.5], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "fix_i"
fix_iClock = core.Clock()
xBucket= 0
wBucket=.4
hBucket=.5

bucket_i1 = visual.ImageStim(win=win, name='bucket_i1',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
bucketText_i1 = visual.TextStim(win=win, ori=0, name='bucketText_i1',
    text='default text',    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
ins1 = visual.TextStim(win=win, ori=0, name='ins1',
    text='A new bucket arrives...',    font='Arial',
    pos=[0, -.5], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
press_1 = visual.TextStim(win=win, ori=0, name='press_1',
    text='press key to continue',    font='Arial',
    pos=[0, -.75], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "shake_i"
shake_iClock = core.Clock()

bucket_i2 = visual.ImageStim(win=win, name='bucket_i2',
    image='bucket_bare.png', mask=None,
    ori=1.0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
bucketText_i2 = visual.TextStim(win=win, ori=1.0, name='bucketText_i2',
    text='demo\nbucket',    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)
ins2 = visual.TextStim(win=win, ori=0, name='ins2',
    text='...and shakes so it is well mixed.',    font='Arial',
    pos=[0, -.5], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)
press_2 = visual.TextStim(win=win, ori=0, name='press_2',
    text='press key to continue',    font='Arial',
    pos=[0, -.75], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "reach_i"
reach_iClock = core.Clock()

ComputerReach_i = visual.ImageStim(win=win, name='ComputerReach_i',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.1*2, 0.5*2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
SubjectReach_i = visual.ImageStim(win=win, name='SubjectReach_i',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.1*2, 0.5*2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
bucket_i3 = visual.ImageStim(win=win, name='bucket_i3',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ins_i3 = visual.TextStim(win=win, ori=0, name='ins_i3',
    text='You and your virtual partner take different samples from the bucket.\n\nYour samples contain different beans.',    font='Arial',
    pos=[0, -.5], height=0.05, wrapWidth=1.2,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)
bucketText_i3 = visual.TextStim(win=win, ori=0, name='bucketText_i3',
    text='demo\nbucket',    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "grab_i"
grab_iClock = core.Clock()

ComputerGrab_i4 = visual.ImageStim(win=win, name='ComputerGrab_i4',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.1*2, 0.5*2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
grab_subject_i4 = visual.ImageStim(win=win, name='grab_subject_i4',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.1*2, 0.5*2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
bucket_i4 = visual.ImageStim(win=win, name='bucket_i4',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ins_i4 = visual.TextStim(win=win, ori=0, name='ins_i4',
    text='You and your virtual partner take different\nsamples from the bucket.\n\nYour samples contain different beans.',    font='Arial',
    pos=[0, -.5], height=0.05, wrapWidth=1.2,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)
press_i4 = visual.TextStim(win=win, ori=0, name='press_i4',
    text='default text',    font='Arial',
    pos=[0, -.85], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)
bucketText_i4 = visual.TextStim(win=win, ori=0, name='bucketText_i4',
    text='demo\nbucket',    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "CompOutcome_i"
CompOutcome_iClock = core.Clock()
xcompHand=  -.25
handw = .45
handh = .92
bucket_i5 = visual.ImageStim(win=win, name='bucket_i5',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
cartoon_3 = visual.ImageStim(win=win, name='cartoon_3',
    image='faces/cartoon.png', mask=None,
    ori=0, pos=[-0.25, -0.2], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
compHandUp_2 = visual.ImageStim(win=win, name='compHandUp_2',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
ins_i5 = visual.TextStim(win=win, ori=0, name='ins_i5',
    text='default text',    font='Arial',
    pos=[.5, -.2], height=0.05, wrapWidth=1,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)
bucketText_i5 = visual.TextStim(win=win, ori=0, name='bucketText_i5',
    text='or',    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)
leftjelly_i5 = visual.ImageStim(win=win, name='leftjelly_i5',
    image='sin', mask=None,
    ori=0, pos=[0.1, .5], size=[0.2, 0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
rightjelly_i5 = visual.ImageStim(win=win, name='rightjelly_i5',
    image='sin', mask=None,
    ori=0, pos=[-0.1, .5], size=[0.2, 0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
press_i5 = visual.TextStim(win=win, ori=0, name='press_i5',
    text='press any key to continue',    font='Arial',
    pos=[0.5, -0.75], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-8.0)

# Initialize components for Routine "compface_i"
compface_iClock = core.Clock()
conditionConf=""
conditionUnconf=""

ins_i6 = visual.TextStim(win=win, ori=0, name='ins_i6',
    text='default text',    font='Arial',
    pos=[0.4, -.3], height=0.05, wrapWidth=0.6,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)
ComputerFace_i6 = visual.ImageStim(win=win, name='ComputerFace_i6',
    image='sin', mask=None,
    ori=0, pos=[-0.25, -0.25], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
bucket_i6 = visual.ImageStim(win=win, name='bucket_i6',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
CompBeanChoice_i6 = visual.ImageStim(win=win, name='CompBeanChoice_i6',
    image='sin', mask=None,
    ori=0, pos=[-0.25, -0.6], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
compHand_i6 = visual.ImageStim(win=win, name='compHand_i6',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
press_i6 = visual.TextStim(win=win, ori=0, name='press_i6',
    text='press key to continue',    font='Arial',
    pos=[0.5, -.85], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "SubOutcome_i"
SubOutcome_iClock = core.Clock()
from random import shuffle
import math
yadd = .065 # jellybean vertical distance
xadd = .06 # jellybean horizontal distance
xhand = .28 #subject hand x pos
jwidth = .06
jheight = .1
subHand_i7 = visual.ImageStim(win=win, name='subHand_i7',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[handw, handh],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
bucket_19 = visual.ImageStim(win=win, name='bucket_19',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sjelly1_2 = visual.ImageStim(win=win, name='sjelly1_2',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth,jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sjelly2_2 = visual.ImageStim(win=win, name='sjelly2_2',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
sjelly3_2 = visual.ImageStim(win=win, name='sjelly3_2',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
sjelly4_2 = visual.ImageStim(win=win, name='sjelly4_2',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
sjelly5_2 = visual.ImageStim(win=win, name='sjelly5_2',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
sjelly6_2 = visual.ImageStim(win=win, name='sjelly6_2',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
sjelly7_2 = visual.ImageStim(win=win, name='sjelly7_2',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
sjelly8_2 = visual.ImageStim(win=win, name='sjelly8_2',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
ins_i7 = visual.TextStim(win=win, ori=0, name='ins_i7',
    text='Then you see\nyour sample.',    font='Arial',
    pos=[.75, 0], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-11.0)
press_i7 = visual.TextStim(win=win, ori=0, name='press_i7',
    text='press key to continue',    font='Arial',
    pos=[0.75, -.25], height=0.05, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-12.0)

# Initialize components for Routine "SubChoose_i"
SubChoose_iClock = core.Clock()

bucket_20 = visual.ImageStim(win=win, name='bucket_20',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
text_6 = visual.TextStim(win=win, ori=0, name='text_6',
    text="Based on ALL the useful information, choose what YOU think is in the bucket.\n\npress 'V' for LEFT label\npress 'B' for the RIGHT label.\n\nWatch out! The labels switch sides.\n\nChoose as quickly as you can.",    font='Arial',
    pos=[0.65, .1], height=0.05, wrapWidth=.75,
    color='black', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "subFeedback_i"
subFeedback_iClock = core.Clock()
bucket_21 = visual.ImageStim(win=win, name='bucket_21',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
LeftJellyS_i = visual.ImageStim(win=win, name='LeftJellyS_i',
    image='sin', mask=None,
    ori=0, pos=[0, .5], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
RightJellyS_i = visual.ImageStim(win=win, name='RightJellyS_i',
    image='sin', mask=None,
    ori=0, pos=[0, 0.5], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

goodjob = visual.TextStim(win=win, ori=0, name='goodjob',
    text='You labeled it.\n\nNow lets have six practice trials in real time.\n\nChoose as quickly and accurately as possible.\n\n\nPress any key.\n',    font='Arial',
    pos=[0, -.5], height=0.075, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "thiscounts"
thiscountsClock = core.Clock()
n = 0
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()


bucket = visual.ImageStim(win=win, name='bucket',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
BucketText1 = visual.TextStim(win=win, ori=0, name='BucketText1',
    text='default text',    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "fixshaker"
fixshakerClock = core.Clock()

bucket2 = visual.ImageStim(win=win, name='bucket2',
    image='bucket_bare.png', mask=None,
    ori=1.0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
BucketText2 = visual.TextStim(win=win, ori=1.0, name='BucketText2',
    text='default text',    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "Reach"
ReachClock = core.Clock()

ComputerReach = visual.ImageStim(win=win, name='ComputerReach',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.1*2, 0.5*2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
SubjectReach = visual.ImageStim(win=win, name='SubjectReach',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.1*2, 0.5*2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
bucket3 = visual.ImageStim(win=win, name='bucket3',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
BucketText3 = visual.TextStim(win=win, ori=0, name='BucketText3',
    text='default text',    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "Grab"
GrabClock = core.Clock()

ComputerGrab = visual.ImageStim(win=win, name='ComputerGrab',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.1*2, 0.5*2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
grab_subject = visual.ImageStim(win=win, name='grab_subject',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[0.1*2, 0.5*2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
bucket4 = visual.ImageStim(win=win, name='bucket4',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
BucketText4 = visual.TextStim(win=win, ori=0, name='BucketText4',
    text='default text',    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-4.0)

# Initialize components for Routine "CompOutcome"
CompOutcomeClock = core.Clock()
xcompHand=  -.25
handw = .45
handh = .92


bucket5 = visual.ImageStim(win=win, name='bucket5',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
cartoon = visual.ImageStim(win=win, name='cartoon',
    image='faces/cartoon.png', mask=None,
    ori=0, pos=[-0.25, -0.2], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
compHand = visual.ImageStim(win=win, name='compHand',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
leftJelly = visual.ImageStim(win=win, name='leftJelly',
    image='sin', mask=None,
    ori=0, pos=[-0.1, 0.5], size=[0.2, 0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
rightJelly = visual.ImageStim(win=win, name='rightJelly',
    image='sin', mask=None,
    ori=0, pos=[.1, 0.5], size=[0.2, 0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
ortext = visual.TextStim(win=win, ori=0, name='ortext',
    text='or',    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=-6.0)

# Initialize components for Routine "CompOutcome_pause"
CompOutcome_pauseClock = core.Clock()
cartoon_2 = visual.ImageStim(win=win, name='cartoon_2',
    image='faces/cartoon.png', mask=None,
    ori=0, pos=[-0.25, -.2], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "CompFace"
CompFaceClock = core.Clock()
conditionConf=""
conditionUnconf=""
ComputerFace = visual.ImageStim(win=win, name='ComputerFace',
    image='sin', mask=None,
    ori=0, pos=[-0.25, -0.25], size=[0.3, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
CompBeanChoice = visual.ImageStim(win=win, name='CompBeanChoice',
    image='sin', mask=None,
    ori=0, pos=[-0.25, -0.6], size=[0.2, 0.25],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
compHandf = visual.ImageStim(win=win, name='compHandf',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "SubOutcome"
SubOutcomeClock = core.Clock()
from random import shuffle
import math
yadd = .065 # jellybean vertical distance
xadd = .06 # jellybean horizontal distance
xhand = .28 #subject hand x pos
jwidth = .06
jheight = .1
subHand = visual.ImageStim(win=win, name='subHand',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[handw, handh],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
sjelly1 = visual.ImageStim(win=win, name='sjelly1',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth,jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sjelly2 = visual.ImageStim(win=win, name='sjelly2',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
sjelly3 = visual.ImageStim(win=win, name='sjelly3',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
sjelly4 = visual.ImageStim(win=win, name='sjelly4',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
sjelly5 = visual.ImageStim(win=win, name='sjelly5',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
sjelly6 = visual.ImageStim(win=win, name='sjelly6',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
sjelly7 = visual.ImageStim(win=win, name='sjelly7',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-8.0)
sjelly8 = visual.ImageStim(win=win, name='sjelly8',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=[jwidth, jheight],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-9.0)
comphandout = visual.ImageStim(win=win, name='comphandout',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[handw,handh],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)

# Initialize components for Routine "SubChoose"
SubChooseClock = core.Clock()


# Initialize components for Routine "subFeedback"
subFeedbackClock = core.Clock()
bucket6 = visual.ImageStim(win=win, name='bucket6',
    image='bucket_bare.png', mask=None,
    ori=0, pos=[0,0], size=[0.6, 0.7],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
LeftJellyS_3 = visual.ImageStim(win=win, name='LeftJellyS_3',
    image='sin', mask=None,
    ori=0, pos=[-.1, .5], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
RightJellyS_3 = visual.ImageStim(win=win, name='RightJellyS_3',
    image='sin', mask=None,
    ori=0, pos=[0.1, 0.5], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)


# Initialize components for Routine "ITI"
ITIClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text='+',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "blank"
blankClock = core.Clock()
all_done = visual.TextStim(win=win, ori=0, name='all_done',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='black', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "initialise"-------
t = 0
initialiseClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat

# keep track of which components have finished
initialiseComponents = []
for thisComponent in initialiseComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "initialise"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = initialiseClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in initialiseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "initialise"-------
for thisComponent in initialiseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#------Prepare to start Routine "Instruct1"-------
t = 0
Instruct1Clock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
Instruct1Components = []
Instruct1Components.append(instruct1)
Instruct1Components.append(key_resp_2)
Instruct1Components.append(presskey1)
for thisComponent in Instruct1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instruct1"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = Instruct1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct1* updates
    if t >= 0.0 and instruct1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct1.tStart = t  # underestimates by a little under one frame
        instruct1.frameNStart = frameN  # exact frame index
        instruct1.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 1 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *presskey1* updates
    if t >= 1 and presskey1.status == NOT_STARTED:
        # keep track of start time/frame for later
        presskey1.tStart = t  # underestimates by a little under one frame
        presskey1.frameNStart = frameN  # exact frame index
        presskey1.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "Instruct1"-------
for thisComponent in Instruct1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
face_recog = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\lab\\Desktop\\Alcohol\\InferenceTask\\InferenceTask_keyboard.psyexp',
    trialList=data.importConditions('filelists/conf_cond.xlsx'),
    seed=None, name='face_recog')
thisExp.addLoop(face_recog)  # add the loop to the experiment
thisFace_recog = face_recog.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisFace_recog.rgb)
if thisFace_recog != None:
    for paramName in thisFace_recog.keys():
        exec(paramName + '= thisFace_recog.' + paramName)

for thisFace_recog in face_recog:
    currentLoop = face_recog
    # abbreviate parameter names if possible (e.g. rgb = thisFace_recog.rgb)
    if thisFace_recog != None:
        for paramName in thisFace_recog.keys():
            exec(paramName + '= thisFace_recog.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    faceButton = event.BuilderKeyResponse()  # create an object of type KeyResponse
    faceButton.status = NOT_STARTED
    imageLeft.setImage(imageFile1)
    imageRight.setImage(imageFile2)
    event.clearEvents(eventType= 'keyboard')
    
    keep = 0
    response = ""
    confFacesRT=0
    
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(faceButton)
    trialComponents.append(ISI)
    trialComponents.append(imageLeft)
    trialComponents.append(imageRight)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *faceButton* updates
        if t >= 0 and faceButton.status == NOT_STARTED:
            # keep track of start time/frame for later
            faceButton.tStart = t  # underestimates by a little under one frame
            faceButton.frameNStart = frameN  # exact frame index
            faceButton.status = STARTED
            # keyboard checking is just starting
            faceButton.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if faceButton.status == STARTED:
            theseKeys = event.getKeys(keyList=['v', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                faceButton.keys = theseKeys[-1]  # just the last key pressed
                faceButton.rt = faceButton.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *imageLeft* updates
        if t >= 0.0 and imageLeft.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageLeft.tStart = t  # underestimates by a little under one frame
            imageLeft.frameNStart = frameN  # exact frame index
            imageLeft.setAutoDraw(True)
        
        # *imageRight* updates
        if t >= 0.0 and imageRight.status == NOT_STARTED:
            # keep track of start time/frame for later
            imageRight.tStart = t  # underestimates by a little under one frame
            imageRight.frameNStart = frameN  # exact frame index
            imageRight.setAutoDraw(True)
        
        
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if faceButton.keys in ['', [], None]:  # No response was made
       faceButton.keys=None
    # store data for face_recog (TrialHandler)
    face_recog.addData('faceButton.keys',faceButton.keys)
    if faceButton.keys != None:  # we had a response
        face_recog.addData('faceButton.rt', faceButton.rt)
    #keys = event.getKeys(['b', 'n']) 
    #print keys
    
    if faceButton.keys == 'n':
        response="right"
        confFacesRT=t
    if faceButton.keys == 'b':
        response="left"
        confFacesRT=t
    
    if (response == str(corrAns)): 
      responseCorr = 1
    else: 
      responseCorr = 0
    
    face_recog.addData('response',response)
    face_recog.addData('responseCorr',responseCorr)
    face_recog.addData('confFacesRT',confFacesRT)
    thisExp.nextEntry()
    
# completed 1 repeats of 'face_recog'

# get names of stimulus parameters
if face_recog.trialList in ([], [None], None):  params = []
else:  params = face_recog.trialList[0].keys()
# save data for this loop
face_recog.saveAsExcel(filename + '.xlsx', sheetName='face_recog',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
face_recog.saveAsText(filename + 'face_recog.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
pickother = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\lab\\Desktop\\Alcohol\\InferenceTask\\InferenceTask_keyboard.psyexp',
    trialList=[None],
    seed=None, name='pickother')
thisExp.addLoop(pickother)  # add the loop to the experiment
thisPickother = pickother.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPickother.rgb)
if thisPickother != None:
    for paramName in thisPickother.keys():
        exec(paramName + '= thisPickother.' + paramName)

for thisPickother in pickother:
    currentLoop = pickother
    # abbreviate parameter names if possible (e.g. rgb = thisPickother.rgb)
    if thisPickother != None:
        for paramName in thisPickother.keys():
            exec(paramName + '= thisPickother.' + paramName)
    
    #------Prepare to start Routine "social_urn_intro"-------
    t = 0
    social_urn_introClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    xbucket = .4
    ybucket = 1.5
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    # keep track of which components have finished
    social_urn_introComponents = []
    social_urn_introComponents.append(computerface)
    social_urn_introComponents.append(pt2_intro_txt)
    social_urn_introComponents.append(blue_bucket_intro)
    social_urn_introComponents.append(redbucket_intro)
    social_urn_introComponents.append(press)
    social_urn_introComponents.append(key_resp_3)
    social_urn_introComponents.append(labelred)
    social_urn_introComponents.append(labelblue)
    for thisComponent in social_urn_introComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "social_urn_intro"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = social_urn_introClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if ybucket>.5:
            ybucket=1-frameN/20
        
        # *computerface* updates
        if t >= 0.0 and computerface.status == NOT_STARTED:
            # keep track of start time/frame for later
            computerface.tStart = t  # underestimates by a little under one frame
            computerface.frameNStart = frameN  # exact frame index
            computerface.setAutoDraw(True)
        if computerface.status == STARTED:  # only update if being drawn
            computerface.setPos([xbucket, .5], log=False)
        
        # *pt2_intro_txt* updates
        if t >= 0.0 and pt2_intro_txt.status == NOT_STARTED:
            # keep track of start time/frame for later
            pt2_intro_txt.tStart = t  # underestimates by a little under one frame
            pt2_intro_txt.frameNStart = frameN  # exact frame index
            pt2_intro_txt.setAutoDraw(True)
        
        # *blue_bucket_intro* updates
        if t >= 0.0 and blue_bucket_intro.status == NOT_STARTED:
            # keep track of start time/frame for later
            blue_bucket_intro.tStart = t  # underestimates by a little under one frame
            blue_bucket_intro.frameNStart = frameN  # exact frame index
            blue_bucket_intro.setAutoDraw(True)
        
        # *redbucket_intro* updates
        if t >= 0.0 and redbucket_intro.status == NOT_STARTED:
            # keep track of start time/frame for later
            redbucket_intro.tStart = t  # underestimates by a little under one frame
            redbucket_intro.frameNStart = frameN  # exact frame index
            redbucket_intro.setAutoDraw(True)
        
        # *press* updates
        if t >= 1 and press.status == NOT_STARTED:
            # keep track of start time/frame for later
            press.tStart = t  # underestimates by a little under one frame
            press.frameNStart = frameN  # exact frame index
            press.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 1 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *labelred* updates
        if t >= 0.0 and labelred.status == NOT_STARTED:
            # keep track of start time/frame for later
            labelred.tStart = t  # underestimates by a little under one frame
            labelred.frameNStart = frameN  # exact frame index
            labelred.setAutoDraw(True)
        
        # *labelblue* updates
        if t >= 0.0 and labelblue.status == NOT_STARTED:
            # keep track of start time/frame for later
            labelblue.tStart = t  # underestimates by a little under one frame
            labelblue.frameNStart = frameN  # exact frame index
            labelblue.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in social_urn_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "social_urn_intro"-------
    for thisComponent in social_urn_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    xbucket = 0
    ybucket = 1.2
    
    #------Prepare to start Routine "pickplayer"-------
    t = 0
    pickplayerClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    playerButton = event.BuilderKeyResponse()  # create an object of type KeyResponse
    playerButton.status = NOT_STARTED
    compplayer = 0
    
    # keep track of which components have finished
    pickplayerComponents = []
    pickplayerComponents.append(playerButton)
    pickplayerComponents.append(player1)
    pickplayerComponents.append(player2)
    pickplayerComponents.append(player3)
    pickplayerComponents.append(player4)
    pickplayerComponents.append(hand1)
    pickplayerComponents.append(hand2)
    pickplayerComponents.append(hand3)
    pickplayerComponents.append(hand4)
    pickplayerComponents.append(Pick)
    pickplayerComponents.append(player1uc)
    pickplayerComponents.append(player2uc)
    pickplayerComponents.append(player3uc)
    pickplayerComponents.append(player4uc)
    pickplayerComponents.append(choose)
    for thisComponent in pickplayerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pickplayer"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pickplayerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *playerButton* updates
        if t >= 0.0 and playerButton.status == NOT_STARTED:
            # keep track of start time/frame for later
            playerButton.tStart = t  # underestimates by a little under one frame
            playerButton.frameNStart = frameN  # exact frame index
            playerButton.status = STARTED
            # keyboard checking is just starting
            playerButton.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if playerButton.status == STARTED:
            theseKeys = event.getKeys(keyList=['v', 'b', 'n', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                playerButton.keys = theseKeys[-1]  # just the last key pressed
                playerButton.rt = playerButton.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        
        # *player1* updates
        if t >= 0.0 and player1.status == NOT_STARTED:
            # keep track of start time/frame for later
            player1.tStart = t  # underestimates by a little under one frame
            player1.frameNStart = frameN  # exact frame index
            player1.setAutoDraw(True)
        
        # *player2* updates
        if t >= 0.0 and player2.status == NOT_STARTED:
            # keep track of start time/frame for later
            player2.tStart = t  # underestimates by a little under one frame
            player2.frameNStart = frameN  # exact frame index
            player2.setAutoDraw(True)
        
        # *player3* updates
        if t >= 0.0 and player3.status == NOT_STARTED:
            # keep track of start time/frame for later
            player3.tStart = t  # underestimates by a little under one frame
            player3.frameNStart = frameN  # exact frame index
            player3.setAutoDraw(True)
        
        # *player4* updates
        if t >= 0.0 and player4.status == NOT_STARTED:
            # keep track of start time/frame for later
            player4.tStart = t  # underestimates by a little under one frame
            player4.frameNStart = frameN  # exact frame index
            player4.setAutoDraw(True)
        
        # *hand1* updates
        if t >= 0.0 and hand1.status == NOT_STARTED:
            # keep track of start time/frame for later
            hand1.tStart = t  # underestimates by a little under one frame
            hand1.frameNStart = frameN  # exact frame index
            hand1.setAutoDraw(True)
        
        # *hand2* updates
        if t >= 0.0 and hand2.status == NOT_STARTED:
            # keep track of start time/frame for later
            hand2.tStart = t  # underestimates by a little under one frame
            hand2.frameNStart = frameN  # exact frame index
            hand2.setAutoDraw(True)
        
        # *hand3* updates
        if t >= 0.0 and hand3.status == NOT_STARTED:
            # keep track of start time/frame for later
            hand3.tStart = t  # underestimates by a little under one frame
            hand3.frameNStart = frameN  # exact frame index
            hand3.setAutoDraw(True)
        
        # *hand4* updates
        if t >= 0.0 and hand4.status == NOT_STARTED:
            # keep track of start time/frame for later
            hand4.tStart = t  # underestimates by a little under one frame
            hand4.frameNStart = frameN  # exact frame index
            hand4.setAutoDraw(True)
        
        # *Pick* updates
        if t >= 0.0 and Pick.status == NOT_STARTED:
            # keep track of start time/frame for later
            Pick.tStart = t  # underestimates by a little under one frame
            Pick.frameNStart = frameN  # exact frame index
            Pick.setAutoDraw(True)
        
        # *player1uc* updates
        if t >= 0.0 and player1uc.status == NOT_STARTED:
            # keep track of start time/frame for later
            player1uc.tStart = t  # underestimates by a little under one frame
            player1uc.frameNStart = frameN  # exact frame index
            player1uc.setAutoDraw(True)
        
        # *player2uc* updates
        if t >= 0.0 and player2uc.status == NOT_STARTED:
            # keep track of start time/frame for later
            player2uc.tStart = t  # underestimates by a little under one frame
            player2uc.frameNStart = frameN  # exact frame index
            player2uc.setAutoDraw(True)
        
        # *player3uc* updates
        if t >= 0.0 and player3uc.status == NOT_STARTED:
            # keep track of start time/frame for later
            player3uc.tStart = t  # underestimates by a little under one frame
            player3uc.frameNStart = frameN  # exact frame index
            player3uc.setAutoDraw(True)
        
        # *player4uc* updates
        if t >= 0.0 and player4uc.status == NOT_STARTED:
            # keep track of start time/frame for later
            player4uc.tStart = t  # underestimates by a little under one frame
            player4uc.frameNStart = frameN  # exact frame index
            player4uc.setAutoDraw(True)
        
        # *choose* updates
        if t >= 0.0 and choose.status == NOT_STARTED:
            # keep track of start time/frame for later
            choose.tStart = t  # underestimates by a little under one frame
            choose.frameNStart = frameN  # exact frame index
            choose.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pickplayerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "pickplayer"-------
    for thisComponent in pickplayerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if playerButton.keys in ['', [], None]:  # No response was made
       playerButton.keys=None
    # store data for pickother (TrialHandler)
    pickother.addData('playerButton.keys',playerButton.keys)
    if playerButton.keys != None:  # we had a response
        pickother.addData('playerButton.rt', playerButton.rt)
    if playerButton.keys == 'v':
        compplayer = 1
        comphand = 'hands/hand_04.png'
        compreach = 'hands/reach_04.png'
        compgrab = 'hands/grab_04.png'
        pronoun = 'his'
        pronoun2 = 'he'
    elif playerButton.keys == 'b':
        compplayer = 2
        comphand = 'hands/hand_19.png'
        compreach = 'hands/reach_19.png'
        compgrab = 'hands/grab_19.png'
        pronoun = 'his'
        pronoun2 = 'he'
    elif playerButton.keys == 'n':
        compplayer = 3
        comphand= 'hands/hand_11.png'
        compreach = 'hands/reach_11.png'
        compgrab = 'hands/grab_11.png'
        pronoun = 'her'
        pronoun2 = 'she'
    elif playerButton.keys == 'm':
        compplayer = 4
        comphand = 'hands/hand_06.png'
        compreach = 'hands/reach_06.png'
        compgrab = 'hands/grab_06.png'
        pronoun = 'her'
        pronoun2 = 'she'
    
    
    #------Prepare to start Routine "confident"-------
    t = 0
    confidentClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if compplayer == 1: 
       confi = 'faces/04c.jpg'
    if compplayer == 2: 
       confi = 'faces/30c.jpg'
    if compplayer == 3: 
       confi = 'faces/11c.jpg'
    if compplayer == 4: 
       confi = 'faces/06c.jpg'
    if compplayer == 1: 
       unconfi = 'faces/04uc.jpg'
    if compplayer == 2: 
       unconfi = 'faces/30uc.jpg'
    if compplayer == 3: 
       unconfi = 'faces/11uc.jpg'
    if compplayer == 4: 
       unconfi = 'faces/06uc.jpg'
    confText.setText('This is '+ pronoun + ' confident face')
    unconfText.setText('This is '+ pronoun + ' unconfident face')
    conf.setImage(confi)
    unconf.setImage(unconfi)
    key_resp_6 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_6.status = NOT_STARTED
    # keep track of which components have finished
    confidentComponents = []
    confidentComponents.append(confText)
    confidentComponents.append(unconfText)
    confidentComponents.append(conf)
    confidentComponents.append(unconf)
    confidentComponents.append(key_resp_6)
    confidentComponents.append(press_i1)
    for thisComponent in confidentComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "confident"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = confidentClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *confText* updates
        if t >= 0.0 and confText.status == NOT_STARTED:
            # keep track of start time/frame for later
            confText.tStart = t  # underestimates by a little under one frame
            confText.frameNStart = frameN  # exact frame index
            confText.setAutoDraw(True)
        
        # *unconfText* updates
        if t >= 0.0 and unconfText.status == NOT_STARTED:
            # keep track of start time/frame for later
            unconfText.tStart = t  # underestimates by a little under one frame
            unconfText.frameNStart = frameN  # exact frame index
            unconfText.setAutoDraw(True)
        
        # *conf* updates
        if t >= 0.0 and conf.status == NOT_STARTED:
            # keep track of start time/frame for later
            conf.tStart = t  # underestimates by a little under one frame
            conf.frameNStart = frameN  # exact frame index
            conf.setAutoDraw(True)
        
        # *unconf* updates
        if t >= 0.0 and unconf.status == NOT_STARTED:
            # keep track of start time/frame for later
            unconf.tStart = t  # underestimates by a little under one frame
            unconf.frameNStart = frameN  # exact frame index
            unconf.setAutoDraw(True)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t  # underestimates by a little under one frame
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # *press_i1* updates
        if t >= 1 and press_i1.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_i1.tStart = t  # underestimates by a little under one frame
            press_i1.frameNStart = frameN  # exact frame index
            press_i1.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in confidentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "confident"-------
    for thisComponent in confidentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    #------Prepare to start Routine "pickhand"-------
    t = 0
    pickhandClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    handButton = event.BuilderKeyResponse()  # create an object of type KeyResponse
    handButton.status = NOT_STARTED
    
    # keep track of which components have finished
    pickhandComponents = []
    pickhandComponents.append(handButton)
    pickhandComponents.append(darker)
    pickhandComponents.append(lighter)
    pickhandComponents.append(Pick_hand)
    pickhandComponents.append(text_3)
    for thisComponent in pickhandComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pickhand"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = pickhandClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *handButton* updates
        if t >= 0.0 and handButton.status == NOT_STARTED:
            # keep track of start time/frame for later
            handButton.tStart = t  # underestimates by a little under one frame
            handButton.frameNStart = frameN  # exact frame index
            handButton.status = STARTED
            # keyboard checking is just starting
            handButton.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if handButton.status == STARTED:
            theseKeys = event.getKeys(keyList=['v', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                handButton.keys = theseKeys[-1]  # just the last key pressed
                handButton.rt = handButton.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *darker* updates
        if t >= 0.0 and darker.status == NOT_STARTED:
            # keep track of start time/frame for later
            darker.tStart = t  # underestimates by a little under one frame
            darker.frameNStart = frameN  # exact frame index
            darker.setAutoDraw(True)
        
        # *lighter* updates
        if t >= 0.0 and lighter.status == NOT_STARTED:
            # keep track of start time/frame for later
            lighter.tStart = t  # underestimates by a little under one frame
            lighter.frameNStart = frameN  # exact frame index
            lighter.setAutoDraw(True)
        
        # *Pick_hand* updates
        if t >= 0.0 and Pick_hand.status == NOT_STARTED:
            # keep track of start time/frame for later
            Pick_hand.tStart = t  # underestimates by a little under one frame
            Pick_hand.frameNStart = frameN  # exact frame index
            Pick_hand.setAutoDraw(True)
        
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pickhandComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "pickhand"-------
    for thisComponent in pickhandComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if handButton.keys in ['', [], None]:  # No response was made
       handButton.keys=None
    # store data for pickother (TrialHandler)
    pickother.addData('handButton.keys',handButton.keys)
    if handButton.keys != None:  # we had a response
        pickother.addData('handButton.rt', handButton.rt)
    if handButton.keys == 'v':
        splayer =1
        sgrab = 'hands/sgrab_darker.png'
        sreach = 'hands/sreach_darker.png'
        shand = 'hands/shand_dark.png'
    elif handButton.keys == 'b':
        splayer = 2
        sgrab = 'hands/sgrab_lighter.png'
        sreach = 'hands/sreach_lighter.png'
        shand = 'hands/shand_light.png'
    thisExp.nextEntry()
    
# completed 1 repeats of 'pickother'

# get names of stimulus parameters
if pickother.trialList in ([], [None], None):  params = []
else:  params = pickother.trialList[0].keys()
# save data for this loop
pickother.saveAsExcel(filename + '.xlsx', sheetName='pickother',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
pickother.saveAsText(filename + 'pickother.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
instructions = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath='C:\\Users\\lab\\Desktop\\Alcohol\\InferenceTask\\InferenceTask_keyboard.psyexp',
    trialList=[None],
    seed=None, name='instructions')
thisExp.addLoop(instructions)  # add the loop to the experiment
thisInstruction = instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisInstruction.rgb)
if thisInstruction != None:
    for paramName in thisInstruction.keys():
        exec(paramName + '= thisInstruction.' + paramName)

for thisInstruction in instructions:
    currentLoop = instructions
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
    if thisInstruction != None:
        for paramName in thisInstruction.keys():
            exec(paramName + '= thisInstruction.' + paramName)
    
    #------Prepare to start Routine "Ins_intro"-------
    t = 0
    Ins_introClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if compplayer == 1: 
       compFace = 'faces/04c.jpg'
    if compplayer == 2: 
        compFace = 'faces/30c.jpg'
    if compplayer == 3: 
       compFace = 'faces/11c.jpg'
    if compplayer == 4: 
       compFace = 'faces/06c.jpg'
    chosen_other.setImage(compFace)
    key_resp_0 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_0.status = NOT_STARTED
    # keep track of which components have finished
    Ins_introComponents = []
    Ins_introComponents.append(ins_0)
    Ins_introComponents.append(press_0)
    Ins_introComponents.append(chosen_other)
    Ins_introComponents.append(key_resp_0)
    for thisComponent in Ins_introComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Ins_intro"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Ins_introClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *ins_0* updates
        if t >= 0.0 and ins_0.status == NOT_STARTED:
            # keep track of start time/frame for later
            ins_0.tStart = t  # underestimates by a little under one frame
            ins_0.frameNStart = frameN  # exact frame index
            ins_0.setAutoDraw(True)
        
        # *press_0* updates
        if t >= 0.5 and press_0.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_0.tStart = t  # underestimates by a little under one frame
            press_0.frameNStart = frameN  # exact frame index
            press_0.setAutoDraw(True)
        
        # *chosen_other* updates
        if t >= 0.0 and chosen_other.status == NOT_STARTED:
            # keep track of start time/frame for later
            chosen_other.tStart = t  # underestimates by a little under one frame
            chosen_other.frameNStart = frameN  # exact frame index
            chosen_other.setAutoDraw(True)
        
        # *key_resp_0* updates
        if t >= 0.5 and key_resp_0.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_0.tStart = t  # underestimates by a little under one frame
            key_resp_0.frameNStart = frameN  # exact frame index
            key_resp_0.status = STARTED
            # keyboard checking is just starting
            key_resp_0.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_0.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_0.keys = theseKeys[-1]  # just the last key pressed
                key_resp_0.rt = key_resp_0.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Ins_introComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "Ins_intro"-------
    for thisComponent in Ins_introComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_0.keys in ['', [], None]:  # No response was made
       key_resp_0.keys=None
    # store data for instructions (TrialHandler)
    instructions.addData('key_resp_0.keys',key_resp_0.keys)
    if key_resp_0.keys != None:  # we had a response
        instructions.addData('key_resp_0.rt', key_resp_0.rt)
    
    #------Prepare to start Routine "fix_i"-------
    t = 0
    fix_iClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    yBucket=1
    bucketText_i1.setText('demo\nbucket')
    key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_4.status = NOT_STARTED
    # keep track of which components have finished
    fix_iComponents = []
    fix_iComponents.append(bucket_i1)
    fix_iComponents.append(bucketText_i1)
    fix_iComponents.append(ins1)
    fix_iComponents.append(press_1)
    fix_iComponents.append(key_resp_4)
    for thisComponent in fix_iComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "fix_i"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = fix_iClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if yBucket>.5:
            yBucket=1-frameN/20
        
        
        
        # *bucket_i1* updates
        if t >= 0 and bucket_i1.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucket_i1.tStart = t  # underestimates by a little under one frame
            bucket_i1.frameNStart = frameN  # exact frame index
            bucket_i1.setAutoDraw(True)
        if bucket_i1.status == STARTED:  # only update if being drawn
            bucket_i1.setPos([xBucket,yBucket], log=False)
        
        # *bucketText_i1* updates
        if t >= 0.0 and bucketText_i1.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucketText_i1.tStart = t  # underestimates by a little under one frame
            bucketText_i1.frameNStart = frameN  # exact frame index
            bucketText_i1.setAutoDraw(True)
        if bucketText_i1.status == STARTED:  # only update if being drawn
            bucketText_i1.setPos([0, yBucket], log=False)
        
        # *ins1* updates
        if t >= 0.0 and ins1.status == NOT_STARTED:
            # keep track of start time/frame for later
            ins1.tStart = t  # underestimates by a little under one frame
            ins1.frameNStart = frameN  # exact frame index
            ins1.setAutoDraw(True)
        
        # *press_1* updates
        if t >= 1 and press_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_1.tStart = t  # underestimates by a little under one frame
            press_1.frameNStart = frameN  # exact frame index
            press_1.setAutoDraw(True)
        
        # *key_resp_4* updates
        if t >= 1 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t  # underestimates by a little under one frame
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fix_iComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "fix_i"-------
    for thisComponent in fix_iComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    #------Prepare to start Routine "shake_i"-------
    t = 0
    shake_iClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    orie = 0
    bucketText_i2.setPos([0, yBucket])
    key_resp_5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_5.status = NOT_STARTED
    # keep track of which components have finished
    shake_iComponents = []
    shake_iComponents.append(bucket_i2)
    shake_iComponents.append(bucketText_i2)
    shake_iComponents.append(ins2)
    shake_iComponents.append(press_2)
    shake_iComponents.append(key_resp_5)
    for thisComponent in shake_iComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "shake_i"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = shake_iClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        orie = random.randint(-5,5)
        
        # *bucket_i2* updates
        if t >= 0.0 and bucket_i2.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucket_i2.tStart = t  # underestimates by a little under one frame
            bucket_i2.frameNStart = frameN  # exact frame index
            bucket_i2.setAutoDraw(True)
        if bucket_i2.status == STARTED:  # only update if being drawn
            bucket_i2.setPos([xBucket,yBucket], log=False)
            bucket_i2.setOri(orie, log=False)
        
        # *bucketText_i2* updates
        if t >= 0.0 and bucketText_i2.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucketText_i2.tStart = t  # underestimates by a little under one frame
            bucketText_i2.frameNStart = frameN  # exact frame index
            bucketText_i2.setAutoDraw(True)
        if bucketText_i2.status == STARTED:  # only update if being drawn
            bucketText_i2.setOri(orie, log=False)
        
        # *ins2* updates
        if t >= 0.0 and ins2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ins2.tStart = t  # underestimates by a little under one frame
            ins2.frameNStart = frameN  # exact frame index
            ins2.setAutoDraw(True)
        
        # *press_2* updates
        if t >= 0.5 and press_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_2.tStart = t  # underestimates by a little under one frame
            press_2.frameNStart = frameN  # exact frame index
            press_2.setAutoDraw(True)
        
        # *key_resp_5* updates
        if t >= 0.5 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t  # underestimates by a little under one frame
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in shake_iComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "shake_i"-------
    for thisComponent in shake_iComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    #------Prepare to start Routine "reach_i"-------
    t = 0
    reach_iClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    xcReach=-0.1
    yReach=1.2
    xsReach=0.1
    
    randomJelLoc=random.sample(set([1, 2]), 2)
    if randomJelLoc ==[1,2]:
        jellyLocCondition=1
        leftJellyv="red_choice_s.png"
        rightJellyv="blue_choice_s.png"
    else:
        jellyLocCondition=2
        leftJellyv="red_choice_s.png"
        rightJellyv="blue_choice_s.png"
    
    ComputerReach_i.setImage(compreach)
    SubjectReach_i.setImage(sreach)
    bucket_i3.setPos([0,yBucket])
    bucketText_i3.setPos([0, yBucket])
    # keep track of which components have finished
    reach_iComponents = []
    reach_iComponents.append(ComputerReach_i)
    reach_iComponents.append(SubjectReach_i)
    reach_iComponents.append(bucket_i3)
    reach_iComponents.append(ins_i3)
    reach_iComponents.append(bucketText_i3)
    for thisComponent in reach_iComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "reach_i"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = reach_iClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        yReach=1.2-frameN/30
        if yReach < 0.8:
            continueRoutine=False
        
        # *ComputerReach_i* updates
        if t >= 0.0 and ComputerReach_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            ComputerReach_i.tStart = t  # underestimates by a little under one frame
            ComputerReach_i.frameNStart = frameN  # exact frame index
            ComputerReach_i.setAutoDraw(True)
        if ComputerReach_i.status == STARTED:  # only update if being drawn
            ComputerReach_i.setPos([xcReach,yReach], log=False)
        
        # *SubjectReach_i* updates
        if t >= 0.0 and SubjectReach_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            SubjectReach_i.tStart = t  # underestimates by a little under one frame
            SubjectReach_i.frameNStart = frameN  # exact frame index
            SubjectReach_i.setAutoDraw(True)
        if SubjectReach_i.status == STARTED:  # only update if being drawn
            SubjectReach_i.setPos([xsReach, yReach], log=False)
        
        # *bucket_i3* updates
        if t >= 0.0 and bucket_i3.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucket_i3.tStart = t  # underestimates by a little under one frame
            bucket_i3.frameNStart = frameN  # exact frame index
            bucket_i3.setAutoDraw(True)
        
        # *ins_i3* updates
        if t >= 0.0 and ins_i3.status == NOT_STARTED:
            # keep track of start time/frame for later
            ins_i3.tStart = t  # underestimates by a little under one frame
            ins_i3.frameNStart = frameN  # exact frame index
            ins_i3.setAutoDraw(True)
        
        # *bucketText_i3* updates
        if t >= 0.0 and bucketText_i3.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucketText_i3.tStart = t  # underestimates by a little under one frame
            bucketText_i3.frameNStart = frameN  # exact frame index
            bucketText_i3.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reach_iComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "reach_i"-------
    for thisComponent in reach_iComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    
    #------Prepare to start Routine "grab_i"-------
    t = 0
    grab_iClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    ycReach= yReach
    ComputerGrab_i4.setImage(compgrab)
    grab_subject_i4.setImage(sgrab)
    bucket_i4.setPos([0, yBucket])
    press_i4.setText('press key to continue')
    bucketText_i4.setPos([0, yBucket])
    key_resp_i4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_i4.status = NOT_STARTED
    # keep track of which components have finished
    grab_iComponents = []
    grab_iComponents.append(ComputerGrab_i4)
    grab_iComponents.append(grab_subject_i4)
    grab_iComponents.append(bucket_i4)
    grab_iComponents.append(ins_i4)
    grab_iComponents.append(press_i4)
    grab_iComponents.append(bucketText_i4)
    grab_iComponents.append(key_resp_i4)
    for thisComponent in grab_iComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "grab_i"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = grab_iClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if ycReach<1.2:
            ycReach=0.8+frameN/30
        
        
        # *ComputerGrab_i4* updates
        if t >= 0.0 and ComputerGrab_i4.status == NOT_STARTED:
            # keep track of start time/frame for later
            ComputerGrab_i4.tStart = t  # underestimates by a little under one frame
            ComputerGrab_i4.frameNStart = frameN  # exact frame index
            ComputerGrab_i4.setAutoDraw(True)
        if ComputerGrab_i4.status == STARTED:  # only update if being drawn
            ComputerGrab_i4.setPos([xcReach,ycReach], log=False)
        
        # *grab_subject_i4* updates
        if t >= 0.0 and grab_subject_i4.status == NOT_STARTED:
            # keep track of start time/frame for later
            grab_subject_i4.tStart = t  # underestimates by a little under one frame
            grab_subject_i4.frameNStart = frameN  # exact frame index
            grab_subject_i4.setAutoDraw(True)
        if grab_subject_i4.status == STARTED:  # only update if being drawn
            grab_subject_i4.setPos([xsReach, ycReach], log=False)
        
        # *bucket_i4* updates
        if t >= 0.0 and bucket_i4.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucket_i4.tStart = t  # underestimates by a little under one frame
            bucket_i4.frameNStart = frameN  # exact frame index
            bucket_i4.setAutoDraw(True)
        
        # *ins_i4* updates
        if t >= 0.0 and ins_i4.status == NOT_STARTED:
            # keep track of start time/frame for later
            ins_i4.tStart = t  # underestimates by a little under one frame
            ins_i4.frameNStart = frameN  # exact frame index
            ins_i4.setAutoDraw(True)
        
        # *press_i4* updates
        if t >= 1 and press_i4.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_i4.tStart = t  # underestimates by a little under one frame
            press_i4.frameNStart = frameN  # exact frame index
            press_i4.setAutoDraw(True)
        
        # *bucketText_i4* updates
        if t >= 0.0 and bucketText_i4.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucketText_i4.tStart = t  # underestimates by a little under one frame
            bucketText_i4.frameNStart = frameN  # exact frame index
            bucketText_i4.setAutoDraw(True)
        
        # *key_resp_i4* updates
        if t >= 1 and key_resp_i4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_i4.tStart = t  # underestimates by a little under one frame
            key_resp_i4.frameNStart = frameN  # exact frame index
            key_resp_i4.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_i4.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in grab_iComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "grab_i"-------
    for thisComponent in grab_iComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    #------Prepare to start Routine "CompOutcome_i"-------
    t = 0
    CompOutcome_iClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    ycompHand= -1.6
    
    bucket_i5.setPos([0, yBucket])
    compHandUp_2.setImage(comphand)
    compHandUp_2.setSize([handw, handh])
    ins_i5.setText('Your partner looks at ' + pronoun + ' sample from the bucket.\n\nYou can not see '+pronoun +' sample \nand '+ pronoun2 +' does not see yours.')
    bucketText_i5.setPos([0, yBucket-.15])
    leftjelly_i5.setImage(leftJellyv)
    rightjelly_i5.setImage(rightJellyv)
    key_resp_i5 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_i5.status = NOT_STARTED
    # keep track of which components have finished
    CompOutcome_iComponents = []
    CompOutcome_iComponents.append(bucket_i5)
    CompOutcome_iComponents.append(cartoon_3)
    CompOutcome_iComponents.append(compHandUp_2)
    CompOutcome_iComponents.append(ins_i5)
    CompOutcome_iComponents.append(bucketText_i5)
    CompOutcome_iComponents.append(leftjelly_i5)
    CompOutcome_iComponents.append(rightjelly_i5)
    CompOutcome_iComponents.append(press_i5)
    CompOutcome_iComponents.append(key_resp_i5)
    for thisComponent in CompOutcome_iComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "CompOutcome_i"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = CompOutcome_iClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        ycompHand= -1.6 + frameN/15
        if ycompHand> -.6:
            continueRoutine=False
        
        # *bucket_i5* updates
        if t >= 0.0 and bucket_i5.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucket_i5.tStart = t  # underestimates by a little under one frame
            bucket_i5.frameNStart = frameN  # exact frame index
            bucket_i5.setAutoDraw(True)
        
        # *cartoon_3* updates
        if t >= 0.0 and cartoon_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            cartoon_3.tStart = t  # underestimates by a little under one frame
            cartoon_3.frameNStart = frameN  # exact frame index
            cartoon_3.setAutoDraw(True)
        
        # *compHandUp_2* updates
        if t >= 0.0 and compHandUp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            compHandUp_2.tStart = t  # underestimates by a little under one frame
            compHandUp_2.frameNStart = frameN  # exact frame index
            compHandUp_2.setAutoDraw(True)
        if compHandUp_2.status == STARTED:  # only update if being drawn
            compHandUp_2.setPos([xcompHand,ycompHand], log=False)
            compHandUp_2.setOri(0, log=False)
        
        # *ins_i5* updates
        if t >= 0.0 and ins_i5.status == NOT_STARTED:
            # keep track of start time/frame for later
            ins_i5.tStart = t  # underestimates by a little under one frame
            ins_i5.frameNStart = frameN  # exact frame index
            ins_i5.setAutoDraw(True)
        
        # *bucketText_i5* updates
        if t >= 0.0 and bucketText_i5.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucketText_i5.tStart = t  # underestimates by a little under one frame
            bucketText_i5.frameNStart = frameN  # exact frame index
            bucketText_i5.setAutoDraw(True)
        
        # *leftjelly_i5* updates
        if t >= 0.0 and leftjelly_i5.status == NOT_STARTED:
            # keep track of start time/frame for later
            leftjelly_i5.tStart = t  # underestimates by a little under one frame
            leftjelly_i5.frameNStart = frameN  # exact frame index
            leftjelly_i5.setAutoDraw(True)
        
        # *rightjelly_i5* updates
        if t >= 0.0 and rightjelly_i5.status == NOT_STARTED:
            # keep track of start time/frame for later
            rightjelly_i5.tStart = t  # underestimates by a little under one frame
            rightjelly_i5.frameNStart = frameN  # exact frame index
            rightjelly_i5.setAutoDraw(True)
        
        # *press_i5* updates
        if t >= 1 and press_i5.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_i5.tStart = t  # underestimates by a little under one frame
            press_i5.frameNStart = frameN  # exact frame index
            press_i5.setAutoDraw(True)
        
        # *key_resp_i5* updates
        if t >= 1 and key_resp_i5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_i5.tStart = t  # underestimates by a little under one frame
            key_resp_i5.frameNStart = frameN  # exact frame index
            key_resp_i5.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_i5.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CompOutcome_iComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "CompOutcome_i"-------
    for thisComponent in CompOutcome_iComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    leftjelly_i5.setAutoDraw(True)
    rightjelly_i5.setAutoDraw(True)
    
    
    #------Prepare to start Routine "compface_i"-------
    t = 0
    compface_iClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if compplayer == 1: 
       compFace = 'faces/04uc.jpg'
    if compplayer == 2: 
       compFace = 'faces/30uc.jpg'
    if compplayer == 3: 
       compFace = 'faces/11uc.jpg'
    if compplayer == 4: 
       compFace = 'faces/06uc.jpg'
    
    showCompChoice="red_choice_s.png"
    
    ycomphandorig  = ycompHand
    ins_i6.setText('Based on ' + pronoun + ' sample, '+ pronoun2 + ' guesses what is inside the bucket and expresses '
+ pronoun+' confidence in that guess.'
)
    ComputerFace_i6.setImage(compFace)
    bucket_i6.setPos([0, yBucket])
    CompBeanChoice_i6.setImage(showCompChoice)
    CompBeanChoice_i6.setSize([0.2, 0.25])
    compHand_i6.setImage(comphand)
    compHand_i6.setSize([handw, handh])
    key_resp_10 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_10.status = NOT_STARTED
    # keep track of which components have finished
    compface_iComponents = []
    compface_iComponents.append(ins_i6)
    compface_iComponents.append(ComputerFace_i6)
    compface_iComponents.append(bucket_i6)
    compface_iComponents.append(CompBeanChoice_i6)
    compface_iComponents.append(compHand_i6)
    compface_iComponents.append(press_i6)
    compface_iComponents.append(key_resp_10)
    for thisComponent in compface_iComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "compface_i"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = compface_iClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if ycompHand > -1:
            ycompHand = ycompHand - .1
        
        
        
        # *ins_i6* updates
        if t >= 0.0 and ins_i6.status == NOT_STARTED:
            # keep track of start time/frame for later
            ins_i6.tStart = t  # underestimates by a little under one frame
            ins_i6.frameNStart = frameN  # exact frame index
            ins_i6.setAutoDraw(True)
        
        # *ComputerFace_i6* updates
        if t >= 0 and ComputerFace_i6.status == NOT_STARTED:
            # keep track of start time/frame for later
            ComputerFace_i6.tStart = t  # underestimates by a little under one frame
            ComputerFace_i6.frameNStart = frameN  # exact frame index
            ComputerFace_i6.setAutoDraw(True)
        
        # *bucket_i6* updates
        if t >= 0.0 and bucket_i6.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucket_i6.tStart = t  # underestimates by a little under one frame
            bucket_i6.frameNStart = frameN  # exact frame index
            bucket_i6.setAutoDraw(True)
        
        # *CompBeanChoice_i6* updates
        if t >= 0.0 and CompBeanChoice_i6.status == NOT_STARTED:
            # keep track of start time/frame for later
            CompBeanChoice_i6.tStart = t  # underestimates by a little under one frame
            CompBeanChoice_i6.frameNStart = frameN  # exact frame index
            CompBeanChoice_i6.setAutoDraw(True)
        
        # *compHand_i6* updates
        if t >= 0.0 and compHand_i6.status == NOT_STARTED:
            # keep track of start time/frame for later
            compHand_i6.tStart = t  # underestimates by a little under one frame
            compHand_i6.frameNStart = frameN  # exact frame index
            compHand_i6.setAutoDraw(True)
        if compHand_i6.status == STARTED:  # only update if being drawn
            compHand_i6.setPos([xcompHand,ycompHand], log=False)
            compHand_i6.setOri(0, log=False)
        
        # *press_i6* updates
        if t >= 2 and press_i6.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_i6.tStart = t  # underestimates by a little under one frame
            press_i6.frameNStart = frameN  # exact frame index
            press_i6.setAutoDraw(True)
        
        # *key_resp_10* updates
        if t >= 2 and key_resp_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_10.tStart = t  # underestimates by a little under one frame
            key_resp_10.frameNStart = frameN  # exact frame index
            key_resp_10.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_10.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in compface_iComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "compface_i"-------
    for thisComponent in compface_iComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    ComputerFace_i6.setAutoDraw(True)
    CompBeanChoice_i6.setAutoDraw(True)
    
    
    
    #------Prepare to start Routine "SubOutcome_i"-------
    t = 0
    SubOutcome_iClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    xReach=0.5
    yReach = -1.2
    
    # now set the jellys in the subject's hand
    jellycond = 4
    
    if jellycond == 0: 
        jellylist=['jb_blue.png','jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
    elif jellycond == 1:
        jellylist=['jb_red.png','jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
    elif jellycond == 2:
        jellylist=['jb_red.png','jb_red.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
    elif jellycond == 3:
        jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
    elif jellycond == 4:
        jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
    elif jellycond == 5:
        jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
    elif jellycond == 6:
        jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_blue.png', 'jb_blue.png']
    elif jellycond == 7:
        jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png','jb_red.png', 'jb_blue.png']
    elif jellycond == 8:
        jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png']
    
    shuffle(jellylist)
    jellyposxset = [.15, .25, .35, .15, .25, .35, .25, .35]
    jelly1 = jellylist.pop()
    jelly2 = jellylist.pop()
    jelly3 = jellylist.pop()
    jelly4 = jellylist.pop()
    jelly5 = jellylist.pop()
    jelly6 = jellylist.pop()
    jelly7 = jellylist.pop()
    jelly8 = jellylist.pop()
    
    subHand_i7.setOri(0)
    subHand_i7.setImage(shand)
    bucket_19.setPos([0, yBucket])
    sjelly1_2.setOri(random.randint(-15,15))
    sjelly1_2.setImage(jelly1)
    sjelly2_2.setOri(random.randint(-15,15))
    sjelly2_2.setImage(jelly2)
    sjelly3_2.setOri(random.randint(-15,15))
    sjelly3_2.setImage(jelly3)
    sjelly4_2.setOri(random.randint(-15,15))
    sjelly4_2.setImage(jelly4)
    sjelly5_2.setOri(random.randint(-15,15))
    sjelly5_2.setImage(jelly5)
    sjelly6_2.setOri(random.randint(-15,15))
    sjelly6_2.setImage(jelly6)
    sjelly7_2.setOri(random.randint(-15,15))
    sjelly7_2.setImage(jelly7)
    sjelly8_2.setOri(random.randint(-15,15))
    sjelly8_2.setImage(jelly8)
    key_resp_11 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_11.status = NOT_STARTED
    # keep track of which components have finished
    SubOutcome_iComponents = []
    SubOutcome_iComponents.append(subHand_i7)
    SubOutcome_iComponents.append(bucket_19)
    SubOutcome_iComponents.append(sjelly1_2)
    SubOutcome_iComponents.append(sjelly2_2)
    SubOutcome_iComponents.append(sjelly3_2)
    SubOutcome_iComponents.append(sjelly4_2)
    SubOutcome_iComponents.append(sjelly5_2)
    SubOutcome_iComponents.append(sjelly6_2)
    SubOutcome_iComponents.append(sjelly7_2)
    SubOutcome_iComponents.append(sjelly8_2)
    SubOutcome_iComponents.append(ins_i7)
    SubOutcome_iComponents.append(press_i7)
    SubOutcome_iComponents.append(key_resp_11)
    for thisComponent in SubOutcome_iComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "SubOutcome_i"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = SubOutcome_iClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if yReach < -0.6:
            yReach = -1.2 + frameN/20
        
        # *subHand_i7* updates
        if t >= 0.0 and subHand_i7.status == NOT_STARTED:
            # keep track of start time/frame for later
            subHand_i7.tStart = t  # underestimates by a little under one frame
            subHand_i7.frameNStart = frameN  # exact frame index
            subHand_i7.setAutoDraw(True)
        if subHand_i7.status == STARTED:  # only update if being drawn
            subHand_i7.setPos([.25,yReach], log=False)
        
        # *bucket_19* updates
        if t >= 0.0 and bucket_19.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucket_19.tStart = t  # underestimates by a little under one frame
            bucket_19.frameNStart = frameN  # exact frame index
            bucket_19.setAutoDraw(True)
        
        # *sjelly1_2* updates
        if t >= 0.0 and sjelly1_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sjelly1_2.tStart = t  # underestimates by a little under one frame
            sjelly1_2.frameNStart = frameN  # exact frame index
            sjelly1_2.setAutoDraw(True)
        if sjelly1_2.status == STARTED:  # only update if being drawn
            sjelly1_2.setPos([xhand-xadd, yReach], log=False)
        
        # *sjelly2_2* updates
        if t >= 0.0 and sjelly2_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sjelly2_2.tStart = t  # underestimates by a little under one frame
            sjelly2_2.frameNStart = frameN  # exact frame index
            sjelly2_2.setAutoDraw(True)
        if sjelly2_2.status == STARTED:  # only update if being drawn
            sjelly2_2.setPos([xhand, yReach], log=False)
        
        # *sjelly3_2* updates
        if t >= 0.0 and sjelly3_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sjelly3_2.tStart = t  # underestimates by a little under one frame
            sjelly3_2.frameNStart = frameN  # exact frame index
            sjelly3_2.setAutoDraw(True)
        if sjelly3_2.status == STARTED:  # only update if being drawn
            sjelly3_2.setPos([xhand+xadd, yReach], log=False)
        
        # *sjelly4_2* updates
        if t >= 0.0 and sjelly4_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sjelly4_2.tStart = t  # underestimates by a little under one frame
            sjelly4_2.frameNStart = frameN  # exact frame index
            sjelly4_2.setAutoDraw(True)
        if sjelly4_2.status == STARTED:  # only update if being drawn
            sjelly4_2.setPos([xhand-xadd, yReach-yadd], log=False)
        
        # *sjelly5_2* updates
        if t >= 0.0 and sjelly5_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sjelly5_2.tStart = t  # underestimates by a little under one frame
            sjelly5_2.frameNStart = frameN  # exact frame index
            sjelly5_2.setAutoDraw(True)
        if sjelly5_2.status == STARTED:  # only update if being drawn
            sjelly5_2.setPos([xhand, yReach-yadd], log=False)
        
        # *sjelly6_2* updates
        if t >= 0.0 and sjelly6_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sjelly6_2.tStart = t  # underestimates by a little under one frame
            sjelly6_2.frameNStart = frameN  # exact frame index
            sjelly6_2.setAutoDraw(True)
        if sjelly6_2.status == STARTED:  # only update if being drawn
            sjelly6_2.setPos([xhand+xadd, yReach-yadd], log=False)
        
        # *sjelly7_2* updates
        if t >= 0.0 and sjelly7_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sjelly7_2.tStart = t  # underestimates by a little under one frame
            sjelly7_2.frameNStart = frameN  # exact frame index
            sjelly7_2.setAutoDraw(True)
        if sjelly7_2.status == STARTED:  # only update if being drawn
            sjelly7_2.setPos([xhand-xadd/2, yReach-yadd*2], log=False)
        
        # *sjelly8_2* updates
        if t >= 0.0 and sjelly8_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sjelly8_2.tStart = t  # underestimates by a little under one frame
            sjelly8_2.frameNStart = frameN  # exact frame index
            sjelly8_2.setAutoDraw(True)
        if sjelly8_2.status == STARTED:  # only update if being drawn
            sjelly8_2.setPos([xhand+xadd/2, yReach-yadd*2], log=False)
        
        # *ins_i7* updates
        if t >= 0.0 and ins_i7.status == NOT_STARTED:
            # keep track of start time/frame for later
            ins_i7.tStart = t  # underestimates by a little under one frame
            ins_i7.frameNStart = frameN  # exact frame index
            ins_i7.setAutoDraw(True)
        
        # *press_i7* updates
        if t >= 1 and press_i7.status == NOT_STARTED:
            # keep track of start time/frame for later
            press_i7.tStart = t  # underestimates by a little under one frame
            press_i7.frameNStart = frameN  # exact frame index
            press_i7.setAutoDraw(True)
        
        # *key_resp_11* updates
        if t >= 1 and key_resp_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_11.tStart = t  # underestimates by a little under one frame
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_11.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SubOutcome_iComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "SubOutcome_i"-------
    for thisComponent in SubOutcome_iComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    subHand_i7.setAutoDraw(True)
    sjelly1_2.setAutoDraw(True)
    sjelly2_2.setAutoDraw(True)
    sjelly3_2.setAutoDraw(True)
    sjelly4_2.setAutoDraw(True)
    sjelly5_2.setAutoDraw(True)
    sjelly6_2.setAutoDraw(True)
    sjelly7_2.setAutoDraw(True)
    sjelly8_2.setAutoDraw(True)
    
    
    
    
    
    #------Prepare to start Routine "SubChoose_i"-------
    t = 0
    SubChoose_iClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    practiceButton = event.BuilderKeyResponse()  # create an object of type KeyResponse
    practiceButton.status = NOT_STARTED
    responseJelly=""
    chosen=""
    
    subHand_i7.setAutoDraw(True)
    sjelly1_2.setAutoDraw(True)
    sjelly2_2.setAutoDraw(True)
    sjelly3_2.setAutoDraw(True)
    sjelly4_2.setAutoDraw(True)
    sjelly5_2.setAutoDraw(True)
    sjelly6_2.setAutoDraw(True)
    sjelly7_2.setAutoDraw(True)
    sjelly8_2.setAutoDraw(True)
    
    event.clearEvents(eventType= 'keyboard')
    
    bucket_20.setPos([0, yBucket])
    # keep track of which components have finished
    SubChoose_iComponents = []
    SubChoose_iComponents.append(practiceButton)
    SubChoose_iComponents.append(bucket_20)
    SubChoose_iComponents.append(text_6)
    for thisComponent in SubChoose_iComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "SubChoose_i"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = SubChoose_iClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practiceButton* updates
        if t >= 0.0 and practiceButton.status == NOT_STARTED:
            # keep track of start time/frame for later
            practiceButton.tStart = t  # underestimates by a little under one frame
            practiceButton.frameNStart = frameN  # exact frame index
            practiceButton.status = STARTED
            # keyboard checking is just starting
            practiceButton.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if practiceButton.status == STARTED:
            theseKeys = event.getKeys(keyList=['v', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                practiceButton.keys = theseKeys[-1]  # just the last key pressed
                practiceButton.rt = practiceButton.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        
        # *bucket_20* updates
        if t >= 0.0 and bucket_20.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucket_20.tStart = t  # underestimates by a little under one frame
            bucket_20.frameNStart = frameN  # exact frame index
            bucket_20.setAutoDraw(True)
        
        # *text_6* updates
        if t >= 0.0 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t  # underestimates by a little under one frame
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SubChoose_iComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "SubChoose_i"-------
    for thisComponent in SubChoose_iComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if practiceButton.keys in ['', [], None]:  # No response was made
       practiceButton.keys=None
    # store data for instructions (TrialHandler)
    instructions.addData('practiceButton.keys',practiceButton.keys)
    if practiceButton.keys != None:  # we had a response
        instructions.addData('practiceButton.rt', practiceButton.rt)
    keys = event.getKeys(['v', 'b']) 
    keep = 0
    
    #if jellyLocCondition==1:
    if  practiceButton.keys == 'b':
        keep = 1
        responseJelly="red"
        subChoice=1
        responseRT = stopwatch.getTime() 
    if practiceButton.keys == 'v':
        keep = 2
        responseJelly="blue"
        responseRT = stopwatch.getTime() 
        subChoice=0
    
    #else:
    #    if practiceButton.keys == 'v':
    #        keep = 1
    #        responseJelly="blue"
    #        chosen="left"
    #        responseRT = stopwatch.getTime() 
    #        subChoice=0
    #    if practiceButton.keys == 'b':
    #        keep = 2
    #        responseJelly="red"
    #        responseRT = stopwatch.getTime() 
    #        subChoice=1
    
    ComputerFace_i6.setAutoDraw(False)
    compHand_i6.setAutoDraw(False)
    CompBeanChoice_i6.setAutoDraw(False)
    
    subHand_i7.setAutoDraw(False)
    sjelly1_2.setAutoDraw(False)
    sjelly2_2.setAutoDraw(False)
    sjelly3_2.setAutoDraw(False)
    sjelly4_2.setAutoDraw(False)
    sjelly5_2.setAutoDraw(False)
    sjelly6_2.setAutoDraw(False)
    sjelly7_2.setAutoDraw(False)
    sjelly8_2.setAutoDraw(False)
    
    leftjelly_i5.setAutoDraw(False)
    rightjelly_i5.setAutoDraw(False)
    
    
    #------Prepare to start Routine "subFeedback_i"-------
    t = 0
    subFeedback_iClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    bucket_21.setPos([0, yBucket])
    LeftJellyS_i.setImage(leftJellyv)
    LeftJellyS_i.setSize([.2, .25])
    RightJellyS_i.setImage(rightJellyv)
    RightJellyS_i.setSize([.2, .25])
    
    key_resp_9 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_9.status = NOT_STARTED
    # keep track of which components have finished
    subFeedback_iComponents = []
    subFeedback_iComponents.append(bucket_21)
    subFeedback_iComponents.append(LeftJellyS_i)
    subFeedback_iComponents.append(RightJellyS_i)
    subFeedback_iComponents.append(key_resp_9)
    subFeedback_iComponents.append(goodjob)
    for thisComponent in subFeedback_iComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "subFeedback_i"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = subFeedback_iClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *bucket_21* updates
        if t >= 0.0 and bucket_21.status == NOT_STARTED:
            # keep track of start time/frame for later
            bucket_21.tStart = t  # underestimates by a little under one frame
            bucket_21.frameNStart = frameN  # exact frame index
            bucket_21.setAutoDraw(True)
        
        # *LeftJellyS_i* updates
        if (keep==1) and LeftJellyS_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            LeftJellyS_i.tStart = t  # underestimates by a little under one frame
            LeftJellyS_i.frameNStart = frameN  # exact frame index
            LeftJellyS_i.setAutoDraw(True)
        
        # *RightJellyS_i* updates
        if (keep==2) and RightJellyS_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            RightJellyS_i.tStart = t  # underestimates by a little under one frame
            RightJellyS_i.frameNStart = frameN  # exact frame index
            RightJellyS_i.setAutoDraw(True)
        
        
        # *key_resp_9* updates
        if t >= 0.0 and key_resp_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_9.tStart = t  # underestimates by a little under one frame
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            key_resp_9.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_9.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_9.keys = theseKeys[-1]  # just the last key pressed
                key_resp_9.rt = key_resp_9.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *goodjob* updates
        if t >= 0.0 and goodjob.status == NOT_STARTED:
            # keep track of start time/frame for later
            goodjob.tStart = t  # underestimates by a little under one frame
            goodjob.frameNStart = frameN  # exact frame index
            goodjob.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in subFeedback_iComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "subFeedback_i"-------
    for thisComponent in subFeedback_iComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    LeftJellyS_i.setAutoDraw(False)
    RightJellyS_i.setAutoDraw(False)
    
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
       key_resp_9.keys=None
    # store data for instructions (TrialHandler)
    instructions.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        instructions.addData('key_resp_9.rt', key_resp_9.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'instructions'

# get names of stimulus parameters
if instructions.trialList in ([], [None], None):  params = []
else:  params = instructions.trialList[0].keys()
# save data for this loop
instructions.saveAsExcel(filename + '.xlsx', sheetName='instructions',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
instructions.saveAsText(filename + 'instructions.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# set up handler to look after randomisation of conditions etc
social_urn_loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath='C:\\Users\\lab\\Desktop\\Alcohol\\InferenceTask\\InferenceTask_keyboard.psyexp',
    trialList=data.importConditions('filelists\\loop_big.xlsx'),
    seed=None, name='social_urn_loop')
thisExp.addLoop(social_urn_loop)  # add the loop to the experiment
thisSocial_urn_loop = social_urn_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisSocial_urn_loop.rgb)
if thisSocial_urn_loop != None:
    for paramName in thisSocial_urn_loop.keys():
        exec(paramName + '= thisSocial_urn_loop.' + paramName)

for thisSocial_urn_loop in social_urn_loop:
    currentLoop = social_urn_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSocial_urn_loop.rgb)
    if thisSocial_urn_loop != None:
        for paramName in thisSocial_urn_loop.keys():
            exec(paramName + '= thisSocial_urn_loop.' + paramName)
    
    #------Prepare to start Routine "thiscounts"-------
    t = 0
    thiscountsClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if n < 6:
        msgp = 'This is practice. \n\n\nPress any key to continue.'
    else:
        msgp = 'The next trials count! \n\nRespond as quickly and accurately as possible. \n\n\nPress any key to continue.'
    
    
    text_4.setText(msgp)
    key_resp_12 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_12.status = NOT_STARTED
    # keep track of which components have finished
    thiscountsComponents = []
    thiscountsComponents.append(text_4)
    thiscountsComponents.append(key_resp_12)
    for thisComponent in thiscountsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "thiscounts"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = thiscountsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        
        # *key_resp_12* updates
        if t >= 0.0 and key_resp_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_12.tStart = t  # underestimates by a little under one frame
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            key_resp_12.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_12.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_12.keys = theseKeys[-1]  # just the last key pressed
                key_resp_12.rt = key_resp_12.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thiscountsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "thiscounts"-------
    for thisComponent in thiscountsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_12.keys in ['', [], None]:  # No response was made
       key_resp_12.keys=None
    # store data for social_urn_loop (TrialHandler)
    social_urn_loop.addData('key_resp_12.keys',key_resp_12.keys)
    if key_resp_12.keys != None:  # we had a response
        social_urn_loop.addData('key_resp_12.rt', key_resp_12.rt)
    
    # set up handler to look after randomisation of conditions etc
    social_urn_trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath='C:\\Users\\lab\\Desktop\\Alcohol\\InferenceTask\\InferenceTask_keyboard.psyexp',
        trialList=data.importConditions(conditionFile),
        seed=None, name='social_urn_trials')
    thisExp.addLoop(social_urn_trials)  # add the loop to the experiment
    thisSocial_urn_trial = social_urn_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisSocial_urn_trial.rgb)
    if thisSocial_urn_trial != None:
        for paramName in thisSocial_urn_trial.keys():
            exec(paramName + '= thisSocial_urn_trial.' + paramName)
    
    for thisSocial_urn_trial in social_urn_trials:
        currentLoop = social_urn_trials
        # abbreviate parameter names if possible (e.g. rgb = thisSocial_urn_trial.rgb)
        if thisSocial_urn_trial != None:
            for paramName in thisSocial_urn_trial.keys():
                exec(paramName + '= thisSocial_urn_trial.' + paramName)
        
        #------Prepare to start Routine "fixation"-------
        t = 0
        fixationClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        yBucket=1
        bucketNumber=bucketNumber+1
        if bucketNumber ==1:
            stopwatch2 = core.Clock()
            start = stopwatch2.getTime()
        time_fixation = stopwatch2.getTime()
        
        n = n + 1
        
        if n < 7:
            bucketName = 'Practice'
        else:
            bucketName = 'Bucket ' + str(n-6)
        
        
        
        BucketText1.setText(bucketName)
        # keep track of which components have finished
        fixationComponents = []
        fixationComponents.append(bucket)
        fixationComponents.append(BucketText1)
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "fixation"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = fixationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            yBucket=1-frameN/20
            if yBucket<.55:
                continueRoutine=False
            
            
            # *bucket* updates
            if t >= 0.0 and bucket.status == NOT_STARTED:
                # keep track of start time/frame for later
                bucket.tStart = t  # underestimates by a little under one frame
                bucket.frameNStart = frameN  # exact frame index
                bucket.setAutoDraw(True)
            if bucket.status == STARTED:  # only update if being drawn
                bucket.setPos([xBucket,yBucket], log=False)
            
            # *BucketText1* updates
            if t >= 0.0 and BucketText1.status == NOT_STARTED:
                # keep track of start time/frame for later
                BucketText1.tStart = t  # underestimates by a little under one frame
                BucketText1.frameNStart = frameN  # exact frame index
                BucketText1.setAutoDraw(True)
            if BucketText1.status == STARTED:  # only update if being drawn
                BucketText1.setPos([xBucket, yBucket], log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "fixation"-------
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        #------Prepare to start Routine "fixshaker"-------
        t = 0
        fixshakerClock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.400000)
        # update component parameters for each repeat
        orie = 0
        BucketText2.setText(bucketName)
        # keep track of which components have finished
        fixshakerComponents = []
        fixshakerComponents.append(bucket2)
        fixshakerComponents.append(BucketText2)
        for thisComponent in fixshakerComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "fixshaker"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = fixshakerClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            orie = random.randint(-5,5)
            
            # *bucket2* updates
            if t >= 0.0 and bucket2.status == NOT_STARTED:
                # keep track of start time/frame for later
                bucket2.tStart = t  # underestimates by a little under one frame
                bucket2.frameNStart = frameN  # exact frame index
                bucket2.setAutoDraw(True)
            elif bucket2.status == STARTED and t >= (0.0 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                bucket2.setAutoDraw(False)
            if bucket2.status == STARTED:  # only update if being drawn
                bucket2.setPos([xBucket,yBucket], log=False)
                bucket2.setOri(orie, log=False)
            
            # *BucketText2* updates
            if t >= 0.0 and BucketText2.status == NOT_STARTED:
                # keep track of start time/frame for later
                BucketText2.tStart = t  # underestimates by a little under one frame
                BucketText2.frameNStart = frameN  # exact frame index
                BucketText2.setAutoDraw(True)
            elif BucketText2.status == STARTED and t >= (0.0 + (0.4-win.monitorFramePeriod*0.75)): #most of one frame period left
                BucketText2.setAutoDraw(False)
            if BucketText2.status == STARTED:  # only update if being drawn
                BucketText2.setPos([xBucket, yBucket], log=False)
                BucketText2.setOri(orie, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixshakerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "fixshaker"-------
        for thisComponent in fixshakerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        #------Prepare to start Routine "Reach"-------
        t = 0
        ReachClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        time_Reach = stopwatch2.getTime()
        
        xcReach=-0.1
        yReach=1.2
        xsReach=0.1
        
        randomJelLoc=random.sample(set([1, 2]), 2)
        if randomJelLoc ==[1,2]:
            jellyLocCondition=1
            leftJellyv="jb_red.png"
            rightJellyv="jb_blue.png"
        else:
            jellyLocCondition=2
            leftJellyv="jb_blue.png"
            rightJellyv="jb_red.png"
        
        
        ComputerReach.setImage(compreach)
        SubjectReach.setImage(sreach)
        bucket3.setPos([0,yBucket])
        BucketText3.setText(bucketName)
        BucketText3.setPos([0, yBucket])
        # keep track of which components have finished
        ReachComponents = []
        ReachComponents.append(ComputerReach)
        ReachComponents.append(SubjectReach)
        ReachComponents.append(bucket3)
        ReachComponents.append(BucketText3)
        for thisComponent in ReachComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Reach"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = ReachClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            yReach = 1.2 - frameN/20
            if yReach < 0.8:
                continueRoutine=False
            
            # *ComputerReach* updates
            if t >= 0.0 and ComputerReach.status == NOT_STARTED:
                # keep track of start time/frame for later
                ComputerReach.tStart = t  # underestimates by a little under one frame
                ComputerReach.frameNStart = frameN  # exact frame index
                ComputerReach.setAutoDraw(True)
            if ComputerReach.status == STARTED:  # only update if being drawn
                ComputerReach.setPos([xcReach,yReach], log=False)
            
            # *SubjectReach* updates
            if t >= 0.0 and SubjectReach.status == NOT_STARTED:
                # keep track of start time/frame for later
                SubjectReach.tStart = t  # underestimates by a little under one frame
                SubjectReach.frameNStart = frameN  # exact frame index
                SubjectReach.setAutoDraw(True)
            if SubjectReach.status == STARTED:  # only update if being drawn
                SubjectReach.setPos([xsReach, yReach], log=False)
            
            # *bucket3* updates
            if t >= 0.0 and bucket3.status == NOT_STARTED:
                # keep track of start time/frame for later
                bucket3.tStart = t  # underestimates by a little under one frame
                bucket3.frameNStart = frameN  # exact frame index
                bucket3.setAutoDraw(True)
            
            # *BucketText3* updates
            if t >= 0.0 and BucketText3.status == NOT_STARTED:
                # keep track of start time/frame for later
                BucketText3.tStart = t  # underestimates by a little under one frame
                BucketText3.frameNStart = frameN  # exact frame index
                BucketText3.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ReachComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "Reach"-------
        for thisComponent in ReachComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        #------Prepare to start Routine "Grab"-------
        t = 0
        GrabClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        
        ComputerGrab.setImage(compgrab)
        grab_subject.setImage(sgrab)
        bucket4.setPos([0, yBucket])
        BucketText4.setText(bucketName)
        BucketText4.setPos([0, yBucket])
        # keep track of which components have finished
        GrabComponents = []
        GrabComponents.append(ComputerGrab)
        GrabComponents.append(grab_subject)
        GrabComponents.append(bucket4)
        GrabComponents.append(BucketText4)
        for thisComponent in GrabComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Grab"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = GrabClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            ycReach=0.8+frameN/30
            if ycReach>1.2:
                continueRoutine=False
            
            
            # *ComputerGrab* updates
            if t >= 0.0 and ComputerGrab.status == NOT_STARTED:
                # keep track of start time/frame for later
                ComputerGrab.tStart = t  # underestimates by a little under one frame
                ComputerGrab.frameNStart = frameN  # exact frame index
                ComputerGrab.setAutoDraw(True)
            if ComputerGrab.status == STARTED:  # only update if being drawn
                ComputerGrab.setPos([xcReach,ycReach], log=False)
            
            # *grab_subject* updates
            if t >= 0.0 and grab_subject.status == NOT_STARTED:
                # keep track of start time/frame for later
                grab_subject.tStart = t  # underestimates by a little under one frame
                grab_subject.frameNStart = frameN  # exact frame index
                grab_subject.setAutoDraw(True)
            if grab_subject.status == STARTED:  # only update if being drawn
                grab_subject.setPos([xsReach, ycReach], log=False)
            
            # *bucket4* updates
            if t >= 0.0 and bucket4.status == NOT_STARTED:
                # keep track of start time/frame for later
                bucket4.tStart = t  # underestimates by a little under one frame
                bucket4.frameNStart = frameN  # exact frame index
                bucket4.setAutoDraw(True)
            
            # *BucketText4* updates
            if t >= 0.0 and BucketText4.status == NOT_STARTED:
                # keep track of start time/frame for later
                BucketText4.tStart = t  # underestimates by a little under one frame
                BucketText4.frameNStart = frameN  # exact frame index
                BucketText4.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in GrabComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "Grab"-------
        for thisComponent in GrabComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        #------Prepare to start Routine "CompOutcome"-------
        t = 0
        CompOutcomeClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        time_CompOutcome = stopwatch2.getTime()
        
        ycompHand= -1.6
        
        randomJelLoc=random.sample(set([1, 2]), 2)
        if randomJelLoc ==[1,2]:
            jellyLocCondition=1
            leftJellyv="red_choice_s.png"
            rightJellyv="blue_choice_s.png"
        else:
            jellyLocCondition=2
            leftJellyv="blue_choice_s.png"
            rightJellyv="red_choice_s.png"
        bucket5.setPos([0, yBucket])
        compHand.setImage(comphand)
        compHand.setSize([handw, handh])
        leftJelly.setImage(leftJellyv)
        rightJelly.setImage(rightJellyv)
        ortext.setPos([0, yBucket-.15])
        # keep track of which components have finished
        CompOutcomeComponents = []
        CompOutcomeComponents.append(bucket5)
        CompOutcomeComponents.append(cartoon)
        CompOutcomeComponents.append(compHand)
        CompOutcomeComponents.append(leftJelly)
        CompOutcomeComponents.append(rightJelly)
        CompOutcomeComponents.append(ortext)
        for thisComponent in CompOutcomeComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "CompOutcome"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = CompOutcomeClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            ycompHand= -1.6 + frameN/15
            if ycompHand> -.6:
                continueRoutine=False
            
            # *bucket5* updates
            if t >= 0.0 and bucket5.status == NOT_STARTED:
                # keep track of start time/frame for later
                bucket5.tStart = t  # underestimates by a little under one frame
                bucket5.frameNStart = frameN  # exact frame index
                bucket5.setAutoDraw(True)
            
            # *cartoon* updates
            if t >= 0.0 and cartoon.status == NOT_STARTED:
                # keep track of start time/frame for later
                cartoon.tStart = t  # underestimates by a little under one frame
                cartoon.frameNStart = frameN  # exact frame index
                cartoon.setAutoDraw(True)
            
            # *compHand* updates
            if t >= 0.0 and compHand.status == NOT_STARTED:
                # keep track of start time/frame for later
                compHand.tStart = t  # underestimates by a little under one frame
                compHand.frameNStart = frameN  # exact frame index
                compHand.setAutoDraw(True)
            if compHand.status == STARTED:  # only update if being drawn
                compHand.setPos([xcompHand,ycompHand], log=False)
                compHand.setOri(0, log=False)
            
            # *leftJelly* updates
            if t >= 0.0 and leftJelly.status == NOT_STARTED:
                # keep track of start time/frame for later
                leftJelly.tStart = t  # underestimates by a little under one frame
                leftJelly.frameNStart = frameN  # exact frame index
                leftJelly.setAutoDraw(True)
            
            # *rightJelly* updates
            if t >= 0.0 and rightJelly.status == NOT_STARTED:
                # keep track of start time/frame for later
                rightJelly.tStart = t  # underestimates by a little under one frame
                rightJelly.frameNStart = frameN  # exact frame index
                rightJelly.setAutoDraw(True)
            
            # *ortext* updates
            if t >= 0.0 and ortext.status == NOT_STARTED:
                # keep track of start time/frame for later
                ortext.tStart = t  # underestimates by a little under one frame
                ortext.frameNStart = frameN  # exact frame index
                ortext.setAutoDraw(True)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CompOutcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "CompOutcome"-------
        for thisComponent in CompOutcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ycompHand= -0.6
        bucket5.setAutoDraw(True)
        leftJelly.setAutoDraw(True)
        rightJelly.setAutoDraw(True)
        compHand.setAutoDraw(True)
        ortext.setAutoDraw(True)
        
        
        
        
        #------Prepare to start Routine "CompOutcome_pause"-------
        t = 0
        CompOutcome_pauseClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        
        # keep track of which components have finished
        CompOutcome_pauseComponents = []
        CompOutcome_pauseComponents.append(cartoon_2)
        for thisComponent in CompOutcome_pauseComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "CompOutcome_pause"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = CompOutcome_pauseClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cartoon_2* updates
            if t >= 0.0 and cartoon_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                cartoon_2.tStart = t  # underestimates by a little under one frame
                cartoon_2.frameNStart = frameN  # exact frame index
                cartoon_2.setAutoDraw(True)
            elif cartoon_2.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                cartoon_2.setAutoDraw(False)
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CompOutcome_pauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "CompOutcome_pause"-------
        for thisComponent in CompOutcome_pauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        
        #------Prepare to start Routine "CompFace"-------
        t = 0
        CompFaceClock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.050000)
        # update component parameters for each repeat
        compHand.setAutoDraw(False)
        
        time_CompFace = stopwatch2.getTime()
        
        if confiComp==1:
            counterD[conditionConf] += 1
            if compplayer == 1: 
               compFace = 'faces/04c.jpg'
            if compplayer == 2: 
               compFace = 'faces/30c.jpg'
            if compplayer == 3: 
               compFace = 'faces/11c.jpg'
            if compplayer == 4: 
               compFace = 'faces/06c.jpg'
        
        if confiComp==0:
            counterD[conditionUnconf] += 1
            if compplayer == 1: 
               compFace = 'faces/04uc.jpg'
            if compplayer == 2: 
               compFace = 'faces/30uc.jpg'
            if compplayer == 3: 
               compFace = 'faces/11uc.jpg'
            if compplayer == 4: 
               compFace = 'faces/06uc.jpg'
        
        if compChoice==1:
            showCompChoice="red_choice_s.png"
        else:
            showCompChoice="blue_choice_s.png"
        
        
        ComputerFace.setImage(compFace)
        CompBeanChoice.setImage(showCompChoice)
        compHandf.setImage(comphand)
        compHandf.setSize([handw,handh])
        # keep track of which components have finished
        CompFaceComponents = []
        CompFaceComponents.append(ComputerFace)
        CompFaceComponents.append(CompBeanChoice)
        CompFaceComponents.append(compHandf)
        for thisComponent in CompFaceComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "CompFace"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = CompFaceClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *ComputerFace* updates
            if t >= 0 and ComputerFace.status == NOT_STARTED:
                # keep track of start time/frame for later
                ComputerFace.tStart = t  # underestimates by a little under one frame
                ComputerFace.frameNStart = frameN  # exact frame index
                ComputerFace.setAutoDraw(True)
            elif ComputerFace.status == STARTED and t >= (0 + (.05-win.monitorFramePeriod*0.75)): #most of one frame period left
                ComputerFace.setAutoDraw(False)
            
            # *CompBeanChoice* updates
            if t >= 0.0 and CompBeanChoice.status == NOT_STARTED:
                # keep track of start time/frame for later
                CompBeanChoice.tStart = t  # underestimates by a little under one frame
                CompBeanChoice.frameNStart = frameN  # exact frame index
                CompBeanChoice.setAutoDraw(True)
            elif CompBeanChoice.status == STARTED and t >= (0.0 + (.05-win.monitorFramePeriod*0.75)): #most of one frame period left
                CompBeanChoice.setAutoDraw(False)
            
            # *compHandf* updates
            if t >= 0.0 and compHandf.status == NOT_STARTED:
                # keep track of start time/frame for later
                compHandf.tStart = t  # underestimates by a little under one frame
                compHandf.frameNStart = frameN  # exact frame index
                compHandf.setAutoDraw(True)
            elif compHandf.status == STARTED and t >= (0.0 + (.05-win.monitorFramePeriod*0.75)): #most of one frame period left
                compHandf.setAutoDraw(False)
            if compHandf.status == STARTED:  # only update if being drawn
                compHandf.setPos([xcompHand,ycompHand], log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CompFaceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "CompFace"-------
        for thisComponent in CompFaceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ComputerFace.setAutoDraw(True)
        CompBeanChoice.setAutoDraw(True)
        #compHandf.setAutoDraw(True)
        
        
        
        
        #------Prepare to start Routine "SubOutcome"-------
        t = 0
        SubOutcomeClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        xReach=0.5
        time_SubOutcome = stopwatch2.getTime()
        
        # now set the jellys in the subject's hand
        jellycond = redJelly
        
        if jellycond == 0: 
            jellylist=['jb_blue.png','jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
        elif jellycond == 1:
            jellylist=['jb_red.png','jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
        elif jellycond == 2:
            jellylist=['jb_red.png','jb_red.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
        elif jellycond == 3:
            jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
        elif jellycond == 4:
            jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
        elif jellycond == 5:
            jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_blue.png', 'jb_blue.png', 'jb_blue.png']
        elif jellycond == 6:
            jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_blue.png', 'jb_blue.png']
        elif jellycond == 7:
            jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png','jb_red.png', 'jb_blue.png']
        elif jellycond == 8:
            jellylist=['jb_red.png','jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png', 'jb_red.png']
        
        shuffle(jellylist)
        jellyposxset = [.15, .25, .35, .15, .25, .35, .25, .35]
        jelly1 = jellylist.pop()
        jelly2 = jellylist.pop()
        jelly3 = jellylist.pop()
        jelly4 = jellylist.pop()
        jelly5 = jellylist.pop()
        jelly6 = jellylist.pop()
        jelly7 = jellylist.pop()
        jelly8 = jellylist.pop()
        subHand.setOri(0)
        subHand.setImage(shand)
        sjelly1.setOri(random.randint(-15,15))
        sjelly1.setImage(jelly1)
        sjelly2.setOri(random.randint(-15,15))
        sjelly2.setImage(jelly2)
        sjelly3.setOri(random.randint(-15,15))
        sjelly3.setImage(jelly3)
        sjelly4.setOri(random.randint(-15,15))
        sjelly4.setImage(jelly4)
        sjelly5.setOri(random.randint(-15,15))
        sjelly5.setImage(jelly5)
        sjelly6.setOri(random.randint(-15,15))
        sjelly6.setImage(jelly6)
        sjelly7.setOri(random.randint(-15,15))
        sjelly7.setImage(jelly7)
        sjelly8.setOri(random.randint(-15,15))
        sjelly8.setImage(jelly8)
        comphandout.setImage(comphand)
        # keep track of which components have finished
        SubOutcomeComponents = []
        SubOutcomeComponents.append(subHand)
        SubOutcomeComponents.append(sjelly1)
        SubOutcomeComponents.append(sjelly2)
        SubOutcomeComponents.append(sjelly3)
        SubOutcomeComponents.append(sjelly4)
        SubOutcomeComponents.append(sjelly5)
        SubOutcomeComponents.append(sjelly6)
        SubOutcomeComponents.append(sjelly7)
        SubOutcomeComponents.append(sjelly8)
        SubOutcomeComponents.append(comphandout)
        for thisComponent in SubOutcomeComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "SubOutcome"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = SubOutcomeClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            yReach=-1.2+frameN/15
            if yReach>-0.6:
                continueRoutine=False
            
            if ycompHand > -1:
                ycompHand = ycompHand - .1
            
            # *subHand* updates
            if t >= 0.0 and subHand.status == NOT_STARTED:
                # keep track of start time/frame for later
                subHand.tStart = t  # underestimates by a little under one frame
                subHand.frameNStart = frameN  # exact frame index
                subHand.setAutoDraw(True)
            if subHand.status == STARTED:  # only update if being drawn
                subHand.setPos([.25,yReach], log=False)
            
            # *sjelly1* updates
            if t >= 0.0 and sjelly1.status == NOT_STARTED:
                # keep track of start time/frame for later
                sjelly1.tStart = t  # underestimates by a little under one frame
                sjelly1.frameNStart = frameN  # exact frame index
                sjelly1.setAutoDraw(True)
            if sjelly1.status == STARTED:  # only update if being drawn
                sjelly1.setPos([xhand-xadd, yReach], log=False)
            
            # *sjelly2* updates
            if t >= 0.0 and sjelly2.status == NOT_STARTED:
                # keep track of start time/frame for later
                sjelly2.tStart = t  # underestimates by a little under one frame
                sjelly2.frameNStart = frameN  # exact frame index
                sjelly2.setAutoDraw(True)
            if sjelly2.status == STARTED:  # only update if being drawn
                sjelly2.setPos([xhand, yReach], log=False)
            
            # *sjelly3* updates
            if t >= 0.0 and sjelly3.status == NOT_STARTED:
                # keep track of start time/frame for later
                sjelly3.tStart = t  # underestimates by a little under one frame
                sjelly3.frameNStart = frameN  # exact frame index
                sjelly3.setAutoDraw(True)
            if sjelly3.status == STARTED:  # only update if being drawn
                sjelly3.setPos([xhand+xadd, yReach], log=False)
            
            # *sjelly4* updates
            if t >= 0.0 and sjelly4.status == NOT_STARTED:
                # keep track of start time/frame for later
                sjelly4.tStart = t  # underestimates by a little under one frame
                sjelly4.frameNStart = frameN  # exact frame index
                sjelly4.setAutoDraw(True)
            if sjelly4.status == STARTED:  # only update if being drawn
                sjelly4.setPos([xhand-xadd, yReach-yadd], log=False)
            
            # *sjelly5* updates
            if t >= 0.0 and sjelly5.status == NOT_STARTED:
                # keep track of start time/frame for later
                sjelly5.tStart = t  # underestimates by a little under one frame
                sjelly5.frameNStart = frameN  # exact frame index
                sjelly5.setAutoDraw(True)
            if sjelly5.status == STARTED:  # only update if being drawn
                sjelly5.setPos([xhand, yReach-yadd], log=False)
            
            # *sjelly6* updates
            if t >= 0.0 and sjelly6.status == NOT_STARTED:
                # keep track of start time/frame for later
                sjelly6.tStart = t  # underestimates by a little under one frame
                sjelly6.frameNStart = frameN  # exact frame index
                sjelly6.setAutoDraw(True)
            if sjelly6.status == STARTED:  # only update if being drawn
                sjelly6.setPos([xhand+xadd, yReach-yadd], log=False)
            
            # *sjelly7* updates
            if t >= 0.0 and sjelly7.status == NOT_STARTED:
                # keep track of start time/frame for later
                sjelly7.tStart = t  # underestimates by a little under one frame
                sjelly7.frameNStart = frameN  # exact frame index
                sjelly7.setAutoDraw(True)
            if sjelly7.status == STARTED:  # only update if being drawn
                sjelly7.setPos([xhand-xadd/2, yReach-2*yadd], log=False)
            
            # *sjelly8* updates
            if t >= 0.0 and sjelly8.status == NOT_STARTED:
                # keep track of start time/frame for later
                sjelly8.tStart = t  # underestimates by a little under one frame
                sjelly8.frameNStart = frameN  # exact frame index
                sjelly8.setAutoDraw(True)
            if sjelly8.status == STARTED:  # only update if being drawn
                sjelly8.setPos([xhand+xadd/2, yReach-2*yadd], log=False)
            
            # *comphandout* updates
            if t >= 0.0 and comphandout.status == NOT_STARTED:
                # keep track of start time/frame for later
                comphandout.tStart = t  # underestimates by a little under one frame
                comphandout.frameNStart = frameN  # exact frame index
                comphandout.setAutoDraw(True)
            if comphandout.status == STARTED:  # only update if being drawn
                comphandout.setPos([xcompHand,ycompHand], log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SubOutcomeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "SubOutcome"-------
        for thisComponent in SubOutcomeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        subHand.setAutoDraw(True)
        sjelly1.setAutoDraw(True)
        sjelly2.setAutoDraw(True)
        sjelly3.setAutoDraw(True)
        sjelly4.setAutoDraw(True)
        sjelly5.setAutoDraw(True)
        sjelly6.setAutoDraw(True)
        sjelly7.setAutoDraw(True)
        sjelly8.setAutoDraw(True)
        compHand.setAutoDraw(False)
        comphandout.setAutoDraw(True)
        
        
        
        
        #------Prepare to start Routine "SubChoose"-------
        t = 0
        SubChooseClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        responseJelly=""
        chosen=""
        stopwatch.reset()
        responseRT=999
        time_SubChoose = stopwatch2.getTime()
        
        
        choiceButton = event.BuilderKeyResponse()  # create an object of type KeyResponse
        choiceButton.status = NOT_STARTED
        # keep track of which components have finished
        SubChooseComponents = []
        SubChooseComponents.append(choiceButton)
        for thisComponent in SubChooseComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "SubChoose"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = SubChooseClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *choiceButton* updates
            if t >= 0.0 and choiceButton.status == NOT_STARTED:
                # keep track of start time/frame for later
                choiceButton.tStart = t  # underestimates by a little under one frame
                choiceButton.frameNStart = frameN  # exact frame index
                choiceButton.status = STARTED
                # keyboard checking is just starting
                choiceButton.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if choiceButton.status == STARTED:
                theseKeys = event.getKeys(keyList=['v', 'b'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    choiceButton.keys = theseKeys[-1]  # just the last key pressed
                    choiceButton.rt = choiceButton.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SubChooseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "SubChoose"-------
        for thisComponent in SubChooseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        keys = event.getKeys(['v', 'b']) 
        keep = 0
        
        if jellyLocCondition==1:
            if  choiceButton.keys == 'v':
                keep = 1
                responseJelly="red"
                subChoice=1
                responseRT = stopwatch.getTime() 
            elif choiceButton.keys == 'b':
                keep = 2
                responseJelly="blue"
                responseRT = stopwatch.getTime() 
                subChoice=0
        else:
            if  choiceButton.keys == 'v':
                keep = 1
                responseJelly="blue"
                subChoice=0
                responseRT = stopwatch.getTime() 
            elif choiceButton.keys == 'b':
                keep = 2
                responseJelly="red"
                responseRT = stopwatch.getTime() 
                subChoice=1
        
        
        ComputerFace_i6.setAutoDraw(False)
        CompBeanChoice_i6.setAutoDraw(False)
        
        subHand_i7.setAutoDraw(False)
        sjelly1_2.setAutoDraw(False)
        sjelly2_2.setAutoDraw(False)
        sjelly3_2.setAutoDraw(False)
        sjelly4_2.setAutoDraw(False)
        sjelly5_2.setAutoDraw(False)
        sjelly6_2.setAutoDraw(False)
        sjelly7_2.setAutoDraw(False)
        sjelly8_2.setAutoDraw(False)
        comphandout.setAutoDraw(False)
        
        leftjelly_i5.setAutoDraw(False)
        rightjelly_i5.setAutoDraw(False)
        
        if responseJelly=="red":
            subresponse = 1
        else:
            subresponse = 0
        if subresponse == correct:
            subcorrect = 1
        else:
            subcorrect = 0
        if correct == 0.5:
            subcorrect = random.randint(0,1)
        social_urn_trials.addData('SubCorrect',subcorrect)
        correctResponses +=  subcorrect
        social_urn_trials.addData('correctResponses', correctResponses)
        
        #remove unnecessary elements
        leftJelly.setAutoDraw(False)
        rightJelly.setAutoDraw(False)
        ComputerFace.setAutoDraw(False)
        CompBeanChoice.setAutoDraw(False)
        compHandf.setAutoDraw(False)
        subHand.setAutoDraw(False)
        sjelly1.setAutoDraw(False)
        sjelly2.setAutoDraw(False)
        sjelly3.setAutoDraw(False)
        sjelly4.setAutoDraw(False)
        sjelly5.setAutoDraw(False)
        sjelly6.setAutoDraw(False)
        sjelly7.setAutoDraw(False)
        sjelly8.setAutoDraw(False)
        bucket5.setAutoDraw(False)
        ortext.setAutoDraw(False)
        
        
        
        
        
        
        
        # check responses
        if choiceButton.keys in ['', [], None]:  # No response was made
           choiceButton.keys=None
        # store data for social_urn_trials (TrialHandler)
        social_urn_trials.addData('choiceButton.keys',choiceButton.keys)
        if choiceButton.keys != None:  # we had a response
            social_urn_trials.addData('choiceButton.rt', choiceButton.rt)
        
        #------Prepare to start Routine "subFeedback"-------
        t = 0
        subFeedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        bucket6.setPos([0, yBucket])
        LeftJellyS_3.setImage(leftJellyv)
        LeftJellyS_3.setSize([0.2, 0.25])
        RightJellyS_3.setImage(rightJellyv)
        RightJellyS_3.setSize([0.2, 0.25])
        time_subFeedback = stopwatch2.getTime()
        
        # keep track of which components have finished
        subFeedbackComponents = []
        subFeedbackComponents.append(bucket6)
        subFeedbackComponents.append(LeftJellyS_3)
        subFeedbackComponents.append(RightJellyS_3)
        for thisComponent in subFeedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "subFeedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = subFeedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *bucket6* updates
            if t >= 0.0 and bucket6.status == NOT_STARTED:
                # keep track of start time/frame for later
                bucket6.tStart = t  # underestimates by a little under one frame
                bucket6.frameNStart = frameN  # exact frame index
                bucket6.setAutoDraw(True)
            elif bucket6.status == STARTED and t >= (0.0 + (1-win.monitorFramePeriod*0.75)): #most of one frame period left
                bucket6.setAutoDraw(False)
            
            # *LeftJellyS_3* updates
            if (keep==1) and LeftJellyS_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                LeftJellyS_3.tStart = t  # underestimates by a little under one frame
                LeftJellyS_3.frameNStart = frameN  # exact frame index
                LeftJellyS_3.setAutoDraw(True)
            elif LeftJellyS_3.status == STARTED and t >= (LeftJellyS_3.tStart + 1):
                LeftJellyS_3.setAutoDraw(False)
            
            # *RightJellyS_3* updates
            if (keep==2) and RightJellyS_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                RightJellyS_3.tStart = t  # underestimates by a little under one frame
                RightJellyS_3.frameNStart = frameN  # exact frame index
                RightJellyS_3.setAutoDraw(True)
            elif RightJellyS_3.status == STARTED and t >= (RightJellyS_3.tStart + 1):
                RightJellyS_3.setAutoDraw(False)
            if stopwatch2.getTime() > time_subFeedback +1:
                continueRoutine=False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in subFeedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "subFeedback"-------
        for thisComponent in subFeedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        social_urn_trials.addData('responseJelly',responseJelly)
        social_urn_trials.addData('responseRT',responseRT)
        social_urn_trials.addData('subChoice',subChoice)
        social_urn_trials.addData('tfix', time_fixation)
        social_urn_trials.addData('treach', time_Reach)
        social_urn_trials.addData('tCompOut', time_CompOutcome)
        social_urn_trials.addData('tCompFace', time_CompFace)
        social_urn_trials.addData('tSubOut', time_SubOutcome)
        social_urn_trials.addData('tSubChoose', time_SubChoose)
        social_urn_trials.addData('tsubFeed', time_subFeedback)
        social_urn_trials.addData('randomJelLoc', time_subFeedback)
        
        
        
        
        
        
        
        
        
        #------Prepare to start Routine "ITI"-------
        t = 0
        ITIClock.reset()  # clock 
        frameN = -1
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = []
        ITIComponents.append(text_2)
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "ITI"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ITIClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            if t >= 0.0 and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t  # underestimates by a little under one frame
                text_2.frameNStart = frameN  # exact frame index
                text_2.setAutoDraw(True)
            elif text_2.status == STARTED and t >= (0.0 + (0.5-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'social_urn_trials'
    
    # get names of stimulus parameters
    if social_urn_trials.trialList in ([], [None], None):  params = []
    else:  params = social_urn_trials.trialList[0].keys()
    # save data for this loop
    social_urn_trials.saveAsExcel(filename + '.xlsx', sheetName='social_urn_trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    social_urn_trials.saveAsText(filename + 'social_urn_trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
# completed 1 repeats of 'social_urn_loop'


#------Prepare to start Routine "blank"-------
t = 0
blankClock.reset()  # clock 
frameN = -1
routineTimer.add(2.000000)
# update component parameters for each repeat
all_done.setText('all done!\n\n'

'You labelled\n       ' + str(correctResponses) + '\nbuckets correctly.')
# keep track of which components have finished
blankComponents = []
blankComponents.append(all_done)
for thisComponent in blankComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "blank"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *all_done* updates
    if t >= 0.0 and all_done.status == NOT_STARTED:
        # keep track of start time/frame for later
        all_done.tStart = t  # underestimates by a little under one frame
        all_done.frameNStart = frameN  # exact frame index
        all_done.setAutoDraw(True)
    elif all_done.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
        all_done.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "blank"-------
for thisComponent in blankComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)



























win.close()
core.quit()
