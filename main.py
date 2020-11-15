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
    
def append_id(id):
  """Add to list of ID"""
  pass

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == "POST":
    link = request.form['link']
    #return redirect(link)
    
    id = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    #id = "deeznuts"
    data(id, link)
    return render_template("newlink.html", link=id)

  if request.method == 'GET':
    return render_template("index.html")

@app.route("/<id>")
def redirect_url(id):
  #link = request.form['link']
  #return redirect(link)
  
  try:
    file = open("url.json", "r")
    data = json.load(file)

  except:
    return
  
  if data["data"]["id"] == id:
    url = data["data"]["link"]
    print(url)
    return redirect(url)
    
  else:
    return render_template("404.html")
  
  """with open("url.json", "r") as f:
    data = json.load(f)
    if data["data"]["id"] == id:
      url = data["data"]["link"]
      print(url)
      #return render_template("index.html")
      return redirect(url)
      
    else:
      return render_template("404.html")"""

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
