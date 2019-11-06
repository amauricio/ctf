from flask import Flask, session, request, render_template
app = Flask(__name__)

@app.route("/")
def index():
    Resp=make_response(render_template("index.html"))
    resp.set_cookie('somecookiename', 'I am cooki')
    return resp
if __name__ =="__main__":
    app.run(port=80, host="0.0.0.0")
