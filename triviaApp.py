import json
import random
import sys

totalQuestions = -1
fileContent = ''
def readTriviaDB(jsonName):
    global totalQuestions
    global fileContent
    try:
        fx = open(jsonName,'r')
        fileContent = fx.read()
        fileContent = json.loads(fileContent)
        fx.close()
        totalQuestions = len(fileContent)
    except:
        print('No such JSON file')


if __name__ == "__main__":
    jsonName = sys.argv[1]
    readTriviaDB(jsonName)
    # execute only if run as a script
    myPoints = 0
    if totalQuestions != -1:
        print('\n\n\n\n\t\t\tWelcome to the Trivia App')

        print('\n\n You will be asked to answer ',totalQuestions,' questions')

        shouldStart = input('\n\n Should we start? [Y\\N]')

        if shouldStart.lower() == 'y':
            print('\n\n')
            for i in range(0,totalQuestions):
                currentQuestion = fileContent[i]
                pn = i
                # if i > 0:
                #     pn = i + 1
                print("Q-",i+1,')', currentQuestion['question'])
                options = []
                for item in currentQuestion['incorrect']:
                    options.append(item)
                options.append(currentQuestion['correct'])

                random.shuffle(options)

                print('\n\nOPTIONS: ',end="")
                for j in range(0,len(options)):
                    print(j+1,') ',options[j],end = '     ')
                print('\n')
                selectedOption = input('Your answer? (Press 1 or 2 or 3 or 4 and press enter): ')
                try:
                    selectedOption = int(selectedOption)
                except:
                    selectedOption = -1
                selectedOption = selectedOption -1
                if selectedOption < len(options) and options[selectedOption] == currentQuestion['correct']:
                    myPoints+=1
                    print('********** Correct Answer ************')
                else:
                    print('!!!!!!!!!! Wrong Answer !!!!!!!!!!!!!!')
                    print('Right answer is : ',currentQuestion['correct'])


                print('\n\n\n')
                print("[Your Points:",myPoints,"/",i+1,"]")
                print('\n\n\n')
    else:
        print('JSON reading error')
