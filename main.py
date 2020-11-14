from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == "POST":
    link = request.form['link']
    #return redirect(link)
    return render_template("newlink.html", )

  if request.method == 'GET':
    return render_template("index.html")

@app.route("/<id>")
def redirect_url(id):
  redirect("home")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
