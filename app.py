from flask import Flask, render_template
app = Flask(__name__)
import csv

a = csv.reader(open("static/phrases.csv"))
wordtable = []

for row in a:
    wordtable.append([row[0],row[1]])



@app.route("/")
def helloworld():
    return render_template("index.html",table=wordtable)


if __name__ == "__main__":
    app.debug = True
    app.run()

