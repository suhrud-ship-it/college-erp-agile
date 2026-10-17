from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the College ERP System",
        "status": "running"
    })

@app.route("/students")
def students():
    return jsonify({
        "students": [
            {"id": 1, "name": "Amit Kumar", "course": "Computer Engineering"},
            {"id": 2, "name": "Priya Sharma", "course": "Information Technology"}
        ]
    })

@app.route("/courses")
def courses():
    return jsonify({
        "courses": [
            {"id": 1, "name": "Artificial Intelligence"},
            {"id": 2, "name": "Web Development"}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
