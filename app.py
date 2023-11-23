from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Python Developer",
        "location": "New York",
        "salary": "Rs. 2000$"
    },
    {
        "id": 2,
        "title": "Python Lead",
        "location": "Delhi",
        "salary": "Rs. 5000$"
    },
    {
        "id": 3,
        "title": "FSE",
        "location": "Remote"
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html",
                           jobs=JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
