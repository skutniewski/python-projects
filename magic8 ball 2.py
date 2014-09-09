import random



answers = ['no sorry','yes awesome','maybe']

while True:
    print('ask me qustion')
    qustion = input('>')
    if 'love' in qustion:
       print('how am i the love fariy')
    elif    'die' in qustion:
        print('are you saying i am mean')
    else:
        answer = random.choice(answers)
        print(answer)
