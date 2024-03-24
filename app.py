from database import load_projects_from_db, load_project_from_db

app = Flask(_name_)


@app.route("/")
def hello_world():
  projects = load_projects_from_db()
  return render_template('home.html', projects=projects)


@app.route("/project/<id>")
def project_details(id):
  project = load_project_from_db(id)
  return render_template('project_details.html', project=project)


@app.route("/message")
def message():
  return render_template('contactus.html')


@app.route("/message_submitted", methods=['post'])
def message_submitted():
  data = request.form
  return render_template('message_submitted.html', data=data)


if _name_ == '_main_':
  app.run(host='0.0.0.0', debug=True)
