from flask import Flask, render_template

app = Flask(__name__)

myName = "sebastian"

@app.route("/")
def hello():
	return ''' 
			<h1>Sebastina ar bast in the world</h1>
    ''' 

@app.route("/index")
def index():
	return render_template("index.html")

app.debug = True

if __name__ == "__main__":
    app.run()