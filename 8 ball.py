import random


print('welcome to magic 8 ball')

print('MMMMMMMMMMUUUUUUUUUUUHAHAHAHAHAHAHAHA')

answers =['YES','NO','MAYBE']



while True:
    print("Ask me a question")
    answer  = input('> ')
    answers = random.choice(answers)
    print(answer)
