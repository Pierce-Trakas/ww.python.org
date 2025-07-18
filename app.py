from flask import (Flask,
  render_template,
  redirect,
  url_for,
  session,
  request
)

app = Flask(__name__)
app.secret_key = "hello"

@app.route("/", methods=["GET", "POST"])
def home():return render_template("index.html")
@app.route("/index.html", methods=["GET", "POST"])
def index():return render_template("index.html")
@app.route("/FUNctions/discreteFunctions.html", methods=["GET", "POST"])
def discreteFunctions():return render_template("/FUNctions/discreteFunctions.html")
@app.route("/FUNctions/exponentialFunctions.html", methods=["GET", "POST"])
def exponentialFunctions():return render_template("/FUNctions/exponentialFunctions.html")
@app.route("/FUNctions/expressions.html", methods=["GET", "POST"])
def expressions():return render_template("/FUNctions/expressions.html")
@app.route("/FUNctions/trigonometricFunctions.html", methods=["GET", "POST"])
def trigonometricFunctions():return render_template("/FUNctions/trigonometricFunctions.html")
@app.route("/FUNctions/quadraticFunctions.html", methods=["GET", "POST"])
def quadraticFunctions():return render_template("/FUNctions/quadraticFunctions.html")
@app.route("/G9_math/algebra.html", methods=["GET", "POST"])
def algebra():return render_template("/G9_math/algebra.html")
@app.route("/G9_math/data-management.html", methods=["GET", "POST"])
def dataManagement():return render_template("/G9_math/data-management.html")
@app.route("/G9_math/financial-literacy.html", methods=["GET", "POST"])
def financialLiteracy():return render_template("/G9_math/financial-literacy.html")
@app.route("/G9_math/geometry.html", methods=["GET", "POST"])
def geometry():return render_template("/G9_math/geometry.html")
@app.route("/G9_math/number-systems.html", methods=["GET", "POST"])
def numberSystems():return render_template("/G9_math/number-systems.html")
@app.route("/Grade 10/analyticalGeometry.html")
def analyticalGeometry():return render_template("/Grade 10/analyticalGeometry.html")
@app.route("/Grade 10/linearSystems.html")
def linearSystems():return render_template("/Grade 10/linearSystems.html")
@app.route("/Grade 10/quadratics.html")
def quadratics():return render_template("/Grade 10/quadratics.html")
@app.route("/Grade 10/trigonometry.html")
def trigonometry():return render_template("/Grade 10/trigonometry.html")
@app.route('/FUNctions/discrete_functions_quiz.html', methods =['GET', 'POST'])
def discreteFunctionsQuiz():
    points=0
    if request.method=="GET":return render_template("/FUNctions/discrete_functions_quiz.html", points=0)
    elif request.method == 'POST':
      for i in range(1, 6):
        lessonchoice = request.form[f'q{i}']
        if lessonchoice == "right":
          points += 1
      return render_template("/FUNctions/discrete_functions_quiz.html", points = points)
@app.route('/FUNctions/exponential-quiz.html', methods =['GET', 'POST'])
def exponentialQuiz():
    points=0
    if request.method=="GET":return render_template("/FUNctions/exponential-quiz.html", points=0)
    elif request.method == 'POST':
      for i in range(1, 5):
        lessonchoice = request.form[f'q{i}']
        if lessonchoice == "right":
          points += 1
      return render_template("/FUNctions/exponential-quiz.html", points = points)
@app.route('/G9_math/algebra-quiz.html', methods =['GET', 'POST'])
def algebraQuiz():
    points=0
    if request.method=="GET":return render_template("/G9_math/algebra-quiz.html", points=0)
    elif request.method == 'POST':
      for i in range(1, 6):
        lessonchoice = request.form[f'q{i}']
        if lessonchoice == "right":
          points += 1
      return render_template("/G9_math/algebra-quiz.html", points = points)
@app.route('/G9_math/geometry_quiz.html', methods =['GET', 'POST'])
def geometryQuiz():
    points=0
    if request.method=="GET":return render_template("/G9_math/geometry_quiz.html", points=0)
    elif request.method == 'POST':
      for i in range(1, 6):
        lessonchoice = request.form[f'q{i}']
        if lessonchoice == "right":
          points += 1
      return render_template("/G9_math/geometry_quiz.html", points = points)
@app.route('/G9_math/number-systems-quiz.html', methods =['GET', 'POST'])
def numberSystemsQuiz():
    points=0
    if request.method=="GET":return render_template("/G9_math/number-systems-quiz.html", points=0)
    elif request.method == 'POST':
      for i in range(1, 6):
        lessonchoice = request.form[f'q{i}']
        if lessonchoice == "right":
          points += 1
      return render_template("/G9_math/number-systems-quiz.html", points = points)
if __name__=="__main__":app.run(port=8000, debug=True)