from flask import Flask, session, request,jsonify, make_response,render_template
import json
import base64
app = Flask(__name__)

@app.route("/")
def index():
    dp = json.dumps({"user":"guest", "message":"hacker easy"})
    fg = base64.b64encode(dp.encode("utf-8"))
    resp=make_response(render_template("index.html"))
    resp.set_cookie('ctf.flag', fg)
    if request.method == "DELETE":
        if "ctf.flag" in request.cookies:
            try:
                js = json.loads(base64.b64decode(request.cookies["ctf.flag"]))
                if js["user"] == "admin":
                    return "flag{flag_ctf_527287353}"
            except:
                return "Bad cookie"
    return resp
if __name__ =="__main__":
    app.run(port=80, host="0.0.0.0")
