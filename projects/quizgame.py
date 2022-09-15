print("Welcome to a car quiz!")

starting = input ("Do you want to play? ")
if starting.lower() != "yes":
  quit()
print ("Perfect let's play!")
score = 0

answer = input("What are tires mainly made of? ")
if answer.lower() == "rubber" :
  print ("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("How many wheels does a normal size sedan have? ")
if answer.lower() == "four" :
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("How many spark plugs are in a six cylinder? ")
if answer.lower() == "six" :
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

answer = input("What makes an electric car move? ")
if answer.lower() == "motor" :
  print("Correct!")
  score += 1
else:
  print("Incorrect!")

print("Congratulations you have completed the quiz!")
print("You got " + str(score)  + " questions correct:")
print(str(score / 4 * 100) + "%")