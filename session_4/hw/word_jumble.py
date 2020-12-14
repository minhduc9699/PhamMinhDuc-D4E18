from random import shuffle, randint
from getpass import getpass

quizzes = []
for i in range(3):
    quiz = getpass('Enter your quizz')
    original_quiz = quiz
    quiz = list(quiz)
    shuffle(quiz)
    quizzes.append(quiz)
random_index = randint(0, len(quizzes))
for i in range(len(quizzes[random_index])):
    print(quizzes[random_index][i], end=' ')
print()

ans = input('Enter your answer: ')
if ans == original_quiz:
    print('yayy!')
else:
    print(':"(')
