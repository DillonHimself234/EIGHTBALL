import random
answers = ['It is decidedly so', 'Without a doubt', 'Yes – definitely', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'My sources say no', 'Outlook not so good', 'Very doubtful']

print('')
print('')
print('')
print('Magic 8 Ball, What is your name?')
name = input()
print('Hello ' + name)


def Magic8Ball():
    print('Ask me a question.')
    input()
    print (answers[random.randint(0, len(answers)-1)] )
    Replay()
    

def Replay():
    print ('Do you have another question? y/n] ')
    reply = input()
    if reply == 'y':
        Magic8Ball()
    elif reply == 'n':
        exit()
    else:
        Replay()

		
Magic8Ball()