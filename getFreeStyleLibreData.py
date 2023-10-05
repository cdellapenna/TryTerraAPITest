from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook-endpoint', methods=['POST'])
def webhook_listener():
    data = request.get_json()
    print("Data received:", data)
    return jsonify({"message": "Data received successfully!"})

if __name__ == '__main__':
    # Run on http://localhost:5000/
    app.run(port=5000, debug=True)