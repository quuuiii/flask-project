from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index_page():
    return "Index Page"

@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/user/<name>")
def user(name):
    return f"User: {name}"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/apple")
def apple():
    return render_template("apple.html")

@app.route("/variables")
def variables():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template("variables.html", person=x)

@app.route("/double")
def double():
    return render_template("index.html", result=None)

@app.route("/predict", methods=["POST"])
def predict():
    x = int(request.form["x"])
    result = x * 2
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)