# First

commands = ["start", "stop", "pause", "end"]

for com in commands:
    print("Your execution command is :",com) 
    match com:
        case "start":
         print("System starting...")
        case "end":
         print("System ending...")
        case "pause":
         print("System continue...")
        case "stop":
         print("System stop...")
        case _:
         print("Unknown command. Please use Start, End, Continue, or Stop.")


# Second

data = [1, "hello", 3.5, 2, "world"]

for info in data:
  print("Your given data is :",info) 
  
  match type(info).__name__:
    case "int":
      print("Your given data is integer")  
    case "str":
      print("Your given data is String")  
    case _:
      print("Your given data is Others")  


# Third

print("enter your Statement which contain 10 character") 

statement = input("Enter something About You :" )

if len(statement)<= 10 :
  for words in statement:
    match words.lower():
      case  "a"| "e" | "i"| "o"| "u":
        print("it is a Vovel")
      case  _:
        print("it is a Consonant")
else:
  print("your Length of character is more than 10.")


# Fourth 

students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Ahmed", "marks": 60}
]


for student in students :
  match student :
    case {"name": name, "marks": marks}  if marks >=90 :
     print(f"{name}: You got Excellent")
    case {"name": name, "marks": marks}  if marks >=70 :
     print(f"{name}: You got Good")
    case _:
     print(f"{name}: You need to Improve yourself")
