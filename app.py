from  flask import Flask ,request,render_template,jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message":"Hello World"})

@app.route("/temp")
def func():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True,port=5000)