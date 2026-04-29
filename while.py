import random
# First 
i = 1
while i <= 5:
     print(i)
     i=i+1 

# Second
num =1
while True:
     command = input("For end the system enter end:")
     if command.lower() == "end":
          break
     else:
         print(num)
         num=num+1 

#Third 
i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished")

#Fourth
i = 1

while i <= 3:
    j = 1
    while j <= 2:
        print(i, j)
        j += 1
    i += 1

#Five

number = 0
secret = random.randint(1, 10)

while number != secret:
     guess = int(input("Guess number: "))
     if guess < secret:
        print("Too low")
     elif guess > secret:
        print("Too high")
     else:
         print("your guess is Correct.")
         break
     
# Sixth

commands = ["start", "stop", "end"]

randomCommand = random.choice(commands)

while True:
    match randomCommand:
        case "start":
         print("Your System is Running.")
         break 
        case "stop":
         print("Your System is stop.") 
         break 
        case "end":
         print("Your System is Terminated.")
         break 

# Seven 
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)

print(cards) 