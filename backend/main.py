from flask import Flask, render_template, request, session, redirect
import random

app = Flask('app')
app.secret_key = "secret key!"
text_file = open("sgb-words.txt", "r")
words = text_file.readlines()
text_file.close()
word = words[random.randint(0, len(words) -1)]
letters = list(word)

MISS = "MISS"    # not in the word
HIT = "HIT"      # in the right spot
CLOSE = "CLOSE"  # in the word, but wrong spot
solved = False

# guesses = a list with words that have been guessed
# results = a list, where each element is another list specifying if the corresponding letter in a guess was a hit, miss, or close

# Extra time? Only allow 5-letter guesses, display error message if len(guess) != 5
# Still have time? Only allow 6 guesses, like the real game! Display the answer if the user cannot guess in 6 tries.
# Still have time? Only allow users to reset the game if they have solved the puzzle or used all 6 guesses
# Even more time? Randomize the word each time the user resets.

@app.route('/', methods=['GET', 'POST'])
def index():
  # Initialize session variables if needed
  if 'guesses' not in session :
    session['guesses'] = list()
  if 'results' not in session :
    session['results'] = list()
  if 'num_guesses' not in session:
    session['num_guesses'] = 0

  if request.method == 'POST' :
    # TODO: save the guess to the session
    # check the result for each letter
    # see wordle.py for sample game logic
    guess = request.form['guess']
    if(len(guess) != 5):
      return redirect('error.html')
    guesses = session['guesses']
    guesses.append(guess)
    session['guesses'] = guesses
    results = session['results']
    position = 0
    result = list()
    guesslen = len(guess)
    if (guesslen != 5):
      session['guesslen'] = guesslen
      return render_template("error.html")
    for letter in guess:
      if letters[position] == letter:
        result.append(HIT)
      elif letter in letters:
        result.append(CLOSE)
      else:
        result.append(MISS)     
      position += 1
    results.append(result)
    session['results'] = results
    num_guesses = session['num_guesses']
    num_guesses += 1
    session['num_guesses'] = num_guesses
    if (guess == word):
      print("Good job")
    elif session['num_guesses'] >= 6:
      return redirect('/reset')
    pass
  return render_template("index.html")

@app.route('/reset', methods=['GET', 'POST'])
def reset():
  # TODO: reset the game board and the session 
  session.clear()
  return redirect('/')

app.run(host='0.0.0.0', port=8080)


