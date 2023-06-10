from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Receptionist',
  'location': 'Roftloc,Vinland',
  'salary': '$ 40,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Tapshire,Vinland',
  'salary': '$ 80,000'
}, {
  'id': 3,
  'title': 'Frontend Engineer',
  'location': 'Remote',
  'salary': '$ 70,000'
}, {
  'id': 4,
  'title': 'Data Entry',
  'location': 'Remote',
  'salary': '$20/hr'
}]


@app.route("/")
def hello():
  return render_template("home.html", jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
