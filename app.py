from flask import (
    Flask, 
    render_template, 
    redirect, 
    url_for, 
    request
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Perform search logic here if needed
    
    # Redirect to result_page.html
    return redirect(url_for('result_page'))

@app.route('/result_page')
def result_page():
    return render_template('result_page.html')

if __name__ == '__main__':
    app.run(debug=True)