from flask import Flask
from flask import request
import login

app = Flask(__name__)

@app.route("/")
def index():
    clusters = login.get_clusters()
    content_pre = """<form action="/create_namespace" method="get">
                <select name="cluster" id="cluster">"""
    options = ""
    for cluster in clusters:
      options =  options + """<option value=""" + cluster + """>""" + cluster +"""</option>"""
                
    content_post = """</select>
                <input type="submit" value="submit">
              </form>"""
    return content_pre + options + content_post

@app.route("/create_namespace")
def create_namespace():
    sc = request.args.get("cluster")
    return "The cluster is: " + sc 

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)