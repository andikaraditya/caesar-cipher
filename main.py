import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)

def encrypt(text, shift, direction):
  cipher = ""
  if direction == "backward":
    shift = - shift
  for letter in text:
    if letter not in alphabet:
      cipher += letter
      continue
    x = alphabet.index(letter)
    x = x + shift
    if x > 25:
      x = x % 26
    elif x < 0:
      x = x % -26
    cipher = cipher + alphabet[x]

  print(cipher)

program = True
while program == True:
  # text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  direction = input("Type direction of encryption 'forward' or 'backward':\n")
  encrypt(text, shift, direction)
  z = input("Do you want to continue program? (Y or N)\n")
  if z == "Y":
    program = True
  else:
    program = False