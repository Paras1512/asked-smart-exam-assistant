from flask import Flask, render_template, request
import os
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
from utils.file_parser import extract_text_from_file
from utils.gpt_answer import generate_answer


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Main route
@app.route('/', methods=['GET', 'POST'])
def index():
    answer = ''
    if request.method == 'POST':
        file = request.files['file']
        question = request.form['question']
        marks = request.form['marks']

        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            notes_text = extract_text_from_file(filepath)
            answer = generate_answer(question, notes_text, marks)

    return render_template('index.html', answer=answer)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
