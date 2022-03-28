import PlayingQuestion
import RecordingQuestions
from pygame import mixer
import soundfile as sf
import sounddevice as sd
import time
# change to extracting from csv file
questions = [[1,"Tell me about yourself"],[2,"What is your biggest challenge"]]

# play in order
for i in range(len(questions)):
    #print question
    print ("Question: ",questions[i][1])
    #Play Audio
    PlayingQuestion.play_questions(questions[i][1])

    #start to record and start a timer
    RecordingQuestions.recordquestion(questions[i][1],3)

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
            break
