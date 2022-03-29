import PlayingQuestions
import RecordingQuestions
from pygame import mixer
import soundfile as sf
import sounddevice as sd
import time
import ImportFromCSV
import random
# change to extracting from csv file
questions = ImportFromCSV.csvQuestion('Interview_Questions.csv')

# users can defined number of questions to play, recording mins, 

qnum = input("How many questions do you wish to be asked?\n")
tmin = input("Enter recording time for each answer in minutes: ")

# converting mins to second
tsec = int(float(tmin)*60) 

# set qnum to size of questions if qunum is larger than questions

qnum = len(questions) if int(qnum)> len(questions) else int(qnum)

# play in order
for i in range(qnum):
    ranum = random.randrange(0,(qnum-1))
    #print question
    print ("Question: ",questions[ranum][1])
    #Play Audio
    PlayingQuestions.play_questions(questions[ranum][1])

    #start to record and start a timer
    RecordingQuestions.recordquestion(questions[ranum][1],tsec)

    # input options, initialized as 0
    option = 0
    
    while(option != '1'):
        print("Enter your Options: \n")
        option = input(" 1 Go to next question\n 2 Play recording\n 3 Record again\n 4 Exit\n Enter: ")
        if option == '2': 
            # playing recording
            filename = "{}.wav".format(questions[i][1])
            # Extract data and sampling rate from file
            data, fs = sf.read(filename, dtype='float32')  
            sd.play(data, fs)
            status = sd.wait()  # Wait until file is done playing
        
        elif option == '3': # restart the recording
            RecordingQuestions.recordquestion(questions[i][1],3)
        
        elif option == '4':
            exit()
