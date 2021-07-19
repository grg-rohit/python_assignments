#Filling a dictionary with user input

dream_vacation = {}
onePlace = {}

print("Dream vacation\n")
# Set a flag to indicate that polling is active.
dreamVacation_polling_active = True

while dreamVacation_polling_active:
  # Prompt for the person's name and dream vacation location.
  name = input("\nusername: ")
  dreamVacation = input("location for dream vacation: ")

  # Store the location in the dictionary:
  dream_vacation[name] = dreamVacation
  
  # Find out if anyone else is going to take the poll.
  repeat = input("Would you like to take another user response? (yes/ no) ")
  if repeat == 'no':
    dreamVacation_polling_active = False

print("\nIf you could visit one place in the world, where would you go?\n")

polling = True
while polling:
  # Prompt for the person's name and one place they would visit.
  name = input("\nusername: ")
  one_place = input("location for one place if u could visit: ")

  # Store the location in the dictionary:
  onePlace[name] = one_place
  
  # Find out if anyone else is going to take the poll.
  repeat = input("Would you like to take another user response? (yes/ no) ")
  if repeat == 'no':
    polling = False

print("\nPolls for: dream vacation")
print(dream_vacation)

print("\nPolls for: If you could visit one place in the world, where would you go?\n")
print(onePlace)