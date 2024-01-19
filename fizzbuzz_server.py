from flask import Flask, request, jsonify, render_template
from collections import Counter

app = Flask(__name__)

# Store statistics
request_stats = Counter()

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/', methods=['GET'])
def hello():
    return "Hello, welcome to the Fizz-Buzz REST Server!"

@app.route('/fizzbuzz', methods=['POST'])
def fizzbuzz():
    int1 = int(request.args.get('int1', 0))  # Default to 0 if not provided
    int2 = int(request.args.get('int2', 0))
    limit = int(request.args.get('limit', 1))  # Default to 1 if not provided
    str1 = request.args.get('str1', '')
    str2 = request.args.get('str2', '')

    output = []

    for num in range(1, limit + 1):
        result = ''
        if int1 and num % int1 == 0:  # Check if int1 is not 0 before performing modulo
            result += str1
        if int2 and num % int2 == 0:
            result += str2
        output.append(result or str(num))

    # Log the request for statistics
    request_stats[(int1, int2, limit, str1, str2)] += 1

    return jsonify(output)

@app.route('/statistics', methods=['GET'])
def statistics():
    most_used_request = request_stats.most_common(1)
    if most_used_request:
        params, hits = most_used_request[0]
        return jsonify({'parameters': params, 'hits': hits})
    else:
        return jsonify({'message': 'No requests yet'})

if __name__ == '__main__':
    app.run(debug=True)
