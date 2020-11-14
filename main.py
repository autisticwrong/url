from flask import Flask, redirect, render_template, request
import random, string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == "POST":
    #link = request.form['link']
    #return redirect(link)
    id = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return render_template("newlink.html", link=id)

  if request.method == 'GET':
    return render_template("index.html")

@app.route("/<id>")
def redirect_url(id):
  #link = request.form['link']
  #return redirect(link)
  pass

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)  app.run(host='0.0.0.0', port=8080, debug=True)
