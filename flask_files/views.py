from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route("/")
def hello():
    a=3
    print("hello",a)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=5002, debug=True)
