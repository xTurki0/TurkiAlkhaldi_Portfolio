@app.route('/message')
def message():
  return render_template('contactus.html')


@app.route("/message_submitted", methods=['POST'])
def message_submitted():
  data = request.form
  add_message_to_db(data)
  return render_template('message_submitted.html', data=data)


if _name_ == '_main_':
  app.run(host='0.0.0.0', debug=True)
