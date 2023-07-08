from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        description = request.form['description']
        email = request.form['email']
        # Process the uploaded file as desired
        file.save('/path/to/save/' + file.filename)
        # Continue with your logic

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
