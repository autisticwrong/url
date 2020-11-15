from flask import Flask, redirect, render_template, request
import random, string, json

app = Flask(__name__)

def data(id, link):
  x = {
      "data": {
        "id": id,
        "link": link
      }
    }

  with open("url.json", "w") as f:
    json.dump(x, f)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == "POST":
    link = request.form['link']
    #return redirect(link)
    
    id = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    data(id, link)
    return render_template("newlink.html", link=id)

  if request.method == 'GET':
    return render_template("index.html")

@app.route("/<id>")
def redirect_url(id):
  #link = request.form['link']
  #return redirect(link)
  with open("url.json", "r") as f:
    data = json.load(f)
    if data["data"]["id"] == id:
      url = data["data"]["link"]
      print(url)
    #return render_template("index.html")
    return redirect(url)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
