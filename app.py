from flask import (Flask,
  render_template,
  redirect,
  url_for,
  session,
  request
)

app = Flask(__name__)
app.secret_key = "hello"


@app.route('/', methods =['GET', 'POST'])
def algebraQuiz():
    points=0
    if request.method=="GET":return render_template("/G9_math/algebra-quiz.html")
    elif request.method == 'POST':
      for i in range(1, 6):
        lessonchoice = request.form[f'q{i}']
        if lessonchoice == "right":
          points += 1
      return f"<h1>{points}/5</h1>"
        