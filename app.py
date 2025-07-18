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

@app.route('G9_math/algebra-quiz.html', methods =['GET', 'POST'])
def algebraQuiz():
    if request.method == 'POST':
      for i in range(1, 6):
        lessonchoice = request.form[f'q{i}']
        if lessonchoice == "right":
          points += 1
    print(points)
        