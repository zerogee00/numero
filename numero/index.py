from flask import Flask, jsonify, request
app = Flask(__name__)

numbers = {}


@app.route("/increment", methods=['POST'])
def increment():
    if request.json in numbers:
        numbers[request.json] += 1
    else:
        numbers[request.json] = 1

    return jsonify(numbers[request.json])


@app.route("/decrement", methods=['POST'])
def decrement():
    if request.json in numbers:
        if numbers[request.json] != 0:
            numbers[request.json] -= 1
            return jsonify(numbers[request.json])
        else:
            return jsonify(str(request.json) + ' would enter negative'), 403
    else:
        return jsonify(str(request.json) + ' does not exist'), 404


@app.route("/remove", methods=['POST'])
def remove():
    if request.json in numbers:
        del numbers[request.json]
        return jsonify(str(request.json) + ' removed')
    else:
        return jsonify(str(request.json) + ' does not exist'), 404


@app.route("/history")
def history():
    return jsonify(numbers)


if __name__ == "__main__":
    app.run()
