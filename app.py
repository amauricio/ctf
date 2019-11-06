from flask import Flask, session, request,jsonify, make_response,render_template
import json
app = Flask(__name__)

@app.route("/")
def index():
    data = jsonify({"user":"guest", "message":"hacker easy"})
    fg = base64.b64encode(data.encode("utf-8"))
    resp=make_response(render_template("index.html"))
    resp.set_cookie('ctf.flag', fg)
    if request.method == "DELETE":
        
    return resp
if __name__ =="__main__":
    app.run(port=80, host="0.0.0.0")
