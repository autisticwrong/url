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
    
def check_user(id, link):
  """Add to list of ID"""
  file = open("url.json", "r")
  data = json.load(file)

  if not str(id) in data:
    data[str(id)] = {}
    data[str(id)]["link"] = link
    dumps = open("url.json", "w")
    json.dump(data, dumps, indent = 4)
    return
  else:
    pass

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == "POST":
    link = request.form['link']
    #return redirect(link)
    
    id = "".join(random.choices(string.ascii_lowercase + string.digits, k=6))
    #id = "deeznuts"
    check_user(id, link)
    #data(id, link)
    return render_template("newlink.html", link=id)

  if request.method == 'GET':
    return render_template("index.html")
    
  return render_template("index.html")

@app.route("/<id>")
def redirect_url(id):
  pass
  #link = request.form['link']
  #return redirect(link)
  
  try:
    file = open("url.json", "r")
    data = json.load(file)
    #print(data)

  except:
    return
  
  #if id in data[str(id)]:
  if id in data:
    url = data[str(id)]["link"]
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
  app.run(host='0.0.0.0', port=8080)
