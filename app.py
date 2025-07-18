from flask import (Flask,
  render_template,
  redirect,
  url_for,
  session,
  request
)

app = Flask(__name__)
app.secret_key = "hello"

points = 0
questionNumber = 0

@app.route('G9_math/algebra-quiz.html', methods =['GET', 'POST'])
def algebraQuiz():
    if request.method == 'POST':
      while questionNumber < 5:
        lessonchoice = request.form['']
        if lessonchoice == "wrong":
          questionNumber += 1
        elif lessonchoice == "right":
          questionNumber += 1
          points += 1