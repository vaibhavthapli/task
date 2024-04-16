from flask import Flask, request, jsonify

app = Flask(__name__)


# get: posting using url , post: posting using body

@app.route("/abc", methods=["GET", 'POST'])
def test1():
    if (request.method == "POST"):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify((str(result)))


@app.route("/abc1", methods=["GET", 'POST'])
def test2():
    if (request.method == "POST"):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify((str(result)))


@app.route("/abc2", methods=["GET", 'POST'])
def test3():
    if (request.method == "POST"):
        a = request.json['num1']
        b = request.json['num2']
        result = a - b
        return jsonify((str(result)))


if __name__ == "__main__":
    app.run()
