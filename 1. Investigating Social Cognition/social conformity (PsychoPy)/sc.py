######                  SOCIAL CONFORMITY TASK                  ######
####imports
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.iohub import launchHubServer
import numpy as np  # whole numpy lib is available, prepend 'np.'
import pandas as pd
import random
import os.path

#at the very beginning to load the server
io = launchHubServer()
keyboard = io.devices.keyboard

#####Variables
#percentage of stimuli for which we don't want a third party rating
#If you don't want to use percentage, modifyable line 185
#Allow us to account for the regression to the mean later on when modelling
RegMeanPer = 10
######

######## Functions to use in the script ########
#function to display info' (before and after experiment) 
def msg(txt):
    instructions = visual.TextStim(win, text=txt, color = 'white', height = 20,alignHoriz='center') # create an instruction text
    instructions.draw() # draw the text stimulus in a "hidden screen" so that it is ready to be presented 
    win.flip() # flip the screen to reveal the stimulus
    event.waitKeys(keyList = 'space')

#function to create and place the elements of the background (lines, number and words)
def BackGround():
    backgroundEl = []
    #create numbers (with loop from 1 to 8)
    for n in range(8):
        backgroundEl.append(visual.TextStim(win, text=str(n+1), color = 'white', height = 50,pos = (-437.5+(n*125),-300),alignHoriz = 'center'))
    #create words
    backgroundEl.append(visual.TextStim(win, text='Untrustworthy', color = 'white', height = 30,pos = (-700,-400),alignHoriz = 'left'))
    backgroundEl.append(visual.TextStim(win, text='Trustworthy', color = 'white', height = 30,pos = (700,-400),alignHoriz = 'right'))
    #lines
    backgroundEl.append(visual.Line(win, start=(-550, -250), end=(550, -250),lineWidth=15))
    backgroundEl.append(visual.Line(win, start=(0, -225), end=(0, -275), lineWidth=20))
    return backgroundEl

#Function to create random third party rating
#Uses an individual rating to generate a tp rating with a difference of 0, 2 or 3 from the individual rating only
def TP_Rating(ind):
    pi = random.uniform(0,100)
    modifList = [2,3]
    if pi < 33.3333:
        if ind == 3:
            tp = ind - 2
        elif ind < 3:
            tp = ind + random.choice(modifList)
        else:
            tp = ind - random.choice(modifList)
    elif pi < 66.6666:
        tp = ind
    else:
        if ind == 6:
            tp = ind + 2
        elif ind > 6:
            tp = ind - random.choice(modifList)
        else:
            tp = ind + random.choice(modifList)
    return tp

#Function to make a rectange around the the backgroud number corresponding to the rating
#Takes a score (rating) as input to decide where to draw the rectangle
#Takes a scoreType as input to decide the color of the rectangle
def RectRating(scoreType, score):
    if scoreType == "individual":
        box = visual.Rect(win, width=70, height=70,lineWidth=5, lineColor='green', pos = (-437.5+(score-1)*125,-300))
    elif scoreType == "tp":
        box = visual.Rect(win, width=70, height=70,lineWidth=5, lineColor='cyan', pos = (-437.5+(score-1)*125,-300))
    box.autoDraw = True
    win.flip()
    return box

#Function to display the difference between individual score and third party score
#Takes the difference and third party rating as input to draw the difference above the tp rating rectangle
def visDif(difference, tp):
    if difference > 0:
        difference = '+'+str(difference)
    else:
        difference = str(difference)
    visDif = visual.TextStim(win, text=difference, color = 'yellow', height = 30,pos = (-437.5 + (tp-1)*125,-210),alignHoriz = 'center')
    visDif.draw()
    win.flip()

#Function to do the individual rating (simply save the key pressed)
def Rating():
    key = event.waitKeys(keyList = ['1','2','3','4','5','6','7','8'])
    rating = int(key[0])

    return rating

##################### 

# gui requesting participant info
# with doublechecking loop to avoid mistakes, while allowing only one dataframe per participant
ok = False
while ok != True:
    #the gui
    participant_id = gui.Dlg(title="Truthworthiness Experiment") 
    participant_id.addText('Subject Info')
    participant_id.addField('Participant number')
    participant_id.addField('Round', choices = ['1st','2nd'])
    participant_id.show()
    #to quit if 'cancel' is pressed
    if participant_id.OK:
        participant = participant_id.data[0]
    else:
        core.quite()
    
    round = participant_id.data[1]
    

    #window where we will show the message
    win = visual.Window(fullscr=True, color='black', colorSpace='rgb', units = 'pix', allowStencil=True)

    #check that conditions are properly matched with rounds to avoid confusion and mistakes in the data

    if round == '2nd':
            if os.path.isfile('data/SC_'+participant+'.csv') == False:
                msg('The participant\' s number was not found in the database. \n Maybe it was wrong? Otherwise, round 1 has to be done first.')
                win.close()
            else:
                ok += True

    else:
        ok += True
#####

##### Preparing datasets #######
#if dataset doesn't exist, set up the dataframe to save the data
if os.path.isfile('data/SC_'+participant+'.csv') == False:
    columnss = ['Participant', 'Face', '1st Rating','Third-Party Rating', 'Difference TP', '2nd Rating', 'Individual Difference']
    indexs = np.arange(0)
    DATA = pd.DataFrame(columns=columnss, index = indexs)
#Otherwise, open it
else:
    DATA = pd.read_csv('data/SC_' + participant + '.csv')

#####

##### Preparing stimuli  #######
#Loading the path for pictures according to condition
facePath = os.listdir('Conformity_faces/I') #pictures are stored in condition specific folders
#Transsforming the pictures into psychopy visual stimuli
faceList = []
for i in range(len(facePath)): #replace number in range() by len(facePath) for full version, 
    faceList.append(visual.ImageStim(win=win, name=facePath[i],image='Conformity_faces/I/'+facePath[i]))


#Making all the different messages that will be displayed along the experiment
instruction1st ='''You will be presented with approximately a 100 pictures of faces.
\n Use keys 1 to 8 to rate the trustworthiness of the person depicted, on a scale from 1 to 8.
\n After what, you'll see people's average rating.
\n The experiment is self paced.
\n\n (press space to continue)  '''

instruction2nd = '''Surprise! You have to do it again!
\n Use keys 1 to 8 to rate the trustworthiness of the person depicted, on a scale from 1 to 8.
\n\n (press space to continue)  '''

ending = '''it's over, thanks!
\n\n (press space to continue)'''

#####

##### condition / round specific set up
#For each condition / round, load relevant insturctions

if round == '1st':
    #Making a random list of stimuli for which we won't show a third party rating
    #Uses a percentage (modifyable line 17) to adapt to different dataset, to use a fixed number
    rmn = int((RegMeanPer * len(faceList))/100) #to use a fixed number instead of percentage, replace this value
    regMeanList = random.sample(faceList, rmn )
    msg(instruction1st)
else:
    #round 2 requires randomizing faces order too
    random.shuffle(faceList)
    msg(instruction2nd)
#####

#Making the background visible
background = BackGround()
for i in range(len(background)):
    background[i].autoDraw = True
win.flip()
#####

##### Start the actual experiment
#Loop to go through the faces
for el in range(len(faceList)):
    faceList[el].autoDraw = True
    win.flip()
    
    #ask participant to rate trustwothiness a first time and display it
    rating = Rating()
    visRating = RectRating("individual",rating)
    core.wait(1)

    #create and display third party rating if conditions met, save all that the info
    #It has to be 1st round of i condition (and not in the list for regression to the mean), or be in the E condition
    if (round == '1st' and faceList[el] not in regMeanList):
        TPrating = TP_Rating(rating)
        visTP = RectRating("tp",TPrating)
        core.wait(0.25)
        difference = TPrating - rating
        visDif(difference, TPrating)
        core.wait(1.5)
        
        
        visTP.autoDraw = False
        
        DATA = DATA.append({
            'Participant': participant,
            'Face': faceList[el].name,
            '1st Rating': rating,
            'Third-Party Rating':TPrating,
            'Difference TP': difference,
            }, ignore_index=True)
    #If face stimulus in the regression to the mean list, still save relevant data
    if round == '1st' and faceList[el] in regMeanList:
            DATA = DATA.append({
            'Participant': participant,
            'Face': faceList[el].name,
            '1st Rating': rating,
            }, ignore_index=True)
    visRating.autoDraw = False
    
    #If round 2
    if round == '2nd':
        #save previous rating as the 2nd rating
        rating2 = rating
        #load rating of 1st round to calculate the difference between 1st and 2nd rating
        rating = DATA.loc[DATA['Face'] == faceList[el].name , ['1st Rating']].values[0]
        indDiff = rating2 -rating
        #save 2nd rating and difference for the relevant face stimulus (as the list has been shuffled for 2nd round)
        DATA.loc[DATA['Face'] == faceList[el].name , ['2nd Rating', 'Individual Difference']] = rating2, indDiff

    #erase previous face stimulus to start another trial
    faceList[el].autoDraw = False
#####


# Making the background disappear
for i in range(len(background)):
    background[i].autoDraw = False
###

#Saving and opening dataset multiple times generates unwanted index columns
#Early cleaning inside of the experiment script
columns = ['Participant', 'Face', '1st Rating','Third-Party Rating', 'Difference TP', '2nd Rating', 'Individual Difference']
for colname in DATA.columns.values.tolist():
    if colname not in columns:
        del DATA[colname]

#Save the dataset to csv file
DATA.to_csv('data/SC_'+participant+'.csv')

#End the experiment
msg(ending)


###Explaining the dataset
#'Participant': the participant id entered in the gui
#'Face': the face stimulus for which data is recorded
#'1st Rating': the first trustworthiness rating, on a 1-8 scale
#'TP Rating': a randomly generated third party rating (supposedly by a group), made to be 3,2 or 0 appart from individual rating
#TP Difference': TP Rating - 1st Rating
#'2nd Rating': A second rating asked after displaying TP rating
#'Individual Difference': 2nd Rating - 1st Rating
