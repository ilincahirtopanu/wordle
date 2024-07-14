# Basic game logic
#  Run in Shell with:   python wordle.py

word = "ultra"
letters = list(word)

MISS = "MISS"    # not in the word
HIT = "HIT"      # in the right spot
CLOSE = "CLOSE"  # in the word, but wrong spot
solved = False

# guesses = a list with words that have been guessed
# results = a list, where each element is another list specifying if the corresponding letter in a guess was a hit, miss, or close

guesses = list()
results = list()
while not solved:
  a = input("Enter a word:")
  guesses.append(a)
  position = 0
  result = list()
  for letter in list(a):
    if letters[position] == letter:
      result.append(HIT)
    elif letter in letters:
      result.append(CLOSE)
    else:
      result.append(MISS)     
    position += 1
  print(result)
  results.append(result)
  if (a == word):
    solved = True
    print("You found the word. hooray.")
    print(guesses)
    print(results)
  

