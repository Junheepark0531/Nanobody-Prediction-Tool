from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    # Perform search logic here if needed
    if request.method == 'POST':
        search_query = request.form['search_query']
        print(f"Search Query: {search_query}")
    # Redirect to result_page.html
    return redirect(url_for('result_page'))

@app.route('/result_page')
def result_page():
    data = {
        'percentage': 80,
        'stability': 'unstable',
        'cell': 'human 293T cells',
        'group': 'Group 1',
        'strands': 'High C Strands'
    }
    return render_template('result_page.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)