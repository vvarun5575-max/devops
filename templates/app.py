from flask import Flask,request,render_template
import subprocess##we are runnign the blat in the docker environment so we need to import subprocess to run the command line blastn command and get the output
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])  
def index():
    result = ""

    if request.method == 'POST':#handling the user input from the form and running the blastn command
        sequence = request.form.get('sequence0',"").strip()
#######checks validating the user input and writing it to a file that will be used as the query 
        if not sequence:
            return render_template('index.html', result="Please enter a valid sequence.")
        #check 1
        if len(sequence) > 200:
            return render_template('index.html', result="Sequence is too long. Please enter a sequence with less than 200 characters.") 
        
        quirey_file = "/app/quirey.fasta"# creating a fasta file with the user input sequence to be used as the query for blastn

        try:
            with open(quirey_file, 'w') as f:
                f.write(">query\n"+sequence)
        except Exception as e:
            return render_template('index.html', result=f"Error writing to file: {str(e)}")
        
    cmd = [
        "blastn",
        "-query", quirey_file,
        "-subject", "/data/test.fasta",
        "-outfmt", "6",
        "-task", "blastn-short",
        "-num_threads", "1",
        "-max_target_seqs", "5",
        "-word_size", "7"           
    ]
    try:
        res = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True
        )
        print("STDOUT:", res.stdout)
        print("STDERR:", res.stderr)
        
        if res.stdout:
            result = res.stdout
        elif res.stderr.strip():
            result = "error: " + res.stderr
        else:
            result = "No output from BLAST command."
    except subprocess.TimeoutExpired:
        result = "Error: BLAST command timed out."
    except Exception as e:
        result = f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)