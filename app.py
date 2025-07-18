from flask import (Flask,
  render_template,
  redirect,
  url_for,
  session,
  request
)

app = Flask(__name__)
app.secret_key = "hello"

# @app.route('/', methods =['GET', 'POST'])
# def index():
#       if request.method == 'POST':
#     lessonchoice = request.form['Index']
#     if lessonchoice == "":
#       return redirect(url_for(''))
#     elif lessonchoice == "":
#       return redirect(url_for(''))
#   else:
#     return render_template('index.html')