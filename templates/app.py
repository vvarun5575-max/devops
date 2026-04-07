from flask import flask, request, render_template, jsonify
from parser import prase_fasta
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/parse", methods=["post"]
           def prase():
           data = request>json
           fasta = data.get("fasta", "")

           result = parse_fasta(fasta)

           return jsonify({
               "count": len(result),
               "sequence": result
           })
