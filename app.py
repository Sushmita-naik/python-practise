from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to my Python Backend!"

# Route to get student data
@app.route("/student")
def student():
    data = {
        "name": "Sushmita",
        "age": 19,
        "course": "BCA"
    }
    return jsonify(data)

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
