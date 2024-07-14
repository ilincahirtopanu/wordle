from flask import Flask, render_template, request, session, redirect

app = Flask('app')
app.secret_key = "secret key!"

word = "ultra"
letters = list(word)

MISS = "MISS"    # not in the word
HIT = "HIT"      # in the right spot
CLOSE = "CLOSE"  # in the word, but wrong spot
solved = False

# guesses = a list with words that have been guessed
# results = a list, where each element is another list specifying if the corresponding letter in a guess was a hit, miss, or close

@app.route('/', methods=['GET', 'POST'])
def index():
  # hard code some guesses and results
  guesses = ["clams", "squid", "ultra"]
  results = []
  result = (MISS, HIT, CLOSE, MISS, MISS)
  results.append(result) # clams
  result = (MISS, MISS, CLOSE, MISS, MISS)
  results.append(result) # squid
  result = (HIT, HIT, HIT, HIT, HIT)
  results.append(result) # ultra
  
  return render_template("index.html", guesses=guesses, results=results)

app.run(host='0.0.0.0', port=8080)
