from flask import Flask, render_template , jsonify

app = Flask(__name__, template_folder="template")


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS, company_name="Jovian")


@app.route("/jobs")

def jobs_in_jason():
    return jsonify(JOBS)


JOBS = [{
    "id": 1,
    "title": "Data analyst",
    "location": "Bengaluru India",
    "salary": "RS 1500000",
}, {
    "id": 2,
    "title": "Data Science",
    "location": "Mumbai India",
    "salary": "RS 1000000",
}, {
    "id": 3,
    "title": "Frontend Engineer",
    "location": "Delhi India",
    "salary": "RS 1200000",
}, {
    "id": 4,
    "title": "Backend Engineer",
    "location": "Bengaluru India",
    "salary":  "RS 1300000",
}]

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
