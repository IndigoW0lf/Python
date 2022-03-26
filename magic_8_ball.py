import random

name = "Kai Indigo"
questions = ("Will I have my dream job in five years?", "Will my kids be successful and happy?", "Will our financial issues be over soon?", "Do I ever find lasting love?", "Is Data Engineering the path for me?", "Do my children all live long healthy lives?", "Does Aaron get to live in his tiny house?", "Do we get to be grandparents?", "Is there life after death?", "Do I find a great job soon?", "Do we make it to New Zealand?")

random_question = random.choice(questions)
random_number = random.randint(1, 12)
answer=""

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "What does your heart tell you?"
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Life has a way of working things out for the best."
elif random_number == 11:
  answer = "I think yes."
elif random_number == 12:
  answer = "Why not?"
else:
  answer = "Error"

print(name + " asks: " + random_question +'\n')
print("Magic 8-Ball's answer: " + answer)
